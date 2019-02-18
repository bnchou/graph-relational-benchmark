from neo4j import GraphDatabase
from statistics import median, mean
import json
from .database import random_entry, load_data, get_json, build_json

output = {}

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))

data = load_data()

def run_query(transaction, query, inputs=[]):
    def execute(tx):
        result = tx.run(query.format(*inputs)).consume()
        return result.t_first

    return transaction(execute)


def get_stats(exec, amount=500):

    res = [exec() for i in range(amount)]
    res.remove(min(res))
    res.remove(min(res))
    res.remove(max(res))
    res.remove(max(res))
    print("median: {}, mean: {}".format(median(res), mean(res)))

    output['cypher'] = res

def get_deals():
    with driver.session() as session:
        get_stats(lambda: run_query(session.read_transaction, '''
            MATCH (p:Person)-[:RESPONSIBLE_FOR]->(d: Deal)
            MATCH (p)-[WORKS_AT]->(c: Company)
            WHERE d.probability > {}
            RETURN p.name, p.position, p.email, p.phone, d.name, c.name;
        ''', [random_entry(data, 'deals', 'probability')]))

    build_json(output)
    return get_json()

def get_history():
    with driver.session() as session:
        get_stats(lambda: run_query(session.read_transaction, '''
                MATCH (deal:Deal)-[:PART_OF]->(history:History)<-[:ATTACHED_TO]-(document:Document)
                MATCH (coworker:Coworker)-[:ATTENDED]->(history)<-[:ATTENDED]-(person:Person)
                WHERE history.id = {}
                RETURN history.id, history.type, history.date, coworker.name, person.name, document.description;
            ''', [random_entry(data, 'histories', 'id')]))

    build_json(output)
    return get_json()

def get_persons():
    with driver.session() as session:
        get_stats(lambda: run_query(session.read_transaction, '''
                MATCH (p: Person)-[:WORKS_AT]->(c:Company)
                WHERE c.id = {}
                RETURN p.name, c.name;
            ''', [random_entry(data, 'companies', 'id')]))
    
    build_json(output)
    return get_json()

def update_deals():
    with driver.session() as session:
        get_stats(lambda: run_query(session.write_transaction, '''
                MATCH (d: Deal)<-[:RESPONSIBLE_FOR]-(p:Person)
                WHERE p.company_id = {}
                SET d.probability = 0.99
                RETURN d;''', [random_entry(data, 'persons', 'company_id')]
            ))

    build_json(output)
    return get_json()

def update_comp_names():
    with driver.session() as session:
         get_stats(lambda: run_query(session.write_transaction, '''
            MATCH (c: Company)
            WHERE c.id = {}
            SET c.name = 'Test'
            RETURN c.name;''', [random_entry(data, 'companies', 'id')]
        ))

    build_json(output)
    return get_json()

if __name__ == "__main__":
        # get_stats(lambda: run_query(session.write_transaction, '''
        #     MATCH (h: History)
        #     WHERE h.id = {}
        #     DETACH DELETE h;''', [random_entry(data, 'histories', 'id')]
        # ))
    get_deals()

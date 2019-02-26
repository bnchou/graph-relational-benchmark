from neo4j import GraphDatabase
from statistics import median, mean
import random
import os
from .database import random_entry, load_data

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))

data = load_data()

queries = {
    'companies': lambda session: get_stats(lambda: run_query(session.write_transaction, '''
        MATCH (c: Company)
        WHERE c.id = {}
        SET c.name = 'Test'
        RETURN c.name;''', [random_entry(data, 'companies', 'id')])),
    'persons': lambda session: get_stats(lambda: run_query(session.read_transaction, '''
        MATCH (p: Person)-[:WORKS_AT]->(c:Company)
        WHERE c.id = {}
        RETURN p.name, c.name;
    ''', [random_entry(data, 'companies', 'id')])),
    'deals': lambda session: get_stats(lambda: run_query(session.read_transaction, '''
        MATCH (p:Person)-[:RESPONSIBLE_FOR]->(d: Deal)
        MATCH (p)-[WORKS_AT]->(c: Company)
        WHERE d.probability > {}
        RETURN p.name, p.position, p.email, p.phone, d.name, c.name;
    ''', [random_entry(data, 'deals', 'probability')])),
    'documents': lambda session: get_stats(lambda: run_query(session.read_transaction, '''
        MATCH (person:Person)-[:OWNS]->(document:Document),
        (document)-[:ATTACHED_TO]->(deal:Deal)
        WHERE person.id = {}
        RETURN document.id, document.description, document.type, deal.name;''', [random_entry(data, 'persons', 'id')])),
    'histories': lambda session: get_stats(lambda: run_query(session.read_transaction, '''
        MATCH (deal:Deal)-[:PART_OF]->(history:History)<-[:ATTACHED_TO]-(document:Document)
        MATCH (coworker:Coworker)-[:ATTENDED]->(history)<-[:ATTENDED]-(person:Person)
        WHERE history.id = {}
        RETURN history.id, history.type, history.date, coworker.name, person.name, document.description;
    ''', [random_entry(data, 'histories', 'id')])),
    'update_deals': lambda session: get_stats(lambda: run_query(session.write_transaction, '''
        MATCH (d: Deal)<-[:RESPONSIBLE_FOR]-(p:Person)-[:WORKS_AT]->(c:Company)
        WHERE c.id = {}
        SET d.probability = 0.99
        RETURN d;''', [random_entry(data, 'persons', 'company_id')])),
    'create_history': lambda session: get_stats(lambda: run_query(session.write_transaction, '''
        MERGE (h: History {{id: {}, type: 'Call', notes: 'Created', date: '2018-03-15' }})
        MERGE (doc: Document {{id: {} }})
        MERGE (d: Deal {{id: {} }})
        MERGE (p: Person {{id: {} }})
        MERGE (c: Coworker {{id: {} }})
        MERGE (h)<-[:ATTACHED_TO]-(doc)
        MERGE (h)<-[:PART_OF]-(d)
        MERGE (h)<-[:ATTENDED]-(p) 
        MERGE (h)<-[:ATTENDED]-(c);''', [
        random.randint(40000000, 90000000),
        random_entry(data, 'documents', 'id'),
        random_entry(data, 'deals', 'id'),
        random_entry(data, 'persons', 'id'),
        random_entry(data, 'coworkers', 'id')
    ])),
    'create_person': lambda session: get_stats(lambda: run_query(session.write_transaction, '''
        MERGE (p: Person {{id: {}, name: 'Inserted Name', phone: '07012345678', position: 'CEO', email: 'insert@insert.com'}})
        MERGE (c: Company {{id: {} }})
        MERGE (p)-[:WORKS_AT]->(c);''', [random.randint(2000000, 3000000), random_entry(data, 'companies', 'id')])),
    'create_deal': lambda session: get_stats(lambda: run_query(session.write_transaction, '''
        MERGE (d: Deal {{id: {}, name: 'Best Deal Ever', value: 10, probability: 0.99999}})
        MERGE (p: Person {{id: {} }})
        MERGE (c: Coworker {{id: {} }})
        MERGE (p)-[:RESPONSIBLE_FOR]->(d)<-[:SALESPERSON_FOR]-(c)
        ;''', [
        random.randint(9999999, 900000000),
        random_entry(data, 'persons', 'id'),
        random_entry(data, 'coworkers', 'id')
    ]))
}


def run_query(transaction, query, inputs=[]):
    print('|', end='', flush=True)

    def execute(tx):
        result = tx.run(query.format(*inputs)).consume()
        return result.t_first

    return transaction(execute)


def get_stats(exec, amount=500):
    if(os.path.isfile('amount.txt')):
        for line in open('amount.txt', 'r'):
            if(line.strip()):
                amount = int(line)
    res = [exec() for i in range(amount)]
    for _ in range(int(amount * 0.05)):
        res.remove(min(res))
        res.remove(max(res))
    return res


def run(stmt):
    with driver.session() as session:
        return queries[stmt](session)

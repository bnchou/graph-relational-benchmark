from neo4j import GraphDatabase
from statistics import median, mean

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
        MATCH (d: Deal)<-[:RESPONSIBLE_FOR]-(p:Person)
        WHERE p.company_id = {}
        SET d.probability = 0.99
        RETURN d;''', [random_entry(data, 'persons', 'company_id')]))
}


def run_query(transaction, query, inputs=[]):
    def execute(tx):
        result = tx.run(query.format(*inputs)).consume()
        return result.t_first

    return transaction(execute)


def get_stats(exec, amount=54):
    res = [exec() for i in range(amount)]
    res.remove(min(res))
    res.remove(min(res))
    res.remove(max(res))
    res.remove(max(res))
    return res


def run(stmt):
    with driver.session() as session:
        return queries[stmt](session)

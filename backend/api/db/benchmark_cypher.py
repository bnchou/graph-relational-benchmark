from neo4j import GraphDatabase
from statistics import median, mean
import random
import os
from .database import random_entry, load_data

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))

data = load_data()

raw_queries = {
    'get': {
        'persons': '''
            MATCH (p: Person)-[:OWNS]->(d: Document)
            WHERE p.id = {}
            RETURN d.id, p.id, p.name, d.type, d.description;''',
        'deals': '''
            MATCH (p: Person)-[:RESPONSIBLE_FOR]->(d: Deal),
            (p)-[:WORKS_AT]->(c: Company)
            WHERE d.probability > {}
            RETURN p.name, p.position, p.email, p.phone, d.name, c.name;''',
        'documents': '''
            MATCH (person:Person)-[:OWNS]->(document:Document),
            (document)-[:ATTACHED_TO]->(deal:Deal)
            WHERE person.id = {}
            RETURN document.id, document.description, document.type, deal.name;''',
        'histories': '''
            MATCH (deal: Deal)-[:PART_OF]->(h: History),
            (h)<-[:ATTACHED_TO]-(d:Document),
            (c: Coworker)-[:ATTENDED]->(h)<-[:ATTENDED]-(p: Person)
            WHERE deal.id = {}
            RETURN h.id, h.type, h.date, c.name, p.name, d.description;''',
        'advanced_coworkers': '''
            MATCH (c: Company)<-[:WORKS_AT]-(p: Person),
            (p)-[:RESPONSIBLE_FOR]->(d: Deal),
            (d)<-[:SALESPERSON_FOR]-(co: Coworker)
            WHERE co.name =~ '{}.*' AND c.city =~ '{}.*'
            RETURN co.name, c.name, c.city;''',
        'advanced_histories': '''
            MATCH (d: Deal)<-[:PART_OF]-(h:History)
            WHERE d.value > {} AND h.type = 'Call'
            AND h.date < '{}'
            RETURN d.name, h.date;''',
    },
    'post': {
        'history': '''
            MERGE (h: History {{id: {}, type: 'Call', notes: 'Created', date: '2018-03-15' }})
            MERGE (doc: Document {{id: {} }})
            MERGE (d: Deal {{id: {} }})
            MERGE (p: Person {{id: {} }})
            MERGE (c: Coworker {{id: {} }})
            MERGE (h)<-[:ATTACHED_TO]-(doc)
            MERGE (h)<-[:PART_OF]-(d)
            MERGE (h)<-[:ATTENDED]-(p) 
            MERGE (h)<-[:ATTENDED]-(c);''',
        'person': '''
            MERGE (p: Person {{id: {}, name: 'Inserted Name', phone: '07012345678', position: 'CEO', email: 'insert@insert.com'}})
            MERGE (c: Company {{id: {} }})
            MERGE (p)-[:WORKS_AT]->(c);''',
        'deal': '''
            MERGE (d: Deal {{id: {}, name: 'Best Deal Ever', value: 10, probability: 0.99999}})
            MERGE (p: Person {{id: {} }})
            MERGE (c: Coworker {{id: {} }})
            MERGE (p)-[:RESPONSIBLE_FOR]->(d)<-[:SALESPERSON_FOR]-(c);''',
    },
    'put': {
        'companies': '''
            MATCH (c: Company)
            WHERE c.id = {}
            SET c.name = 'Test'
            RETURN c.name;''',
        'deals': '''
            MATCH (d: Deal)<-[:RESPONSIBLE_FOR]-(p:Person)-[:WORKS_AT]->(c:Company)
            WHERE c.id = {}
            SET d.probability = 0.99
            RETURN d;''',
    }
}

queries = {
    'get_persons': lambda session: get_stats(lambda: run_query(session.read_transaction, raw_queries['get']['persons'], [random_entry(data, 'companies', 'id')])),
    'get_deals': lambda session: get_stats(lambda: run_query(session.read_transaction, raw_queries['get']['deals'], [random_entry(data, 'deals', 'probability')])),
    'get_documents': lambda session: get_stats(lambda: run_query(session.read_transaction, raw_queries['get']['documents'], [random_entry(data, 'persons', 'id')])),
    'get_histories': lambda session: get_stats(lambda: run_query(session.read_transaction, raw_queries['get']['histories'], [random_entry(data, 'deals', 'id')])),
    'get_advanced_coworkers': lambda session: get_stats(lambda: run_query(session.read_transaction, raw_queries['get']['advanced_coworkers'], [
        random_entry(data, 'coworkers', 'name').split()[0],
        random_entry(data, 'companies', 'city')
    ])),
    'get_advanced_histories': lambda session: get_stats(lambda: run_query(session.read_transaction, raw_queries['get']['advanced_histories'], [
        random_entry(data, 'deals', 'value'),
        random_entry(data, 'histories', 'date')
    ])),
    'put_companies': lambda session: get_stats(lambda: run_query(session.write_transaction, raw_queries['put']['companies'], [random_entry(data, 'companies', 'id')])),
    'put_deals': lambda session: get_stats(lambda: run_query(session.write_transaction, raw_queries['put']['deals'], [random_entry(data, 'persons', 'company_id')])),
    'post_history': lambda session: get_stats(lambda: run_query(session.write_transaction, raw_queries['post']['history'], [
        random.randint(40000000, 90000000),
        random_entry(data, 'documents', 'id'),
        random_entry(data, 'deals', 'id'),
        random_entry(data, 'persons', 'id'),
        random_entry(data, 'coworkers', 'id')
    ])),
    'post_person': lambda session: get_stats(lambda: run_query(session.write_transaction, raw_queries['post']['person'], [random.randint(2000000, 3000000), random_entry(data, 'companies', 'id')])),
    'post_deal': lambda session: get_stats(lambda: run_query(session.write_transaction, raw_queries['post']['deal'], [
        random.randint(9999999, 900000000),
        random_entry(data, 'persons', 'id'),
        random_entry(data, 'coworkers', 'id')
    ])),
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

from neo4j import GraphDatabase
from statistics import mean, stdev
import random
import os
from .database import random_entry, load_data

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))

data = load_data()

raw_queries = {
    'get': {
        'documents': '''
            MATCH (d: Deal)<-[:PART_OF]-(h: History),
            (h)<-[:ATTENDED]-(co: Coworker),
            (h)<-[:ATTENDED]-(p: Person),
            (p)-[:WORKS_AT]->(c: Company)
            WHERE h.type = '{}'
            RETURN h.date, co.name, h.type, p.name, c.name, d.name
            LIMIT 10000;''',
        'persons': '''
            MATCH (p: Person)-[:WORKS_AT]->(c: Company)
            WHERE c.id = {}
            RETURN p.name, p.email, c.name
            LIMIT 10000;''',
        'filter_histories': '''
            MATCH (d: Deal)<-[:PART_OF]-(h: History),
            (h)<-[:ATTACHED_TO]-(doc: Document),
            (h)<-[:ATTENDED]-(c: Coworker),
            (h)<-[:ATTENDED]-(p: Person)
            WHERE d.id = {} AND h.type = 'Call'
            AND h.date < '{}'
            RETURN h.date, c.name, h.type, p.name, doc.description
            LIMIT 10000;''',
        'histories': '''
            MATCH (d: Deal)<-[:PART_OF]-(h: History),
            (h)<-[:ATTACHED_TO]-(doc: Document),
            (h)<-[:ATTENDED]-(c: Coworker),
            (h)<-[:ATTENDED]-(p: Person)
            WHERE (h.type =~ '{}.*' OR c.name =~ '{}.*' OR p.name =~ '{}.*' OR doc.description =~ '{}.*')
            AND (h.type =~ '{}.*' OR c.name =~ '{}.*' OR p.name =~ '{}.*' OR doc.description =~ '{}.*')
            RETURN h.type, h.date, c.name, p.name, doc.description
            LIMIT 10000;''',
        'filter_coworkers': '''
            MATCH (c: Company)<-[:WORKS_AT]-(p: Person),
            (d: Deal)<-[:RESPONSIBLE_FOR]-(p),
            (d)<-[:SALESPERSON_FOR]-(co: Coworker)
            WHERE co.name =~ '{}.*' AND c.city =~ '{}.*'
            RETURN co.name, c.name, c.city
            LIMIT 10000;''',
        'deals': '''
            MATCH (p: Person)-[:RESPONSIBLE_FOR]->(d: Deal),
            (p)-[:WORKS_AT]->(c: Company)
            WHERE d.probability > {} AND c.name =~ '{}.*'
            RETURN p.name, p.email, p.phone, d.name, c.name
            LIMIT 10000;''',
        'transfer_deals': '''
            MATCH (co: Coworker)-[:SALESPERSON_FOR]->(d: Deal),
            (d)<-[:RESPONSIBLE_FOR]-(p1: Person)
            WITH d.id as d_id
            WHERE d.name =~ '{}.*' OR p1.name =~ '{}.*' OR co.name =~ '{}.*'
            MATCH (h: History)-[:PART_OF]->(deal: Deal {{id: d_id}}),
            (h)<-[:ATTENDED]-(p2: Person)
            RETURN COLLECT(DISTINCT p2.name), p2.email
            LIMIT 10000;''',
        'top_deal': '''
            MATCH (d: Deal)<-[:SALESPERSON_FOR]-(co: Coworker)
            WITH co.id as id, d.probability as prob
            ORDER BY d.probability DESC LIMIT 1
            MATCH (c: Coworker {{id: id}})-[:SALESPERSON_FOR]->(deal: Deal)
            WHERE deal.probability > {}
            RETURN deal.name, deal.value, deal.probability, c.name
            LIMIT 10000;'''

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
            MERGE (d)<-[:RESPONSIBLE_FOR]-(p)
            MERGE (d)<-[:SALESPERSON_FOR]-(c);''',
    },
    'put': {
        'companies': '''
            MATCH (c: Company)
            WHERE c.id = {}
            SET c.name = 'Test'
            RETURN c.name;''',
        'deals': '''
            MATCH (d: Deal)<-[:RESPONSIBLE_FOR]-(p: Person),
            (p)-[:WORKS_AT]->(c: Company)
            WHERE c.id = {}
            SET d.probability = 0.99
            RETURN d;''',
    }
}

queries = {
    'get_top_deal': lambda session: get_stats(lambda: run_query(session.read_transaction, raw_queries['get']['top_deal'], [random_entry(data, 'deals', 'probability')])),
    'get_documents': lambda session: get_stats(lambda: run_query(session.read_transaction, raw_queries['get']['documents'], [random_entry(data, 'histories', 'type')])),
    'get_persons': lambda session: get_stats(lambda: run_query(session.read_transaction, raw_queries['get']['persons'], [random_entry(data, 'companies', 'id')])),
    'get_histories': lambda session: get_stats(lambda: run_query(session.read_transaction, raw_queries['get']['histories'], [
        random_entry(data, 'persons', 'name')[:1],
        random_entry(data, 'persons', 'name')[:1],
        random_entry(data, 'persons', 'name')[:1],
        random_entry(data, 'persons', 'name')[:1],
        random_entry(data, 'documents', 'description')[:1],
        random_entry(data, 'documents', 'description')[:1],
        random_entry(data, 'documents', 'description')[:1],
        random_entry(data, 'documents', 'description')[:1],
    ])),
    'get_filter_coworkers': lambda session: get_stats(lambda: run_query(session.read_transaction, raw_queries['get']['filter_coworkers'], [
        random_entry(data, 'coworkers', 'name').split()[0],
        random_entry(data, 'companies', 'city')[:2]
    ])),
    'get_filter_histories': lambda session: get_stats(lambda: run_query(session.read_transaction, raw_queries['get']['filter_histories'], [
        random_entry(data, 'deals', 'id'),
        random_entry(data, 'histories', 'date')
    ])),
    'get_deals': lambda session: get_stats(lambda: run_query(session.read_transaction, raw_queries['get']['deals'], [
        random_entry(data, 'deals', 'probability'),
        random_entry(data, 'companies', 'name')[:2],
    ])),
    'get_transfer_deals': lambda session: get_stats(lambda: run_query(session.read_transaction, raw_queries['get']['transfer_deals'], [
        random_entry(data, 'persons', 'name')[:5],
        random_entry(data, 'persons', 'name')[:5],
        random_entry(data, 'persons', 'name')[:5]
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

    def execute(tx):
        result = tx.run(query.format(*inputs))
        print('|{}'.format(len(result.values())), end='', flush=True)
        consumed = result.consume()
        return consumed.t_first + consumed.t_last

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
    print("\nMean: {}, Std: {}".format(mean(res), stdev(res)))
    return res


def run(stmt):
    with driver.session() as session:
        return queries[stmt](session)

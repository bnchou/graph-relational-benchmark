from neo4j import GraphDatabase
import query_randomizer as q
from time import time

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))


def get_persons_with_deal_prob(tx, prob):
    query = '''
        MATCH (p:Person)-[:RESPONSIBLE_FOR]->(d: Deal)
        MATCH (p)-[WORKS_AT]->(c: Company)
        WHERE d.probability > {}
        RETURN p.name, p.position, p.email, p.phone, d.name, c.name;
        '''.format(prob)

    for record in tx.run(query):
        p_name = record["p.name"].encode('UTF-8')
        p_pos = record["p.position"].encode('UTF-8')
        p_mail = record["p.email"].encode('UTF-8')
        p_phone = record["p.phone"].encode('UTF-8')
        d_name = record["d.name"].encode('UTF-8')
        c_name = record["c.name"].encode('UTF-8')

        print("{} | {} | {} | {} | {} | {}".format(p_name, p_pos, p_mail, p_phone, d_name, c_name))

def get_companies(tx):
    query = '''
        MATCH (c: Company)
        RETURN c.name, c.id;
        '''
        
    for record in tx.run(query):
        print("{} | {}".format(record["c.name"].encode('UTF-8'), record["c.id"]))

def get_history(tx, id):
    query = '''
        MATCH (deal:Deal)-[:PART_OF]->(history:History)<-[:ATTACHED_TO]-(document:Document)
        MATCH (coworker:Coworker)-[:ATTENDED]->(history)<-[:ATTENDED]-(person:Person)
        WHERE history.id = {}
        RETURN history.id, history.type, history.date, coworker.name, person.name, document.description;
        '''.format(id)

    for record in tx.run(query):
        h_id = record["history.id"]
        h_type = record["history.type"]
        h_date = record["history.date"]
        c_name = record["coworker.name"]
        p_name = record["person.name"]
        d_desc = record["document.description"]

        print("{} | {} | {} | {} | {} | {}".format(h_id, h_type, h_date, c_name, p_name, d_desc))
        

def get_company_persons(tx, id):
    query = '''
        MATCH (p: Person)-[:WORKS_AT]->(c:Company)
        WHERE c.id = {}
        RETURN p.name, c.name;'''.format(id)

    for record in tx.run(query):
        print("{} | {}".format(record["p.name"].encode('UTF-8'), record["c.name"].encode('UTF-8')))

with driver.session() as session:
    # t = time()
    # session.read_transaction(get_companies)
    # print((time() - t) * 1000)
    #session.read_transaction(get_persons_with_deal_prob, q.rand_entry('deals', 'probability'))
    t = time()
    session.read_transaction(get_history, q.rand_entry('histories', 'id'))
    print((time() - t) * 1000)
    #session.read_transaction(get_company_persons, q.rand_entry('companies', 'id'))
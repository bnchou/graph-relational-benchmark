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

    result = tx.run(query).consume()
    print("{} ms, {} ms".format(result.t_first, result.t_last))


def get_companies(tx):
    query = '''
        MATCH (c: Company)
        RETURN c.name, c.id;
        '''

    result = tx.run(query).consume()
    print("{} ms, {} ms".format(result.t_first, result.t_last))


def get_history(tx, id):
    query = '''
        MATCH (deal:Deal)-[:PART_OF]->(history:History)<-[:ATTACHED_TO]-(document:Document)
        MATCH (coworker:Coworker)-[:ATTENDED]->(history)<-[:ATTENDED]-(person:Person)
        WHERE history.id = {}
        RETURN history.id, history.type, history.date, coworker.name, person.name, document.description;
        '''.format(id)

    result = tx.run(query).consume()
    print("{} ms, {} ms".format(result.t_first, result.t_last))


def get_company_persons(tx, id):
    query = '''
        MATCH (p: Person)-[:WORKS_AT]->(c:Company)
        WHERE c.id = {}
        RETURN p.name, c.name;'''.format(id)

    result = tx.run(query).consume()
    print("{} ms, {} ms".format(result.t_first, result.t_last))


with driver.session() as session:
    session.read_transaction(get_companies)
    session.read_transaction(get_persons_with_deal_prob,
                             q.rand_entry('deals', 'probability'))
    session.read_transaction(get_history, q.rand_entry('histories', 'id'))
    session.read_transaction(
        get_company_persons, q.rand_entry('companies', 'id'))

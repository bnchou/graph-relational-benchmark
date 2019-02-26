from statistics import median, mean
from time import time
import pyodbc
import os
import random

from .database import random_entry, load_data

cnxn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER='+os.environ['SQL_SERVER']+';DATABASE=LimeDB;')

cursor = cnxn.cursor()

data = load_data()

queries = {
    'companies': lambda: get_stats(lambda: run_query(cursor.execute, '''
        UPDATE companies
        SET companies.name = 'Test'
        WHERE companies.id = {}''', [random_entry(data, 'companies', 'id')])),
    'persons': lambda: get_stats(lambda: run_query(cursor.execute, '''
        SELECT persons.name, companies.name
        FROM persons
        LEFT JOIN companies ON persons.company_id = companies.id
        WHERE companies.id = {};
    ''', [random_entry(data, 'companies', 'id')])),
    'deals': lambda: get_stats(lambda: run_query(cursor.execute, '''
        SELECT p.name, p.position, p.email, p.phone, deals.name, companies.name
        FROM persons AS p
        LEFT JOIN deals ON p.id = deals.person_id
        LEFT JOIN companies ON p.company_id = companies.id
        WHERE deals.probability > {}''',  [random_entry(data, 'deals', 'probability')])),
    'documents': lambda: get_stats(lambda: run_query(cursor.execute, '''
        SELECT documents.id, persons.id, persons.name, documents.type, documents.description
        FROM documents
        LEFT JOIN persons ON documents.person_id = persons.id
        WHERE documents.id IN (
            SELECT documents.id AS id
            FROM documents
            LEFT JOIN persons ON documents.person_id = persons.id
            WHERE  persons.id = {}
        );''', [random_entry(data, 'persons', 'id')])),
    'histories': lambda: get_stats(lambda: run_query(cursor.execute, '''
        SELECT histories.id, histories.date, coworkers.id, coworkers.name, histories.type, persons.id, persons.name, documents.id, documents.description, histories.notes
        FROM histories
        LEFT JOIN deals ON histories.deal_id = deals.id
        LEFT JOIN coworkers ON histories.coworker_id = coworkers.id
        LEFT JOIN persons ON histories.person_id = persons.id
        LEFT JOIN documents ON histories.document_id = documents.id
        WHERE (histories.id IN (
            SELECT histories.id AS id
            FROM histories
            LEFT JOIN deals ON histories.deal_id = deals.id
            WHERE  (deals.id = {})
            )
        );''', [random_entry(data, 'deals', 'id')])),
    'update_deals': lambda: get_stats(lambda: run_query(cursor.execute, '''
        UPDATE deals
        SET deals.probability = 0.99
        WHERE deals.person_id IN (
            SELECT p.id
            FROM persons as p
            WHERE p.company_id = {}
        );''', [random_entry(data, 'persons', 'company_id')])),
    'create_history': lambda: get_stats(lambda: run_query(cursor.execute, '''
        INSERT INTO histories
        VALUES ({}, 'Call', '2018-03-15', 'Created', {}, {}, {}, {}
        );''', [
        random.randint(40000000, 90000000),
        random_entry(data, 'persons', 'id'),
        random_entry(data, 'coworkers', 'id'),
        random_entry(data, 'deals', 'id'),
        random_entry(data, 'documents', 'id')
    ])),
    'create_person': lambda: get_stats(lambda: run_query(cursor.execute, '''
        INSERT INTO persons
        VALUES ({}, 'Inserted Name', '07012345678', 'CEO', 'insert@insert.com', {}
        );''', [random.randint(40000000, 90000000), random_entry(data, 'companies', 'id')])),
    'create_deal': lambda: get_stats(lambda: run_query(cursor.execute, '''
        INSERT INTO deals
        VALUES ({}, 'Best Deal Ever', 10, 0.99999, {}, {}
        );''', [
        random.randint(40000000, 90000000),
        random_entry(data, 'persons', 'id'),
        random_entry(data, 'coworkers', 'id')
    ]))
}


def run_query(execute, query, inputs=[]):
    print('|', end='', flush=True)

    t1 = time()
    execute(query.format(*inputs))
    t2 = time()
    return (t2 - t1) * 1000


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
    return queries[stmt]()

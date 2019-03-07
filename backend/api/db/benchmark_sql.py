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
        SELECT p.name, c.name
        FROM persons AS p
        LEFT JOIN companies AS c
        ON p.company_id = c.id;
        WHERE c.id = {};
    ''', [random_entry(data, 'companies', 'id')])),
    'deals': lambda: get_stats(lambda: run_query(cursor.execute, '''
        SELECT p.name, p.position, p.email, p.phone, d.name, c.name
        FROM persons AS p
        LEFT JOIN deals AS d ON p.id = d.person_id
        LEFT JOIN companies AS c ON p.company_id = c.id
        WHERE d.probability > {}''',  [random_entry(data, 'deals', 'probability')])),
    'documents': lambda: get_stats(lambda: run_query(cursor.execute, '''
        SELECT d.id, p.id, p.name, d.type, d.description
        FROM documents AS d
        LEFT JOIN persons AS p 
        ON d.person_id = p.id
        WHERE persons.id = {};''', [random_entry(data, 'persons', 'id')])),
    'histories': lambda: get_stats(lambda: run_query(cursor.execute, '''
        SELECT h.id, h.type, h.date, c.name, p.name, d.description
        FROM histories AS h
        LEFT JOIN deals ON h.deal_id = deals.id 
        LEFT JOIN coworkers AS c ON h.coworker_id = c.id 
        LEFT JOIN persons AS p ON h.person_id = p.id 
        LEFT JOIN documents AS d ON h.document_id = d.id 
        WHERE deals.id = {};''', [random_entry(data, 'deals', 'id')])),
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
    ])),
    'advanced_coworkers': lambda: get_stats(lambda: run_query(cursor.execute, '''
        SELECT c.name, p.name
        FROM companies as c
        LEFT JOIN persons as p
        ON p.company_id = c.id
        LEFT JOIN deals as d
        ON deals.person_id = p.id
        LEFT JOIN coworkers as co
        ON co.id = d.coworker_id
        WHERE co.name LIKE '{}*' AND c.city LIKE '{}*';''', [
            random_entry(data, 'coworkers', 'name').split()[0],
            random_entry(data, 'companies', 'city')[:4]
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

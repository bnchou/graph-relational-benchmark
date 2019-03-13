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

raw_queries = {
    'get': {
        'persons': '''
            SELECT p.name, c.name
            FROM persons AS p
            LEFT JOIN companies AS c
            ON p.company_id = c.id
            WHERE c.id = {};''',
        'deals': '''
            SELECT p.name, p.email, p.phone, d.name, c.name
            FROM persons AS p
            LEFT JOIN deals AS d ON p.id = d.person_id
            LEFT JOIN companies AS c ON p.company_id = c.id
            WHERE d.probability > {};''',
        'documents': '''
            SELECT doc.id, doc.description, doc.type, d.name
            FROM documents AS doc
            LEFT JOIN persons AS p ON doc.person_id = p.id
            LEFT JOIN deals AS d ON doc.deal_id = d.id
            WHERE p.id = {};''',
        'histories': '''
            SELECT h.type, h.date, c.name, p.name, doc.description
            FROM histories AS h
            LEFT JOIN deals AS d ON h.deal_id = d.id 
            LEFT JOIN coworkers AS c ON h.coworker_id = c.id 
            LEFT JOIN persons AS p ON h.person_id = p.id 
            LEFT JOIN documents AS doc ON h.document_id = doc.id 
            WHERE d.id = {};''',
        'filter_coworkers': '''
            SELECT co.name, c.name, c.city
            FROM companies as c
            LEFT JOIN persons as p ON p.company_id = c.id
            LEFT JOIN deals as d ON d.person_id = p.id
            LEFT JOIN coworkers as co ON d.coworker_id = co.id
            WHERE co.name LIKE '{}*' AND c.city LIKE '{}*';''',
        'filter_histories': '''
            SELECT d.name, h.date
            FROM deals AS d
            LEFT JOIN histories AS h ON h.deal_id = d.id
            WHERE d.value > {} AND h.type = 'Call'
            AND h.date < '{}';'''
    },
    'post': {
        'history': '''
            INSERT INTO histories
            VALUES ({}, 'Call', '2018-03-15', 'Created', {}, {}, {}, {}
            );''',
        'person': '''
            INSERT INTO persons
            VALUES ({}, 'Inserted Name', '07012345678', 'CEO', 'insert@insert.com', {}
            );''',
        'deal': '''
            INSERT INTO deals
            VALUES ({}, 'Best Deal Ever', 10, 0.99999, {}, {}
            );''',
    },
    'put': {
        'companies': '''
            UPDATE companies
            SET companies.name = 'Test'
            WHERE companies.id = {};''',
        'deals': '''
            UPDATE deals
            SET deals.probability = 0.99
            WHERE deals.person_id IN (
                SELECT p.id
                FROM persons AS p
                WHERE p.company_id = {}
            );''',
    }
}

queries = {
    'get_persons': lambda: get_stats(lambda: run_query(cursor.execute, raw_queries['get']['persons'], [random_entry(data, 'companies', 'id')])),
    'get_deals': lambda: get_stats(lambda: run_query(cursor.execute, raw_queries['get']['deals'],  [random_entry(data, 'deals', 'probability')])),
    'get_documents': lambda: get_stats(lambda: run_query(cursor.execute, raw_queries['get']['documents'], [random_entry(data, 'persons', 'id')])),
    'get_histories': lambda: get_stats(lambda: run_query(cursor.execute, raw_queries['get']['histories'], [random_entry(data, 'deals', 'id')])),
    'get_filter_coworkers': lambda: get_stats(lambda: run_query(cursor.execute, raw_queries['get']['filter_coworkers'], [
        random_entry(data, 'coworkers', 'name').split()[0],
        random_entry(data, 'companies', 'city')
    ])),
    'get_filter_histories': lambda: get_stats(lambda: run_query(cursor.execute, raw_queries['get']['filter_histories'], [
        random_entry(data, 'deals', 'value'),
        random_entry(data, 'histories', 'date')
    ])),
    'post_history': lambda: get_stats(lambda: run_query(cursor.execute, raw_queries['post']['history'], [
        random.randint(40000000, 90000000),
        random_entry(data, 'persons', 'id'),
        random_entry(data, 'coworkers', 'id'),
        random_entry(data, 'deals', 'id'),
        random_entry(data, 'documents', 'id')
    ])),
    'post_person': lambda: get_stats(lambda: run_query(cursor.execute, raw_queries['post']['person'], [
        random.randint(40000000, 90000000),
        random_entry(data, 'companies', 'id')])),
    'post_deal': lambda: get_stats(lambda: run_query(cursor.execute, raw_queries['post']['deal'], [
        random.randint(40000000, 90000000),
        random_entry(data, 'persons', 'id'),
        random_entry(data, 'coworkers', 'id')
    ])),
    'put_companies': lambda: get_stats(lambda: run_query(cursor.execute, raw_queries['put']['companies'], [random_entry(data, 'companies', 'id')])),
    'put_deals': lambda: get_stats(lambda: run_query(cursor.execute, raw_queries['put']['deals'], [random_entry(data, 'persons', 'company_id')])),
}


def run_query(execute, query, inputs=[]):
    t1 = time()
    res = execute(query.format(*inputs)).fetchall()
    t2 = time()

    print('|{}'.format(len(res)), end='', flush=True)
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

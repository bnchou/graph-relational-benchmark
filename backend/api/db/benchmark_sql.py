from statistics import mean, stdev
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
        'histories_type': ('The query being benchmarked here returns all deals with the specified history type', '''
            SELECT TOP 10000 h.date, co.name, h.type, p.name, c.name, d.name
            FROM histories AS h
            LEFT JOIN deals AS d ON h.deal_id = d.id
            LEFT JOIN coworkers AS co ON h.coworker_id = co.id
            LEFT JOIN persons AS p ON h.person_id = p.id
            LEFT JOIN companies AS c ON p.company_id = c.id
            WHERE h.type = '{}';'''),
        'persons': ('The query being benchmarked here returns all persons working at a specific company', '''
            SELECT TOP 10000 p.name, p.email, c.name
            FROM persons AS p
            LEFT JOIN companies AS c ON p.company_id = c.id
            WHERE c.id = {};'''),
        'filter_histories': ('The query being benchmarked here returns all histories that are of type ’Call’ and before a specific date and that are part of the deal with the specified id', '''
            SELECT TOP 10000 h.date, c.name, h.type, p.name, doc.description
            FROM deals AS d
            LEFT JOIN histories AS h ON h.deal_id = d.id
            LEFT JOIN documents AS doc on h.document_id = doc.id
            LEFT JOIN persons AS p ON h.person_id = p.id
            LEFT JOIN coworkers AS c ON h.coworker_id = c.id
            WHERE d.id = {} AND h.type = 'Call'
            AND h.date < '{}';'''),
        'histories': ('The query being benchmarked here utilizes the filtering function in Lime CRM by typing two random data entities and looking through all possible columns for a potential hit', '''
            SELECT TOP 10000 h.type, h.date, c.name, p.name, doc.description
            FROM histories AS h
            LEFT JOIN deals AS d ON h.deal_id = d.id
            LEFT JOIN coworkers AS c ON h.coworker_id = c.id
            LEFT JOIN persons AS p ON h.person_id = p.id
            LEFT JOIN documents AS doc ON h.document_id = doc.id
            WHERE (h.type LIKE '{}%' OR c.name LIKE '{}%' OR p.name LIKE '{}%' OR doc.description LIKE '{}%')
            AND (h.type LIKE '{}%' OR c.name LIKE '{}%' OR p.name LIKE '{}%' OR doc.description LIKE '{}%');'''),
        'filter_coworkers': ('The query being benchmarked here returns all coworkers with a randomized first name that work in a randomized city beginning with the given letter combination', '''
            SELECT TOP 10000 co.name, c.name, c.city
            FROM companies as c
            LEFT JOIN persons as p ON p.company_id = c.id
            LEFT JOIN deals as d ON d.person_id = p.id
            LEFT JOIN coworkers as co ON d.coworker_id = co.id
            WHERE co.name LIKE '{}%' AND c.city LIKE '{}%';'''),
        'deals': ('The query being benchmarked here returns all deals above the given probability at a company beginning with the given letter combination', '''
            SELECT TOP 10000 p.name, p.email, p.phone, d.name, c.name
            FROM persons AS p
            LEFT JOIN deals AS d ON p.id = d.person_id
            LEFT JOIN companies AS c ON p.company_id = c.id
            WHERE d.probability > {} AND c.name LIKE '{}%';'''),
        'transfer_deals': ('The query being benchmarked here filters all deals containing a given word, selects all histories that are part of those deals and then returns all persons that are part of these histories', '''
            SELECT TOP 10000 p1.name, p1.email
            FROM persons AS p1
            LEFT JOIN histories AS h1 ON h1.person_id = p1.id
            WHERE h1.id IN (
                SELECT h2.id
                FROM histories AS h2
                WHERE h2.deal_id IN (
                    SELECT d3.id
                    FROM deals AS d3
                    LEFT JOIN persons AS p2 ON d3.person_id = p2.id
                    LEFT JOIN coworkers AS co ON d3.coworker_id = co.id
                    WHERE d3.name LIKE '{}%' OR p2.name LIKE '{}%' OR co.name LIKE '{}%'
                )
            )
            GROUP BY p1.name, p1.email'''),
        'top_deal': ('The query being benchmarked here returns all deals above a given probability for the coworker that is responsible for the deal with the highest probability in the system', '''
            SELECT TOP 10000 d.name, d.value, d.probability, co.name
            FROM deals AS d
            LEFT JOIN coworkers AS co ON d.coworker_id = co.id
            WHERE co.id IN (
                SELECT TOP 1 co2.id
                FROM deals as d2
                LEFT JOIN coworkers AS co2 ON d2.coworker_id = co2.id
                ORDER BY d2.probability DESC
            ) AND d.probability > {}
            ORDER BY d.probability DESC;'''),
    },
    'post': {
        'history': ('The query being benchmarked here inserts a row/node of type history', '''
            INSERT INTO histories
            VALUES ({}, 'Call', '2018-03-15', 'Created', {}, {}, {}, {}
            );'''),
        'person': ('The query being benchmarked here inserts a row/node of type person', '''
            INSERT INTO persons
            VALUES ({}, 'Inserted Name', '07012345678', 'CEO', 'insert@insert.com', {}
            );'''),
        'deal': ('The query being benchmarked here inserts a row/node of type deal', '''
            INSERT INTO deals
            VALUES ({}, 'Best Deal Ever', 10, 0.99999, {}, {}
            );'''),
    },
    'put': {
        'companies': ('The query being benchmarked here updates the company name for a given company', '''
            UPDATE companies
            SET companies.name = 'Test'
            WHERE companies.id = {};'''),
        'deals': ('The query being benchmarked here updates the probability of all deals connected to a given company', '''
            UPDATE deals
            SET deals.probability = 0.99
            WHERE deals.person_id IN (
                SELECT p.id
                FROM persons AS p
                WHERE p.company_id = {}
            );'''),
    }
}

queries = {
    'get_top_deal': lambda: get_stats(lambda: run_query(cursor.execute, raw_queries['get']['top_deal'], [random_entry(data, 'deals', 'probability')])),
    'get_histories_type': lambda: get_stats(lambda: run_query(cursor.execute, raw_queries['get']['histories_type'], [random_entry(data, 'histories', 'type')])),
    'get_persons': lambda: get_stats(lambda: run_query(cursor.execute, raw_queries['get']['persons'], [random_entry(data, 'companies', 'id')])),
    'get_filter_histories': lambda: get_stats(lambda: run_query(cursor.execute, raw_queries['get']['filter_histories'], [
        random_entry(data, 'deals', 'id'),
        random_entry(data, 'histories', 'date')
    ])),
    'get_histories': lambda: get_stats(lambda: run_query(cursor.execute, raw_queries['get']['histories'], [
        random_entry(data, 'persons', 'name')[:1],
        random_entry(data, 'persons', 'name')[:1],
        random_entry(data, 'persons', 'name')[:1],
        random_entry(data, 'persons', 'name')[:1],
        random_entry(data, 'documents', 'description')[:1],
        random_entry(data, 'documents', 'description')[:1],
        random_entry(data, 'documents', 'description')[:1],
        random_entry(data, 'documents', 'description')[:1],
    ])),
    'get_filter_coworkers': lambda: get_stats(lambda: run_query(cursor.execute, raw_queries['get']['filter_coworkers'], [
        random_entry(data, 'coworkers', 'name').split()[0],
        random_entry(data, 'companies', 'city')[:2]
    ])),
    'get_deals': lambda: get_stats(lambda: run_query(cursor.execute, raw_queries['get']['deals'],  [
        random_entry(data, 'deals', 'probability'),
        random_entry(data, 'companies', 'name')[:2],
    ])),
    'get_transfer_deals': lambda: get_stats(lambda: run_query(cursor.execute, raw_queries['get']['transfer_deals'],  [
        random_entry(data, 'persons', 'name')[:5],
        random_entry(data, 'persons', 'name')[:5],
        random_entry(data, 'persons', 'name')[:5]
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
    # res = execute(query[1].format(*inputs)).fetchall()
    res = execute(query[1].format(*inputs))
    t2 = time()

    print('|{}'.format(res.rowcount), end='', flush=True)
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
    print("\nMean: {}, Std: {}".format(mean(res), stdev(res)))
    return res


def run(stmt):
    return queries[stmt]()

from statistics import median, mean
from time import time
import pyodbc
import os

from .database import random_entry, load_data

cnxn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER='+os.environ['SQL_SERVER']+';DATABASE=LimeDB;')

cursor = cnxn.cursor()

data = load_data()

queries = {
    'deals': lambda: get_stats(lambda: run_query(cursor.execute, '''
        SELECT p.name, p.position, p.email, p.phone, deals.name, companies.name
        FROM persons AS p
        LEFT JOIN deals ON p.id = deals.person_id
        LEFT JOIN companies ON p.company_id = companies.id
        WHERE deals.probability > {}''',  [random_entry(data, 'deals', 'probability')])),
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
    'persons': lambda: get_stats(lambda: run_query(cursor.execute, '''
        SELECT persons.name, companies.name
        FROM persons
        LEFT JOIN companies ON persons.company_id = companies.id
        WHERE companies.id = {};
    ''', [random_entry(data, 'companies', 'id')])),
    'update_deals': lambda: get_stats(lambda: run_query(cursor.execute, '''
        UPDATE deals
        SET deals.probability = 0.99
        WHERE deals.person_id IN (
            SELECT p.id
            FROM persons as p
            WHERE p.company_id = {}
        );''', [random_entry(data, 'persons', 'company_id')])),
    'update_companies': lambda: get_stats(lambda: run_query(cursor.execute, '''
        UPDATE companies
        SET companies.name = 'Test'
        WHERE companies.id = {}''', [random_entry(data, 'companies', 'id')])),
    'documents': lambda session: get_stats(lambda: run_query(cursor.execute, '''
        SELECT documents.id, persons.id, persons.name, documents.type, documents.description
        FROM documents 
        LEFT JOIN persons ON documents.person_id = persons.id 
        WHERE documents.id IN (
            SELECT documents.id AS id 
            FROM documents 
            LEFT JOIN persons ON documents.person_id = persons.id 
            WHERE  persons.id = {}
        );''', [random_entry(data, 'persons', 'id')]))
}


def run_query(execute, query, inputs=[]):
    t1 = time()
    execute(query.format(*inputs))
    t2 = time()
    return round((t2 - t1) * 1000, 1)


def get_stats(exec, amount=500):
    res = [exec() for i in range(amount)]
    res.remove(min(res))
    res.remove(min(res))
    res.remove(max(res))
    res.remove(max(res))
    return res


def run(stmt):
    return queries[stmt](cursor)

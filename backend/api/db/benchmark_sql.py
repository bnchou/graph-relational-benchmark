from statistics import median
from time import time
import pyodbc
import dotenv
import os

from database import random_entry, load_data

# Remove code under when file is used by django
# ------------- BEGIN REMOVE -------------
dotenv.read_dotenv(os.path.join(
    os.path.dirname(__file__), '..', '..', '..', '.env'))
# ------------- END REMOVE ---------------


def run_query(execute, query, inputs=[]):
    t1 = time()
    execute(query.format(*inputs))
    t2 = time()
    return round((t2 - t1) * 1000, 1)


def get_stats(exec, amount=100):
    print(median([exec() for i in range(amount)]))


if __name__ == "__main__":
    # Specifying the ODBC driver, server name, database, etc. directly
    cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER='+os.environ['SQL_SERVER']+';DATABASE=LimeDB;')

    # Create a cursor from the connection
    cursor = cnxn.cursor()

    data = load_data()

    get_stats(lambda: run_query(cursor.execute, "SELECT * FROM companies;"))

    get_stats(lambda: run_query(cursor.execute, '''
        SELECT p.name, p.position, p.email, p.phone, deals.name, companies.name
        FROM persons AS p
        LEFT JOIN deals ON p.id = deals.person_id
        LEFT JOIN companies ON p.company_id = companies.id
        WHERE deals.probability > {}''',  [random_entry(data, 'deals', 'probability')]))

    get_stats(lambda: run_query(cursor.execute, ''' 
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
        );''', [random_entry(data, 'deals', 'id')]))

    get_stats(lambda: run_query(cursor.execute, '''
        DELETE FROM histories
        WHERE histories.id = {}''', [random_entry(data, 'histories', 'id')]
    ))

    get_stats(lambda: run_query(cursor.execute, '''
        UPDATE deals
        SET deals.probability = 0.99
        WHERE deals.person_id IN (
            SELECT p.id 
            FROM persons as p
            WHERE p.company_id = {}
        );''', [random_entry(data, 'persons', 'company_id')]
    ))

    get_stats(lambda: run_query(cursor.execute, '''
        UPDATE companies
        SET companies.name = 'Test'
        WHERE companies.id = {}''', [random_entry(data, 'companies', 'id')]
    ))

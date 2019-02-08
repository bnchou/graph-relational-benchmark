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

import pyodbc
import os

# Remove code under when file is used by django
# ------------- BEGIN REMOVE -------------
import dotenv
dotenv.read_dotenv(os.path.join(
    os.path.dirname(__file__), '..', '..', '..', '.env'))
# ------------- END REMOVE ---------------


# Specifying the ODBC driver, server name, database, etc. directly
cnxn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER='+os.environ['SQL_SERVER']+';DATABASE=LimeDB;')

# Create a cursor from the connection
cursor = cnxn.cursor()

cursor.execute("SELECT * FROM companies;")

cursor.execute('''
    SELECT p.name, p.position, p.email, p.phone, deals.name, companies.name
    FROM persons AS p
    LEFT JOIN deals ON p.id = deals.person_id
    LEFT JOIN companies ON p.company_id = companies.id
    WHERE deals.probability > ?''', 0.99)

print(cursor.fetchall())

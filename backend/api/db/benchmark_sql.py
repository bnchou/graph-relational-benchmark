import pyodbc

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=BS28M32;DATABASE=LimeDB;')
cursor = cnxn.cursor()

cursor.execute("SELECT * FROM companies;")

cursor.execute('''
    SELECT p.name, p.position, p.email, p.phone, deals.name, companies.name
    FROM persons AS p
    LEFT JOIN deals ON p.id = deals.person_id
    LEFT JOIN companies ON p.company_id = companies.id
    WHERE deals.probability > ?''', 0.99)

print(cursor.fetchall())
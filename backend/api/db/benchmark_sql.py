import pyodbc

# Specifying the ODBC driver, server name, database, etc. directly
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=BS28M32;DATABASE=LimeDB;')

# Create a cursor from the connection
cursor = cnxn.cursor()

cursor.execute("SELECT * FROM companies;")

print(cursor.fetchall())
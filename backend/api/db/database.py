from subprocess import call
import json
from random import randint


def load_data(filepath="backend/api/db/out/output-minimized.json"):
    f = open(filepath, 'r')
    data = json.loads(f.read())
    f.close()
    return data


def reset():
    filename = "backend/api/db/out/output.txt"
    call('reset_cypher.sh', cwd='backend/api/db', shell=True)
    call('reset_sql.sh', cwd='backend/api/db', shell=True)

    f = open(filename)
    data = json.loads(f.read())
    f.close()
    return data


def random_entry(data, table_name, column):
    table = data[table_name]
    random_row = table[randint(0, len(table) - 1)]
    return random_row[column]


def save_amount_to_file(amount):
    f = open('amount.txt', 'w')
    f.write(amount)


def get_amount_from_file():
    f = open('amount.txt', 'r')
    return f.read()

from subprocess import call
import json
from random import randint


def load_data(filepath="out/output.json"):
    f = open(filepath, 'r')
    data = json.loads(f.read())
    f.close()
    return data


def insert(adapter):
    filename = "backend/api/db/out/output.txt"
    call('run_{}.sh'.format(adapter), cwd='backend/api/db', shell=True)

    f = open(filename)
    data = json.loads(f.read())
    f.close()
    return data


def random_entry(data, table_name, column):
    table = data[table_name]
    random_row = table[randint(0, len(table))]
    return random_row[column]

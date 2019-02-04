# MS SQL script command
# > py build_mssql.py | mssql ...

import json
import sys
import re

label = {
    "companies": "Company",
    "persons": "Person",
    "offices": "Office",
    "coworkers": "Coworker",
    "deals": "Deal",
    "documents": "Document",
    "histories": "History"
}

def to_value(value):
    if type(value) == str:
        return '"{}"'.format(value)
    else:
        return str(value)

if __name__ == "__main__":
    filename = "output.json"
    if(len(sys.argv) > 1):
        filename = sys.argv[1]

    f = open(filename)
    data = json.loads(f.read())
    f.close()

    for key in data:
        header, queries, label = [], [], data[key]
        keys = list(label[0].keys())
        p = ', '.join(keys)
        print('INSERT INTO {} ({})'.format(key, p))
        for entry in label:
            values = []
            for k in entry:
                values.append(entry[k])
            value = ','.join(to_value(v) for v in values)
            queries.append('({})'.format(value))
        print('VALUES {};\n'.format(',\n  '.join(queries)))

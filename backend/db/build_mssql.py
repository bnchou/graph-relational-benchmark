# MS SQL script command
# > py build_mssql.py

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

    lines = []

    lines.append('USE LimeDB; \n')

    for key in data:
        header, queries, label = [], [], data[key]
        keys = list(label[0].keys())
        p = ', '.join(keys)
        lines.append('INSERT INTO {} ({})'.format(key, p))
        for entry in label:
            values = []
            for k in entry:
                values.append(entry[k])
            value = ','.join(to_value(v) for v in values)
            queries.append('({})'.format(value))
        lines.append('VALUES {};\n'.format(',\n  '.join(queries)))

    with open('output.sql', 'w') as f_out:
        f_out.write('\n'.join(lines))

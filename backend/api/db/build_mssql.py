# MS SQL script command
# > py build_mssql.py

import json
import sys
import re
import os

label = {
    "companies": "Company",
    "persons": "Person",
    "offices": "Office",
    "coworkers": "Coworker",
    "deals": "Deal",
    "documents": "Document",
    "histories": "History"
}

if __name__ == "__main__":
    f1 = "output.json"
    f2 = "output.sql"
    if(len(sys.argv) > 2):
        [f1, f2] = sys.argv[1:3]

    f = open(f1)
    data = json.loads(f.read())
    f.close()

    lines = []

    lines.append('''\
        USE LimeDB;
        -- DECLARE @path varchar(50);
        -- SET @path = '';''')

    for key in data:
        header, queries, label = [], [], data[key]
        keys = list(label[0].keys())
        p = ', '.join(keys)
        lines.append('''
            BULK INSERT {}
            FROM '{}\\out\\temp\{}.csv'
            WITH
            (
                FIRSTROW = 2,
                FIELDTERMINATOR = '~',
                ROWTERMINATOR ='\\n'
            );
        '''.format(key, os.getcwd(), key))
        queries.append('~'.join(keys))
        for entry in label:
            values = []
            for k in entry:
                values.append(entry[k])
            value = '~'.join(str(v) for v in values)
            queries.append(value)

        with open('out/temp/{}.csv'.format(key), 'w') as f_out:
            f_out.write('\n'.join(queries))

    with open(f2, 'w') as f_out:
        f_out.write('\n'.join(lines))

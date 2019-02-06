# MS SQL build script command
# > py build_mssql.py [INPUT_FILE] [OUTPUT_FILE]

import json
import sys
import os

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

    with open(f2, 'w') as f_out:
        f_out.write('\n'.join(lines))

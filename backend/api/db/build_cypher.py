# Cypher-shell build script command
# > py build_cypher.py [INPUT_FILE] [OUTPUT_FILE] | cypher-shell -u neo4j -p password --format verbose

import json
import sys
import os

label = {
    "companies": "Company",
    "persons": "Person",
    "offices": "Office",
    "coworkers": "Coworker",
    "deals": "Deal",
    "documents": "Document",
    "histories": "History",
    "relationships": "Relationship"
}


def get_row(attribute):
    if attribute == "id" or attribute.endswith("_id") or attribute == "value":
        return "toInteger(row.{})".format(str(attribute))
    elif attribute == "probability":
        return "toFloat(row.{})".format(str(attribute))
    else:
        return "row.{}".format(attribute)


if __name__ == "__main__":
    f1 = "output.json"
    f2 = "output.cypher"
    if(len(sys.argv) > 2):
        [f1, f2] = sys.argv[1:3]

    f = open(f1)
    data = json.loads(f.read())
    f.close()

    lines = []

    lines.append('MATCH ()-[r]-() DELETE r;')
    lines.append('MATCH (n) DELETE n;')

    for key in data:
        keys = ',\n'.join(
            map(lambda x: '{}: {}'.format(x, get_row(x)), data[key][0].keys()))

        lines.append('''
            USING PERIODIC COMMIT
            LOAD CSV WITH HEADERS FROM "file:///{}/out/temp/{}.csv" AS row
            FIELDTERMINATOR '~'
            CREATE (:{} {{
                {}
            }});

            CREATE INDEX ON :{}(id);
        '''.format(os.getcwd().replace('\\', '/'), key, label[key], keys, label[key]))

    with open(f2, 'w') as f_out:
        f_out.write('\n'.join(lines))

# Cypher-shell script command
# > py .\to_cypher.py | cypher-shell -u neo4j -p password --format verbose

import json
import sys
import re

label = {
    "companies": "Company",
    "persons": "Person",
    "offices": "Office",
    "coworkers": "Coworker",
    "deals": "Deal"
}

if __name__ == "__main__":
    filename = "output.json"
    if(len(sys.argv) > 1):
        filename = sys.argv[1]

    f = open(filename)
    data = json.loads(f.read())
    f.close()

    print('MATCH ()-[r]-() DELETE r;')
    print('MATCH (n) DELETE n;')

    queries = []

    for key in data:
        for node in data[key]:
            props = re.sub(r'(?<!: )"(\S*?)"', '\\1', json.dumps(node))
            queries.append('(:{} {})'.format(label[key], props))

    print('CREATE {};'.format(','.join(queries)))
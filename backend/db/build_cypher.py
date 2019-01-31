# Cypher-shell script command
# > py build_cypher.py | cypher-shell -u neo4j -p password --format verbose

import json
import sys
import re

label = {
    "companies": "Company",
    "persons": "Person",
    "offices": "Office",
    "coworkers": "Coworker",
    "deals": "Deal",
    "documents": "Document"
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

    print('''
        MATCH (person:Person), (company:Company)
        WHERE person.company_id = company.id
        CREATE (person)-[:WORKS_AT]->(company);

        MATCH (coworker:Coworker), (office:Office)
        WHERE coworker.office_id = office.id
        CREATE (coworker)-[:WORKS_AT]->(office);

        MATCH (deal:Deal), (person:Person)
        WHERE deal.person_id = person.id
        CREATE (deal)<-[:RESPONSIBLE_FOR]-(person);

        MATCH (deal:Deal), (coworker:Coworker)
        WHERE deal.coworker_id = coworker.id
        CREATE (deal)<-[:SALESPERSON_FOR]-(coworker);

        MATCH (document:Document), (person:Person)
        WHERE document.person_id = person.id
        CREATE (document)<-[:OWNS]-(person);

        MATCH (document:Document), (deal:Deal)
        WHERE document.deal_id = deal.id
        CREATE (document)-[:ATTACHED_TO]->(deal);
    ''')
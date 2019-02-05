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
    "documents": "Document",
    "histories": "History"
}

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

    queries = []

    for key in data:
        for node in data[key]:
            props = re.sub(r'(?<!: )"(\S*?)"', '\\1', json.dumps(node))
            queries.append('(:{} {})'.format(label[key], props))

    lines.append('CREATE {};'.format(','.join(queries)))

    lines.append('''
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

        MATCH (history:History), (person:Person)
        WHERE history.person_id = person.id
        CREATE (history)<-[:ATTENDED]-(person);

        MATCH (history:History), (coworker:Coworker)
        WHERE history.coworker_id = coworker.id
        CREATE (history)<-[:ATTENDED]-(coworker);

        MATCH (history:History), (document:Document)
        WHERE history.document_id = document.id
        CREATE (history)<-[:ATTACHED_TO]-(document);

        MATCH (history:History), (deal:Deal)
        WHERE history.deal_id = deal.id
        CREATE (history)<-[:PART_OF]-(deal);
    ''')

    with open(f2, 'w') as f_out:
        f_out.write('\n'.join(lines))
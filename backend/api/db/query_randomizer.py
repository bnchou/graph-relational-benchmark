import json
import sys
import random

def rand_entry(table, column, data):
   table_entries = data[table]
   rand_row = table_entries[random.randint(0, len(table_entries))]
   rand_data_entry = rand_row[column]
   
   return rand_data_entry

if __name__ == "__main__":
    f1 = "output.json"
    f2 = "output.sql"

    if(len(sys.argv) > 2):
        [f1, f2] = sys.argv[1:3]

    f = open(f1)
    data = json.loads(f.read())
    f.close()

    
    lines = []

    deal_id = rand_entry('deals', 'id', data)

    lines.append('''
SELECT histories.id, histories.date, coworkers.id, coworkers.name, histories.type, persons.id, persons.name , documents.id, documents.description, histories.notes
FROM histories
LEFT JOIN deals ON histories.deal_id = deals.id 
LEFT JOIN coworkers ON histories.coworker_id = coworkers.id 
LEFT JOIN persons ON histories.person_id = persons.id 
LEFT JOIN documents ON histories.document_id = documents.id 
WHERE (histories.id IN (
    SELECT histories.id AS id 
    FROM histories 
    LEFT JOIN deals ON histories.deal_id = deals.id 
    WHERE  (deals.id = {})
    ) AND deals.id = {})'''.format(deal_id, deal_id))

    with open(f2, 'w') as f_out:
        f_out.write('\n'.join(lines))


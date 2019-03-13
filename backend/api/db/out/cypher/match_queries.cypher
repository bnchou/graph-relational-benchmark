MATCH (p: Person)-[:WORKS_AT]->(c: Company)
WHERE c.id = 100
RETURN p.name, c.name;

MATCH (p: Person)-[:RESPONSIBLE_FOR]->(d: Deal),
      (p)-[:WORKS_AT]->(c: Company)
WHERE d.probability > 0.9
RETURN p.name, p.email, p.phone, d.name, c.name;

MATCH (d: Deal)<-[:PART_OF]-(h: History),
    (h)<-[:ATTACHED_TO]-(doc:Document),
    (c: Coworker)-[:ATTENDED]->(h)<-[:ATTENDED]-(p: Person)
WHERE d.id = 1
RETURN h.id, h.type, h.date, c.name, p.name, doc.description;

 MATCH (p: Person)-[:OWNS]->(doc: Document),
    (doc)-[:ATTACHED_TO]->(d: Deal)
WHERE p.id = 100
RETURN doc.id, doc.description, doc.type, d.name;

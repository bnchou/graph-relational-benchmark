MATCH (c: Company)
RETURN c;

MATCH (p: Person)-[:WORKS_AT]->(c: Company)
RETURN p.name, c.name;

MATCH (p: Person)-[:RESPONSIBLE_FOR]->(d: Deal),
      (p)-[:WORKS_AT]->(c: Company)
WHERE d.probability > 0.9
RETURN p.name, p.position, p.email, p.phone, d.name, c.name;

MATCH (deal: Deal)-[:PART_OF]->(h: History),
    (h)<-[:ATTACHED_TO]-(d:Document),
    (c: Coworker)-[:ATTENDED]->(h)<-[:ATTENDED]-(p: Person)
WHERE deal.id = 1
RETURN h.id, h.type, h.date, c.name, p.name, d.description;

MATCH (p: Person)-[:OWNS]->(d: Document)
WHERE p.id = 1
RETURN d.id, p.id, p.name, d.type, d.description;

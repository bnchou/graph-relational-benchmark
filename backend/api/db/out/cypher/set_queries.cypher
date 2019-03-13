MATCH (c: Company {name: 'Reed & Burton Ltd'})
SET c.name = 'Test'
RETURN c.name;

MATCH (d: Deal)<-[:RESPONSIBLE_FOR]-(p: Person),
(p)-[:WORKS_AT]->(c: Company)
WHERE c.id = 9
SET d.probability = 0.99
RETURN d;
MATCH (c: Company {name: 'Reed & Burton Ltd'})
SET c.name = 'Test'
RETURN c.name;

MATCH (d: Deal)<-[:RESPONSIBLE_FOR]-(p:Person)
WHERE p.company_id = 0
SET d.probability = 0.99
RETURN d;
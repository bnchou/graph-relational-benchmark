MATCH (c: Company)
RETURN c;

MATCH (p: Person)-[:WORKS_AT]->(c:Company)
RETURN p.name, c.name;


// Filter to show all persons and corresponding companies that have deals with probability > 0.9
// ''Depth'' = 2

PROFILE
MATCH (p:Person)-[:RESPONSIBLE_FOR]->(d: Deal)
MATCH (p)-[WORKS_AT]->(c: Company)
WHERE d.probability > 0.9
RETURN p.name, p.position, p.email, p.phone, d.name, c.name;


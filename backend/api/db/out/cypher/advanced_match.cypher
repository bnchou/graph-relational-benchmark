MATCH (c: Company)<-[:WORKS_AT]-(p: Person),
(p)-[:RESPONSIBLE_FOR]->(d: Deal),
(d)<-[:SALESPERSON_FOR]-(co: Coworker)
WHERE co.name =~ 'Anna.*' AND c.city =~ 'Troll.*'
RETURN co.name, c.city;
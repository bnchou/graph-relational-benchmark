MATCH (c: Company)<-[:WORKS_AT]-(p: Person),
(p)-[:RESPONSIBLE_FOR]->(d: Deal),
(d)<-[:SALESPERSON_FOR]-(co: Coworker)
WHERE co.name =~ 'Anna.*' AND c.city =~ 'Troy.*'
RETURN co.name, c.city;

MATCH (d: Deal)-[:PART_OF]->(h:History)
WHERE d.value > 100000 AND h.type = 'Call'
AND h.date >= apoc.date.format(apoc.date.add(apoc.date.currentTimestamp(), 'ms', -183, 'd'), 'ms', 'yyyy-MM-dd')
RETURN d.name;
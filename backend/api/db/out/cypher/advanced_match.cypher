MATCH (c: Company)<-[:WORKS_AT]-(p: Person),
(p)-[:RESPONSIBLE_FOR]->(d: Deal),
(d)<-[:SALESPERSON_FOR]-(co: Coworker)
WHERE co.name =~ 'Anna.*' AND c.city =~ 'Troy.*'
RETURN co.name, c.city;

MATCH (d: Deal)<-[:PART_OF]-(h:History)
WHERE d.value > 10000 AND h.type = 'Call'
AND h.date < '2018-01-05'
RETURN d.name, h.date;

MATCH (doc: Document)<-[:OWNS]-(p:Person),
(doc)-[:ATTACHED_TO]->(d: Deal)
WHERE d.probability > 0.9 AND p.name =~ 'Anna.*' AND doc.type = 'pdf'
RETURN count(*);
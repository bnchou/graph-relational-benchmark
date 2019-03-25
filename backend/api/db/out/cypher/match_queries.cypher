MATCH (d: Deal)<-[:PART_OF]-(h: History),
(h)<-[:ATTENDED]-(co: Coworker),
(h)<-[:ATTENDED]-(p: Person),
(p)-[:WORKS_AT]->(c: Company)
WHERE h.type = 'Call'
RETURN h.date, co.name, h.type, p.name, c.name, d.name
LIMIT 10000;

MATCH (p: Person)-[:WORKS_AT]->(c: Company)
WHERE c.id = 1
RETURN p.name, p.email, c.name
LIMIT 10000;

MATCH (d: Deal)<-[:PART_OF]-(h: History),
(h)<-[:ATTACHED_TO]-(doc: Document),
(h)<-[:ATTENDED]-(c: Coworker),
(h)<-[:ATTENDED]-(p: Person)
WHERE d.id = 1 AND h.type = 'Call'
AND h.date < '2019-03-13'
RETURN h.date, c.name, h.type, p.name, doc.description
LIMIT 10000;

MATCH (d: Deal)<-[:PART_OF]-(h: History),
(h)<-[:ATTACHED_TO]-(doc: Document),
(h)<-[:ATTENDED]-(c: Coworker),
(h)<-[:ATTENDED]-(p: Person)
WHERE (h.type =~ 'Per.*' OR c.name =~ 'Per.*' OR p.name =~ 'Per.*' OR doc.description =~ 'Per.*')
AND (h.type =~ 'Co.*' OR c.name =~ 'Co.*' OR p.name =~ 'Co.*' OR doc.description =~ 'Co.*')
RETURN h.type, h.date, c.name, p.name, doc.description
LIMIT 10000;

MATCH (c: Company)<-[:WORKS_AT]-(p: Person),
(d: Deal)<-[:RESPONSIBLE_FOR]-(p),
(d)<-[:SALESPERSON_FOR]-(co: Coworker)
WHERE co.name =~ 'Anna.*' AND c.city =~ 'Bos.*'
RETURN co.name, c.name, c.city
LIMIT 10000;

MATCH (p: Person)-[:RESPONSIBLE_FOR]->(d: Deal),
(p)-[:WORKS_AT]->(c: Company)
WHERE d.probability > 0.5 AND c.name =~ 'And.*'
RETURN p.name, p.email, p.phone, d.name, c.name
LIMIT 10000;

MATCH (co: Coworker)-[:SALESPERSON_FOR]->(d: Deal),
(d)<-[:RESPONSIBLE_FOR]-(p1: Person)
WITH d.id as d_id
WHERE d.name =~ 'Rob.*' OR p1.name =~ 'Rob.*' OR co.name =~ 'Rob.*'
MATCH (h: History)-[:PART_OF]->(deal: Deal {{id: d_id}}),
(h)<-[:ATTENDED]-(p2: Person)
RETURN COLLECT(DISTINCT p2.name), p2.email
LIMIT 10000;

MATCH (d: Deal)<-[:SALESPERSON_FOR]-(co: Coworker)
WITH co.id as id, d.probability as prob
ORDER BY d.probability DESC LIMIT 1
MATCH (c: Coworker {{id: id}})-[:SALESPERSON_FOR]->(deal: Deal)
WHERE deal.probability > 0.5
RETURN deal.name, deal.value, deal.probability, c.name
LIMIT 10000;
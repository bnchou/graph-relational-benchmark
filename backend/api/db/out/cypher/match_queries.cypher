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

MATCH (d: Deal)<-[:SALESPERSON_FOR]-(co: Coworker)
WITH co.id as id, d.probability as prob
ORDER BY d.probability DESC LIMIT 1
MATCH (c: Coworker {id: id})-[:SALESPERSON_FOR]->(deal: Deal)
RETURN deal.name, deal.value, deal.probability;

MATCH (co: Coworker)-[:SALESPERSON_FOR]->(d: Deal)<-[:RESPONSIBLE_FOR]-(p1: Person)
WITH d.id as d_id
WHERE d.name =~ 'Ab.*' OR p1.name =~ 'Ab.*' OR co.name =~ 'Ab.*'
MATCH (h1: History)-[:PART_OF]->(deal: Deal {id: d_id}),
(h1)<-[:ATTENDED]-(p2: Person)
RETURN COLLECT(DISTINCT p2.name), p2.email;

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



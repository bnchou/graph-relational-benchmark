CREATE (h: History {
    id: 100000000,
    type: 'Call',
    notes: 'Test',
    date: '2018-02-13'
})

MATCH (h:History),(doc:Document),
(d: Deal), (p: Person), (c: Coworker)
WHERE h.id = 100000000 AND doc.id = 100 
AND d.id = 100 AND p.id = 100 AND c.id = 100
CREATE (h)<-[:ATTACHED_TO]-(doc)
CREATE (h)<-[:PART_OF]-(d)
CREATE (h)<-[:ATTENDED]-(p) 
CREATE (h)<-[:ATTENDED]-(c);

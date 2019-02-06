MATCH (c: Company)
RETURN COUNT(c);

MATCH (p: Person)-[:WORKS_AT]->(c:Company)
RETURN COUNT(p.name), COUNT(c.name);


// Filter to show all persons and corresponding companies that have deals with probability > 0.9
// ''Depth'' = 2

// PROFILE
MATCH (p:Person)-[:RESPONSIBLE_FOR]->(d: Deal)
MATCH (p)-[WORKS_AT]->(c: Company)
WHERE d.probability > 0.9
RETURN COUNT(p.name), COUNT(p.position), COUNT(p.email), COUNT(p.phone), COUNT(d.name), COUNT(c.name);

// Fetch history on deal id: 1

MATCH (deal:Deal {id: 1})-[:PART_OF]->(history:History)<-[:ATTACHED_TO]-(document:Document)
MATCH (coworker:Coworker)-[:ATTENDED]->(history)<-[:ATTENDED]-(person:Person)
RETURN COUNT(history.id), COUNT(history.type), COUNT(history.date), COUNT(coworker.name), COUNT(person.name), COUNT(document.description);
// ORDER BY history.date DESC;

// Fetch documents on person id: 1

MATCH (person:Person {id: 1})-[:OWNS]->(document:Document)-[:ATTACHED_TO]->(deal:Deal)
RETURN COUNT(document.id), COUNT(document.description), COUNT(document.type), COUNT(deal.name);

// Fun

// MATCH (company:Company)<-[:WORKS_AT]-(:Person)-[:RESPONSIBLE_FOR]->(deal:Deal)-[:PART_OF]->(history:History)<-[:PART_OF]-(document:Document)
// WHERE deal.probability > 0.5
// RETURN DISTINCT company.name,deal.name,deal.value,deal.probability,history.date,document.description,company.country
// ORDER BY history.date DESC;


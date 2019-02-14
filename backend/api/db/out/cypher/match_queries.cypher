MATCH (c: Company)
RETURN c;

MATCH (p: Person)-[:WORKS_AT]->(c:Company)
RETURN p.name, c.name;


// Filter to show all persons and corresponding companies that have deals with probability > 0.9
// ''Depth'' = 2

// PROFILE
MATCH (p:Person)-[:RESPONSIBLE_FOR]->(d: Deal)
MATCH (p)-[WORKS_AT]->(c: Company)
WHERE d.probability > 0.9
RETURN p.name, p.position, p.email, p.phone, d.name, c.name;

// Fetch history on deal id: 1

MATCH (d:Deal)-[:PART_OF]->(h:History),
    (h)<-[:ATTACHED_TO]-(doc:Document),
    (c:Coworker)-[:ATTENDED]->(h)<-[:ATTENDED]-(p:Person)
WHERE h.id = 1
RETURN h.id, h.type, h.date, c.name, p.name, doc.description;

// Fetch documents on person id: 1

MATCH (person:Person {id: 1})-[:OWNS]->(document:Document),
    (document)-[:ATTACHED_TO]->(deal:Deal)
RETURN document.id, document.description, document.type, deal.name;

// Fun

// MATCH (company:Company)<-[:WORKS_AT]-(:Person)-[:RESPONSIBLE_FOR]->(deal:Deal)-[:PART_OF]->(history:History)<-[:PART_OF]-(document:Document)
// WHERE deal.probability > 0.5
// RETURN DISTINCT company.name,deal.name,deal.value,deal.probability,history.date,document.description,company.y
// ORDER BY history.date DESC;


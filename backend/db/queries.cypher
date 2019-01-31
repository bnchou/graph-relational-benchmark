// Fetch history on deal id: 1

MATCH (deal:Deal {id: 1})-[:PART_OF]->(history:History)<-[:ATTACHED_TO]-(document:Document)
MATCH (coworker:Coworker)-[:ATTENDED]->(history)<-[:ATTENDED]-(person:Person)
RETURN history.id, history.type, history.date, coworker.name, person.name, document.description
ORDER BY history.date DESC

// Fetch documents on person id: 1

MATCH (person:Person {id: 1})-[:OWNS]->(document:Document)-[:ATTACHED_TO]->(deal:Deal)
RETURN document.id, document.description, document.type, deal.name

// Fun

MATCH (company:Company)<-[:WORKS_AT]-(:Person)-[:RESPONSIBLE_FOR]->(deal:Deal)-[:PART_OF]->(history:History)<-[:PART_OF]-(document:Document)
WHERE deal.probability > 0.5
RETURN DISTINCT company.name,deal.name,deal.value,deal.probability,history.date,document.description,company.country
ORDER BY history.date DESC
MERGE (h: History {id: 99999999, type: 'Call', notes: 'Created', date: '2018-03-15'})
MERGE (doc: Document {id: 100})
MERGE (d: Deal {id:100})
MERGE (p: Person {id: 100})
MERGE (c: Coworker {id: 100})
MERGE (h)<-[:ATTACHED_TO]-(doc)
MERGE (h)<-[:PART_OF]-(d)
MERGE (h)<-[:ATTENDED]-(p) 
MERGE (h)<-[:ATTENDED]-(c);

MERGE (p: Person {id: 999999, name: 'Inserted Name', phone: '07012345678', position: 'CEO', email: 'insert@insert.com'})
MERGE (c: Company {id: 100})
MERGE (p)-[:WORKS_AT]->(c);

MERGE (d: Deal {id: 99999, name: 'Best Deal Ever', value: 10, probability: 0.99999})
MERGE (p: Person {id: 100})
MERGE (c: Coworker {id: 100})
MERGE (p)-[:RESPONSIBLE_FOR]->(d)<-[:SALESPERSON_FOR]-(c);


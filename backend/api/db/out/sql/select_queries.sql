SELECT c.id FROM companies AS c;

SELECT p.name, c.name
FROM persons AS p
LEFT JOIN companies AS c
ON p.company_id = c.id
WHERE c.id = 1;

SELECT p.name, p.position, p.email, p.phone, d.name, c.name
FROM persons AS p
LEFT JOIN deals AS d ON p.id = d.person_id
LEFT JOIN companies AS c ON p.company_id = c.id
WHERE d.probability > 0.9;

SELECT h.id, h.type, h.date, c.name, p.name, d.description
FROM histories AS h
LEFT JOIN deals ON h.deal_id = deals.id 
LEFT JOIN coworkers AS c ON h.coworker_id = c.id 
LEFT JOIN persons AS p ON h.person_id = p.id 
LEFT JOIN documents AS d ON h.document_id = d.id 
WHERE deals.id = 1;

SELECT d.id, p.id, p.name, d.type, d.description
FROM documents AS d
LEFT JOIN persons AS p 
ON d.person_id = p.id
WHERE persons.id = 1;

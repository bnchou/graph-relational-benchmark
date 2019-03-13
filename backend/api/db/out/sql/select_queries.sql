SELECT p.name, c.name
FROM persons AS p
LEFT JOIN companies AS c ON p.company_id = c.id
WHERE c.id = 1;

SELECT p.name, p.email, p.phone, d.name, c.name
FROM persons AS p
LEFT JOIN deals AS d ON p.id = d.person_id
LEFT JOIN companies AS c ON p.company_id = c.id
WHERE d.probability > 0.9;

SELECT h.type, h.date, c.name, p.name, doc.description
FROM histories AS h
LEFT JOIN deals AS d ON h.deal_id = d.id 
LEFT JOIN coworkers AS c ON h.coworker_id = c.id 
LEFT JOIN persons AS p ON h.person_id = p.id 
LEFT JOIN documents AS doc ON h.document_id = doc.id 
WHERE d.id = 1;

SELECT doc.id, doc.description, doc.type, d.name
FROM documents AS doc
LEFT JOIN persons AS p ON doc.person_id = p.id
LEFT JOIN deals AS d ON doc.deal_id = d.id
WHERE p.id = 1;
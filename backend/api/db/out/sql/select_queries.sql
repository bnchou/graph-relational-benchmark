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

SELECT d.name, d.value, d.probability, co.name
FROM deals AS d
LEFT JOIN coworkers AS co ON d.coworker_id = co.id
WHERE co.id IN (
    SELECT TOP 1 co2.id
    FROM deals as d2
    LEFT JOIN coworkers AS co2 ON d2.coworker_id = co2.id
    ORDER BY d2.probability DESC
) AND d.probability > 0.8
ORDER BY d.probability DESC;

SELECT p1.name, p1.email
FROM persons AS p1
LEFT JOIN histories AS h1 ON h1.person_id = p1.id
WHERE h1.id IN (
    SELECT h2.id
    FROM histories AS h2
    WHERE h2.deal_id IN (
        SELECT d3.id
        FROM deals AS d3
        LEFT JOIN persons AS p2 ON d3.person_id = p2.id
        LEFT JOIN coworkers AS co ON d3.coworker_id = co.id
        WHERE d3.name LIKE 'Ro%' OR p2.name LIKE 'Ro%' OR co.name LIKE 'Ro%'
    )
)
GROUP BY p1.name, p1.email
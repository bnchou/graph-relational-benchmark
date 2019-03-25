SELECT TOP 10000 h.date, co.name, h.type, p.name, c.name, d.name
FROM histories AS h
LEFT JOIN deals AS d ON h.deal_id = d.id 
LEFT JOIN coworkers AS co ON h.coworker_id = co.id 
LEFT JOIN persons AS p ON h.person_id = p.id 
LEFT JOIN companies AS c ON p.company_id = c.id
WHERE h.type = 'Call';

SELECT TOP 10000 p.name, p.email, c.name
FROM persons AS p
LEFT JOIN companies AS c ON p.company_id = c.id
WHERE c.id = 1;

SELECT TOP 10000 h.date, c.name, h.type, p.name, doc.description
FROM deals AS d
LEFT JOIN histories AS h ON h.deal_id = d.id
LEFT JOIN documents AS doc on h.document_id = doc.id
LEFT JOIN persons AS p ON h.person_id = p.id
LEFT JOIN coworkers AS c ON h.coworker_id = c.id
WHERE d.id = 1 AND h.type = 'Call'
AND h.date < '2019-03-13';

SELECT TOP 10000 h.type, h.date, c.name, p.name, doc.description
FROM histories AS h
LEFT JOIN deals AS d ON h.deal_id = d.id 
LEFT JOIN coworkers AS c ON h.coworker_id = c.id 
LEFT JOIN persons AS p ON h.person_id = p.id 
LEFT JOIN documents AS doc ON h.document_id = doc.id 
WHERE (h.type LIKE 'Per%' OR c.name LIKE 'Per%' OR p.name LIKE 'Per%' OR doc.description LIKE 'Per%')
AND (h.type LIKE 'Co%' OR c.name LIKE 'Co%' OR p.name LIKE 'Co%' OR doc.description LIKE 'Co%');

SELECT TOP 10000 co.name, c.name, c.city
FROM companies as c
LEFT JOIN persons as p ON p.company_id = c.id
LEFT JOIN deals as d ON d.person_id = p.id
LEFT JOIN coworkers as co ON d.coworker_id = co.id
WHERE co.name LIKE 'Rob%' AND c.city LIKE 'Bos%';

SELECT TOP 10000 p.name, p.email, p.phone, d.name, c.name
FROM persons AS p
LEFT JOIN deals AS d ON p.id = d.person_id
LEFT JOIN companies AS c ON p.company_id = c.id
WHERE d.probability > 0.5 AND c.name LIKE 'And%';

SELECT TOP 10000 p1.name, p1.email
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
        WHERE d3.name LIKE 'Rob%' OR p2.name LIKE 'Rob%' OR co.name LIKE 'Rob%'
    )
)
GROUP BY p1.name, p1.email;

SELECT TOP 10000 d.name, d.value, d.probability, co.name
FROM deals AS d
LEFT JOIN coworkers AS co ON d.coworker_id = co.id
WHERE co.id IN (
    SELECT TOP 1 co2.id
    FROM deals as d2
    LEFT JOIN coworkers AS co2 ON d2.coworker_id = co2.id
    ORDER BY d2.probability DESC
) AND d.probability > 0.5
ORDER BY d.probability DESC;
SELECT c.name, co.name
FROM companies AS c
LEFT JOIN persons AS p ON p.company_id = c.id
LEFT JOIN deals AS d ON d.person_id = p.id
LEFT JOIN coworkers AS co ON co.id = d.coworker_id
WHERE co.name LIKE 'D%' AND c.city LIKE 'T%';

SELECT d.name, h.date
FROM deals AS d
LEFT JOIN histories AS h ON h.deal_id = d.id
WHERE d.value > 100000 AND h.type = 'Call'
AND h.date < '2018-01-05';

SELECT COUNT(*)
FROM documents as doc
LEFT JOIN persons as p ON doc.person_id = p.id
LEFT JOIN deals as d ON d.id = doc.deal_id
WHERE d.probability > 0.9 AND p.name LIKE 'Anna*'
AND doc.type = 'pdf';

SELECT c.name, p.name
FROM companies AS c
LEFT JOIN persons AS p
ON p.company_id = c.id
LEFT JOIN deals AS d
ON deals.person_id = p.id
LEFT JOIN coworkers AS co
ON co.id = d.coworker_id
WHERE co.name LIKE 'Anna*' AND c.city LIKE 'Troll*';

SELECT COUNT(*) AS NumCallsHalfYear
FROM deals AS d
LEFT JOIN histories AS h
ON h.deal_id = d.id
WHERE d.value > 100000 AND h.type = 'Call'
AND h.date BETWEEN GETDATE() AND DATEADD(mm, -6, GETDATE())



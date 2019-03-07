SELECT c.name, p.name
FROM companies as c
LEFT JOIN persons as p
ON p.company_id = c.id
LEFT JOIN deals as d
ON deals.person_id = p.id
LEFT JOIN coworkers as co
ON co.id = d.coworker_id
WHERE co.name LIKE 'Anna*' AND c.city LIKE 'Troll*';


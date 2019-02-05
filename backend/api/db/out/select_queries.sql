Use LimeDB;


SELECT * FROM companies;

-- Displays all p in the system and their respective companies

SELECT p.name, companies.name
FROM persons AS p
LEFT JOIN companies ON p.company_id = companies.id;


-- Filter to show all persons and corresponding companies that have deals with probability > 0.9
-- ''Depth'' = 2

SELECT p.name, p.position, p.email, p.phone, deals.name, companies.name
FROM persons AS p
LEFT JOIN deals ON p.id = deals.person_id
LEFT JOIN companies ON p.company_id = companies.id
WHERE deals.probability > 0.9
Use LimeDB;
SET STATISTICS TIME ON;

SELECT COUNT(companies.id) FROM companies;

-- -- Displays all p in the system and their respective companies

SELECT COUNT(p.name), COUNT(companies.name)
FROM persons AS p
LEFT JOIN companies ON p.company_id = companies.id;


-- -- Filter to show all persons and corresponding companies that have deals with probability > 0.9
-- -- ''Depth'' = 2

SELECT COUNT(p.name), COUNT(p.position), COUNT(p.email), COUNT(p.phone), COUNT(deals.name), COUNT(companies.name)
FROM persons AS p
LEFT JOIN deals ON p.id = deals.person_id
LEFT JOIN companies ON p.company_id = companies.id
WHERE deals.probability > 0.9

-- Fetch histories on deal id: 1

SELECT COUNT(histories.id), COUNT(histories.date), COUNT(coworkers.id), COUNT(coworkers.name), COUNT(histories.type), COUNT(persons.id), COUNT(persons.name), COUNT(documents.id)--, COUNT(documents.description), COUNT(histories.notes)
FROM histories
LEFT JOIN deals ON histories.deal_id = deals.id 
LEFT JOIN coworkers ON histories.coworker_id = coworkers.id 
LEFT JOIN persons ON histories.person_id = persons.id 
LEFT JOIN documents ON histories.document_id = documents.id 
WHERE (histories.id IN (
    SELECT histories.id AS id 
    FROM histories 
    LEFT JOIN deals ON histories.deal_id = deals.id 
    WHERE  (deals.id = 1)
    ) AND deals.id = 1
);

-- Fetch documents on person id: 1

SELECT COUNT(documents.id), COUNT(persons.id), COUNT(persons.name), COUNT(documents.type)--, COUNT(documents.description)
FROM documents 
LEFT JOIN persons ON documents.person_id = persons.id 
WHERE ( (documents.id IN (SELECT documents.id AS id 
    FROM documents 
    LEFT JOIN persons ON documents.person_id = persons.id 
    WHERE  (persons.id = 1)) AND persons.id = 1)
)


SET STATISTICS TIME OFF;
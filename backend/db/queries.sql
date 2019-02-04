-- Fetch histories on deal id: 1

SELECT histories.id, histories.date, coworkers.id, coworkers.name, histories.type, persons.id, persons.name , documents.id, documents.description, histories.notes
FROM histories
LEFT JOIN deals ON histories.deal_id = deals.id 
LEFT JOIN coworkers ON histories.coworker_id = coworkers.id 
LEFT JOIN persons ON histories.person_id = persons.id 
LEFT JOIN documents ON histories.document_id = documents.id 
-- LEFT JOIN file ON document.document = file.id 
WHERE (histories.id IN (
    SELECT histories.id AS id 
    FROM histories 
    LEFT JOIN deals ON histories.deal_id = deals.id 
    WHERE  (deals.id = 1)
    ) AND deals.id = 1
)


-- Fetch documents on person id: 1

SELECT documents.id, documents.description, persons.id, persons.name, documents.type
FROM documents 
LEFT JOIN persons ON documents.person_id = persons.id 
-- LEFT JOIN coworkers ON documents.coworker_id = coworkers.id
-- LEFT JOIN file ON document.document = file.id 
WHERE ( (documents.id IN (SELECT documents.id AS id 
    FROM documents 
    LEFT JOIN persons ON documents.person_id = persons.id 
 --    LEFT JOIN file ON document.document = file.id 
    WHERE  (persons.id = 1)) AND persons.id = 1)
)
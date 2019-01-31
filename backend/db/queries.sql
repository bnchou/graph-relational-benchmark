-- Fetch history on deal id: 1005

SELECT history.id, history.date, coworker.id, coworker.name, history.type, person.idperson, (person.firstname + ' ' + person.lastname), document.id, document.comment, history.note
FROM history
LEFT JOIN deal ON history.deal = deal.id 
LEFT JOIN coworker ON history.coworker = coworker.id 
LEFT JOIN person ON history.person = person.idperson 
LEFT JOIN document ON history.document = document.id 
LEFT JOIN file ON document.document = file.id 
WHERE (history.id IN (
    SELECT history.id AS id 
    FROM history 
    LEFT JOIN deal ON history.deal = deal.id 
    WHERE  (deal.id = 1005)
    ) AND deal.id = 1005
)


-- Fetch documents on person id: 1027

SELECT document.id, document.createdtime, document.comment, coworker.idcoworker, coworker.name, document.type, document.document
FROM document 
LEFT JOIN person ON document.person = person.id 
LEFT JOIN coworker ON document.coworker = coworker.idcoworker 
LEFT JOIN file ON document.document = file.id 
WHERE ( (document.id IN (SELECT document.id AS id 
    FROM document 
    LEFT JOIN person ON document.person = person.id 
    LEFT JOIN file ON document.document = file.id 
    WHERE  (person.id = 1027)) AND person.id = 1027)
)
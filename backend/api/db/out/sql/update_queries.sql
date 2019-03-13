UPDATE companies
SET companies.name = 'Test'
WHERE companies.name = 'Reed & Burton Ltd'

UPDATE deals
SET deals.probability = 0.99
WHERE deals.person_id IN (
    SELECT p.id 
    FROM persons AS p
    WHERE p.company_id = 0
)
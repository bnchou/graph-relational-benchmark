USE LimeDB;

-- -- Run with > sqlcmd -i create_schema.sql

-- SWITCH ALL VARCHARS TO NVARCHAR FOR UNICODE

-- GO Signals end of batch (send to server)
-- Decide whether each table creations should be sent separately or all at once.

-- IF EXISTS is not a valid MSSQL command
--DROP TABLE IF EXISTS histories;
--DROP TABLE IF EXISTS documents;
--DROP TABLE IF EXISTS deals;
--DROP TABLE IF EXISTS persons;
--DROP TABLE IF EXISTS coworkers;
--DROP TABLE IF EXISTS offices;
--DROP TABLE IF EXISTS companies;

IF (EXISTS (SELECT * 
                 FROM INFORMATION_SCHEMA.TABLES 
                 WHERE TABLE_SCHEMA = 'LimeDB' 
                 AND  TABLE_NAME = 'histories'))
BEGIN
    DROP TABLE IF EXISTS histories;
END

IF (EXISTS (SELECT * 
                 FROM INFORMATION_SCHEMA.TABLES 
                 WHERE TABLE_SCHEMA = 'LimeDB' 
                 AND  TABLE_NAME = 'documents'))
BEGIN
    DROP TABLE IF EXISTS documents;
END

IF (EXISTS (SELECT * 
                 FROM INFORMATION_SCHEMA.TABLES 
                 WHERE TABLE_SCHEMA = 'LimeDB' 
                 AND  TABLE_NAME = 'deals'))
BEGIN
    DROP TABLE IF EXISTS deals;
END

IF (EXISTS (SELECT * 
                 FROM INFORMATION_SCHEMA.TABLES 
                 WHERE TABLE_SCHEMA = 'LimeDB' 
                 AND  TABLE_NAME = 'persons'))
BEGIN
    DROP TABLE IF EXISTS persons;
END

IF (EXISTS (SELECT * 
                 FROM INFORMATION_SCHEMA.TABLES 
                 WHERE TABLE_SCHEMA = 'LimeDB' 
                 AND  TABLE_NAME = 'coworkers'))
BEGIN
    DROP TABLE IF EXISTS coworkers;
END

IF (EXISTS (SELECT * 
                 FROM INFORMATION_SCHEMA.TABLES 
                 WHERE TABLE_SCHEMA = 'LimeDB' 
                 AND  TABLE_NAME = 'offices'))
BEGIN
    DROP TABLE IF EXISTS offices;
END

IF (EXISTS (SELECT * 
                 FROM INFORMATION_SCHEMA.TABLES 
                 WHERE TABLE_SCHEMA = 'LimeDB' 
                 AND  TABLE_NAME = 'companies'))
BEGIN
    DROP TABLE IF EXISTS companies;
END

GO

CREATE TABLE companies (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone VARCHAR(25),
    website VARCHAR(255),
    address VARCHAR(255),
    postcode VARCHAR(10),
    city VARCHAR(50)
);
GO

CREATE TABLE persons (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone VARCHAR(25),
    position VARCHAR(75),
    email VARCHAR(255),
    company_id INT REFERENCES Companies (id)
);
GO

CREATE TABLE offices (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone VARCHAR(25),
    address VARCHAR(255)
);
GO

CREATE TABLE coworkers (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone VARCHAR(25),
    email VARCHAR(255),
    office_id INT REFERENCES Offices (id)
);
GO

CREATE TABLE deals (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    value INT,
    probability FLOAT,
    person_id INT REFERENCES Persons (id),
    coworker_id INT REFERENCES Coworkers (id)
);
GO

CREATE TABLE documents (
    id INT NOT NULL PRIMARY KEY,
    description TEXT,
    type VARCHAR(25),
    deal_id INT REFERENCES Deals (id),
    person_id INT REFERENCES Persons (id)
);
GO

CREATE TABLE histories (
    id INT NOT NULL PRIMARY KEY,
    type VARCHAR(25),
    date DATE,
    notes TEXT,
    person_id INT REFERENCES Persons (id),
    coworker_id INT REFERENCES Coworkers (id),
    deal_id INT REFERENCES Deals (id),
    document_id INT REFERENCES Documents (id)
);
GO

-- CREATE TABLE relationships (
--     id INT NOT NULL PRIMARY KEY,
--     type VARCHAR(25),
--     from_person_id INT REFERENCES Persons (id),
--     to_person_id INT REFERENCES Persons (id),
-- );

CREATE INDEX idx_company_id
ON companies (id);
CREATE INDEX idx_person_company_id
ON persons (company_id);

CREATE INDEX idx_person_id
ON persons (id);
CREATE INDEX idx_deal_person_id
ON deals (person_id);
CREATE INDEX idx_document_person_id
ON documents (person_id);
CREATE INDEX idx_history_person_id
ON histories (person_id);

CREATE INDEX idx_office_id
ON offices (id);
CREATE INDEX idx_person_office_id
ON coworkers (office_id);

CREATE INDEX idx_coworker_id
ON coworkers (id);
CREATE INDEX idx_deal_coworker_id
ON deals (coworker_id);
CREATE INDEX idx_history_coworker_id
ON histories (coworker_id);

CREATE INDEX idx_deal_id
ON deals (id);
CREATE INDEX idx_document_deal_id
ON documents (deal_id);
CREATE INDEX idx_history_deal_id
ON histories (deal_id);

CREATE INDEX idx_document_id
ON documents (id);
CREATE INDEX idx_history_document_id
ON histories (document_id);

CREATE INDEX idx_history_id
ON histories (id);

-- CREATE INDEX idx_relationship_id
-- ON relationships (id);
-- CREATE INDEX idx_relationship_from_person_id
-- ON relationships (from_person_id);
-- CREATE INDEX idx_relationship_to_person_id
-- ON relationships (to_person_id);
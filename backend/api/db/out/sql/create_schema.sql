USE LimeDB;

-- -- Run with > sqlcmd -i create_schema.sql

-- SWITCH ALL VARCHARS TO NVARCHAR FOR UNICODE

-- GO Signals end of batch (send to server)
-- Decide whether each table creations should be sent separately or all at once.

DROP TABLE IF EXISTS histories;
DROP TABLE IF EXISTS documents;
DROP TABLE IF EXISTS deals;
DROP TABLE IF EXISTS persons;
DROP TABLE IF EXISTS coworkers;
DROP TABLE IF EXISTS offices;
DROP TABLE IF EXISTS companies;

GO

CREATE TABLE companies (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone VARCHAR(25),
    website VARCHAR(255),
    address VARCHAR(255),
    postcode VARCHAR(10),
    city VARCHAR(50),
    country VARCHAR(50)
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
    address VARCHAR(255),
    country VARCHAR(50)
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



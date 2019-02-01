USE LimeDB;

-- SWITCH ALL VARCHARS TO NVARCHAR FOR UNICODE

-- GO Signals end of batch (send to server)
-- Decide whether each table creations should be sent separately or all at once.

-- Some column names need to be renamed as they are keywords in t-sql

CREATE TABLE companies (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(30) NOT NULL PRIMARY KEY,
    phone VARCHAR(20),
    website VARCHAR(2000),
    address VARCHAR(30),
    postcode VARCAR(10),
    city VARCHAR(20),
    country VARCHAR(20)
);
GO

CREATE TABLE persons (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(30) NOT NULL PRIMARY KEY,
    position VARCHAR(30),
    email VARCHAR(20),
    company_id INT REFERENCES companies (id)
);
GO

CREATE TABLE offices (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(30) NOT NULL PRIMARY KEY,
    phone VARCHAR(20),
    address VARCHAR(30),
    country VARCHAR(20)
);
GO

CREATE TABLE coworkers (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(30) NOT NULL PRIMARY KEY,
    phone VARCHAR(20),
    email VARCHAR(20),
    office_id INT REFERENCES offices (id)
);
GO

CREATE TABLE deals (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(30) NOT NULL PRIMARY KEY,
    value INT,
    probability FLOAT,
    person_id INT REFERENCES persons (id),
    coworker_id INT REFERENCES coworkers (id)
);
GO

CREATE TABLE documents (
    id INT NOT NULL PRIMARY KEY,
    description TEXT,
    type VARCHAR(4),
    deal_id INT REFERENCES deals (id),
    person_id INT REFERENCES persons (id)
);
GO

CREATE TABLE history (
    id INT NOT NULL PRIMARY KEY,
    type VARCHAR(15),
    creation_date DATE,
    notes TEXT,
    person_id INT REFERENCES persons (id),
    coworker_id INT REFERENCES coworkers (id),
    deal_id INT REFERENCES deals (id),
    document_id INT REFERENCES documents (id)
);



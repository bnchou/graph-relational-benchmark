USE LimeDB;

-- SWITCH ALL VARCHARS TO NVARCHAR FOR UNICODE

-- GO Signals end of batch (send to server)
-- Decide whether each table creations should be sent separately or all at once.

-- Some column names need to be renamed as they are keywords in t-sql (?)

DROP TABLE IF EXISTS Histories;
DROP TABLE IF EXISTS Documents;
DROP TABLE IF EXISTS Deals;
DROP TABLE IF EXISTS Persons;
DROP TABLE IF EXISTS Coworkers;
DROP TABLE IF EXISTS Offices;
DROP TABLE IF EXISTS Companies;

GO

CREATE TABLE Companies (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    website VARCHAR(200),
    address VARCHAR(50),
    postcode VARCHAR(10),
    city VARCHAR(20),
    country VARCHAR(50)
);
GO

CREATE TABLE Persons (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    position VARCHAR(30),
    email VARCHAR(20),
    company_id INT REFERENCES Companies (id)
);
GO

CREATE TABLE Offices (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    phone VARCHAR(20),
    address VARCHAR(30),
    country VARCHAR(20)
);
GO

CREATE TABLE Coworkers (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(20),
    office_id INT REFERENCES Offices (id)
);
GO

CREATE TABLE Deals (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    value INT,
    probability FLOAT,
    person_id INT REFERENCES Persons (id),
    coworker_id INT REFERENCES Coworkers (id)
);
GO

CREATE TABLE Documents (
    id INT NOT NULL PRIMARY KEY,
    description TEXT,
    type VARCHAR(4),
    deal_id INT REFERENCES Deals (id),
    person_id INT REFERENCES Persons (id)
);
GO

CREATE TABLE Histories (
    id INT NOT NULL PRIMARY KEY,
    type VARCHAR(15),
    creation_date DATE,
    notes TEXT,
    person_id INT REFERENCES Persons (id),
    coworker_id INT REFERENCES Coworkers (id),
    deal_id INT REFERENCES Deals (id),
    document_id INT REFERENCES Documents (id)
);



// Neo4j db import location: %userprofile%\.Neo4jDesktop\neo4jDatabases\database-XXXXXXX\installation-3.X.X\import

// Cypher-shell script command:
// > cat .\load_csv.cypher | cypher-shell -u neo4j -p password --format verbose

MATCH ()-[r]-() DELETE r;
MATCH (n) DELETE n;

USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///companies.csv" AS row
CREATE (:Company {
    idcompany: row.idcompany,
    status: row.status,
    createduser: row.createduser,
    createdtime: row.createdtime,
    updateduser: row.updateduser,
    timestamp: row.timestamp,
    rowguid: row.rowguid,
    name: row.name,
    phone: row.phone,
    www: row.www,
    postaladdress1: row.postaladdress1,
    visitingaddress1: row.visitingaddress1,
    postaladdress2: row.postaladdress2,
    visitingaddress2: row.visitingaddress2,
    postalzipcode: row.postalzipcode,
    postalcity: row.postalcity,
    visitingzipcode: row.visitingzipcode,
    visitingcity: row.visitingcity,
    country: row.country,
    fullpostaladdress: row.fullpostaladdress,
    fullvisitingaddress: row.fullvisitingaddress,
    inactive: row.inactive,
    registrationno: row.registrationno,
    coworker: row.coworker,
    buyingstatus: row.buyingstatus
});

USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///persons.csv" AS row
CREATE (:Person {
    idperson: row.idperson,
    status: row.status,
    createduser: row.createduser,
    createdtime: row.createdtime,
    updateduser: row.updateduser,
    timestamp: row.timestamp,
    rowguid: row.rowguid,
    firstname: row.firstname,
    lastname: row.lastname,
    name: row.name,
    phone: row.phone,
    mobilephone: row.mobilephone,
    email: row.email,
    inactive: row.inactive,
    position: row.position,
    expireddate: row.expireddate,
    anonymizeddate: row.anonymizeddate,
    emailhardbounce: row.emailhardbounce
});

USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///offices.csv" AS row
CREATE (:Office {
    idoffice: row.idoffice,
    status: row.status,
    createduser: row.createduser,
    createdtime: row.createdtime,
    updateduser: row.updateduser,
    timestamp: row.timestamp,
    rowguid: row.rowguid,
    name: row.name,
    phone: row.phone,
    fax: row.fax,
    www: row.www,
    registrationno: row.registrationno,
    vatno: row.vatno,
    pg: row.pg,
    bg: row.bg,
    address: row.address,
    visitingaddress1: row.visitingaddress1,
    zipcode: row.zipcode,
    city: row.city,
    visitingzipcode: row.visitingzipcode,
    visitingcity: row.visitingcity,
    misc: row.misc
});

USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///coworkers.csv" AS row
CREATE (:Coworker {
    idcoworker: row.idcoworker,
    status: row.status,
    createduser: row.createduser,
    createdtime: row.createdtime,
    updateduser: row.updateduser,
    timestamp: row.timestamp,
    rowguid: row.rowguid,
    picture: row.picture,
    firstname: row.firstname,
    lastname: row.lastname,
    name: row.name,
    phone: row.phone,
    mobilephone: row.mobilephone,
    email: row.email,
    username: row.username,
    inactive: row.inactive,
    lastlogintime: row.lastlogintime,
    nbrlogin: row.nbrlogin,
    nbrupdates: row.nbrupdates,
    admin: row.admin
});

USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///deals.csv" AS row
CREATE (:Deal {
    iddeal: row.iddeal,
    status: row.status,
    createduser: row.createduser,
    createdtime: row.createdtime,
    updateduser: row.updateduser,
    timestamp: row.timestamp,
    rowguid: row.rowguid,
    name: row.name,
    dealstatus: row.dealstatus,
    value: row.value,
    probability: row.probability,
    weightedvalue: row.weightedvalue,
    wonlostreason: row.wonlostreason,
    quotesent: row.quotesent,
    expecteddate: row.expecteddate,
    closeddate: row.closeddate
});

USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///documents.csv" AS row
CREATE (:Document {
    iddocument: row.iddocument,
    status: row.status,
    createduser: row.createduser,
    createdtime: row.createdtime,
    updateduser: row.updateduser,
    timestamp: row.timestamp,
    rowguid: row.rowguid,
    comment: row.comment,
    type: row.type,
    document: row.document
});

CREATE INDEX ON :Company(idcompany);
CREATE INDEX ON :Person(idperson);
CREATE INDEX ON :Office(idoffice);
CREATE INDEX ON :Coworker(idcoworker);
CREATE INDEX ON :Deal(iddeal);
CREATE INDEX ON :Document(iddocument);

USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///persons.csv" AS row
MATCH (person:Person {idperson: row.idperson})
MATCH (company:Company {idcompany: row.company})
MERGE (person)-[:WORKS_AT]->(company);

USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///coworkers.csv" AS row
MATCH (coworker:Coworker {idcoworker: row.idcoworker})
MATCH (office:Office {idoffice: row.office})
MERGE (coworker)-[:WORKS_AT]->(office);

USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///deals.csv" AS row
MATCH (deal:Deal {iddeal: row.iddeal})
MATCH (person:Person {idperson: row.person})
MERGE (deal)<-[:RESPONSIBLE_FOR]-(person);

USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///deals.csv" AS row
MATCH (deal:Deal {iddeal: row.iddeal})
MATCH (coworker:Coworker {idcoworker: row.coworker})
MERGE (deal)<-[:SALESPERSON_FOR]-(coworker);

USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///documents.csv" AS row
MATCH (document:Document {iddocument: row.iddocument})
MATCH (person:Person {idperson: row.person})
MERGE (document)<-[:OWNS]-(person);

USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///documents.csv" AS row
MATCH (document:Document {iddocument: row.iddocument})
MATCH (deal:Deal {iddeal: row.deal})
MERGE (document)-[:ATTACHED_TO]->(deal);
-- Run with > sqlcmd -i create_db.sql

USE master;  
GO
IF DB_ID ( N'LimeDB' ) IS NOT NULL
DROP DATABASE LimeDB;
GO
CREATE DATABASE LimeDB;  
GO




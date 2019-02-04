#!/bin/bash

py fake_data.py

START=$(date +%s%3N)

sqlcmd -i create_schema.sql
py build_mssql.py
sqlcmd -i output.sql

END=$(date +%s%3N)

echo Time: $(($END - $START)) ms
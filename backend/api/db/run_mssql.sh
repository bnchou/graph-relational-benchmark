#!/bin/bash

py fake_data.py "out/output.json"
py build_csv.py "out/output.json" "out/temp"
py build_mssql.py "out/output.json" "out/output.sql"

START=$(date +%s%3N)

sqlcmd -i "out/sql/create_schema.sql"
sqlcmd -i "out/output.sql"

END=$(date +%s%3N)

echo {\"data\": $(($END - $START))} > "out/output.txt"
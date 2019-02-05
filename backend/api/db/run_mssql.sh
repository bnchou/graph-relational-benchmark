#!/bin/bash

py fake_data.py "out/output.json"
py build_mssql.py "out/output.json" "out/output.sql"

START=$(date +%s%3N)

sqlcmd -i "out/create_schema.sql"
sqlcmd -i "out/output.sql"

END=$(date +%s%3N)

echo {\"time\": $(($END - $START))} > "out/output.txt"
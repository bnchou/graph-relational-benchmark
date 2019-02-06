#!/bin/bash

if [[ $1 = "-u" ]] ; then
    echo "Updating fake data..."
    py fake_data.py "out/output.json"
fi

echo "Building csv files..."
py build_csv.py "out/output.json" "out/temp"

echo "Building sql output..."
py build_mssql.py "out/output.json" "out/output.sql"

echo "Running sql scripts..."
START=$(date +%s%3N)

sqlcmd -i "out/sql/create_schema.sql"
sqlcmd -i "out/output.sql"

END=$(date +%s%3N)

echo {\"data\": $(($END - $START))} > "out/output.txt"
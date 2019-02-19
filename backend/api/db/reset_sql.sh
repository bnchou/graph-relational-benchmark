#!/bin/bash

if [[ $1 = "-u" ]] ; then
    echo "Updating fake data..."
    py fake_data.py "out/output.json"

    echo "Building csv files..."
    py build_csv.py "out/output.json" "out/temp"

    echo "Building minimized output"
    py build_minimized.py "out/output.json" "out/output-minimized.json"
fi

echo "Building sql output..."
py build_sql.py "out/output.json" "out/output.sql"

echo "Running sql scripts..."
START=$(date +%s%3N)

sqlcmd -i "out/sql/create_schema.sql"
sqlcmd -i "out/output.sql"

END=$(date +%s%3N)

echo \"sql\": $(($END - $START))} >> "out/output.txt"
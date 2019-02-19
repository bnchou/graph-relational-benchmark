#!/bin/bash

if [[ $1 = "-u" ]] ; then
    echo "Updating fake data..."
    py fake_data.py "out/output.json"

    echo "Building csv files..."
    py build_csv.py "out/output.json" "out/temp"

    echo "Building minimized output"
    py build_minimized.py "out/output.json" "out/output-minimized.json"
fi

echo "Building cypher output..."
py build_cypher.py "out/output.json" "out/output.cypher"

echo "Running cypher scripts..."
START=$(date +%s%3N)

cat "out/output.cypher" | cypher-shell -u neo4j -p password --format verbose
cat "out/cypher/create_edges.cypher" | cypher-shell -u neo4j -p password --format verbose

END=$(date +%s%3N)

echo {\"cypher\": $(($END - $START)), > "out/output.txt"
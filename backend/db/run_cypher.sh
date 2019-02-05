#!/bin/bash

py fake_data.py "out/output.json"
py build_cypher.py "out/output.json" "out/output.cypher"

START=$(date +%s%3N)

cat "out/output.cypher" | cypher-shell -u neo4j -p password --format verbose

END=$(date +%s%3N)

echo Time: $(($END - $START)) ms
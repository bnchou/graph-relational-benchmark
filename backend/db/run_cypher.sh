#!/bin/bash

py fake_data.py

START=$(date +%s%3N)

py build_cypher.py | cypher-shell -u neo4j -p password --format verbose

END=$(date +%s%3N)

echo Time: $(($END - $START)) ms
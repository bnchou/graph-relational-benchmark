#!/bin/bash

START1=$(date +%s%3N)

cat "out/match_queries.cypher" | cypher-shell -u neo4j -p password --format verbose

END1=$(date +%s%3N)

sqlcmd -d LimeDB -i out/select_queries.sql

END2=$(date +%s%3N)

echo Time GraphDB: $(($END1 - $START1)) ms

echo Time RelationalDB: $(($END2 - $END1)) ms

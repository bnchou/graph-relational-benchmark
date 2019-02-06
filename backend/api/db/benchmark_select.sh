#!/bin/bash

T1=$(date +%s%3N)

cat "out/cypher/match_queries.cypher" | cypher-shell -u neo4j -p password --format verbose

T2=$(date +%s%3N)

sqlcmd -d LimeDB -i out/sql/select_queries.sql

T3=$(date +%s%3N)

echo Time GraphDB: $(($T2 - $T1)) ms

echo Time RelationalDB: $(($T3 - $T2)) ms

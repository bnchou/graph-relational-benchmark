#!/bin/bash

echo "--- Cypher ---"
py lexical_analyzer.py "out/cypher/$1_queries.cypher" "out/output-cypher-lexical.json"
py complexity_analyzer.py "cypher" "complexity.json" "out/output-cypher-lexical.json" "out/output-cypher-complexity.json"

echo "--- SQL ---"
py lexical_analyzer.py "out/sql/$2_queries.sql" "out/output-sql-lexical.json"
py complexity_analyzer.py "sql" "complexity.json" "out/output-sql-lexical.json" "out/output-sql-complexity.json"
#!/usr/bin/bash

# this script will delete test.db and create a new
# test.db using the data scheme "prj_tables.sql"
# and the dataset "project1_data.sql"

echo "Bash script started"

rm test.db

touch test.db

sqlite3 test.db < prj-tables.sql
sqlite3 test.db < project1_data.sql

echo "Database [test.db] successfully"
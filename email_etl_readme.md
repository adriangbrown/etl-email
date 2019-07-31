# Email test etl

## Getting Started
Requirements:  csvs with customer data, python installed 
Files to use:
  -create_tables.py
  -email_queries.py
  -email_etl.py
  -config_psql.py

Order of execution
1.  python create_tables.py - drops and creates relevant tables
2.  python email_etl.py - reads data and writes to table

## Walk-through of email_etl.py
libraries imported:  
  -pandas for csv transformations
  -psycopg2 for postgresql connection

Function

process_email_data()
  -update file path(s) for customer csv files
  -read each csv and add column to label each group, concatenate to one dataframe
  -export to csv
  -copy csv to data table

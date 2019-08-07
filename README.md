# Email test etl 
Understand the behavior of a control and test group.  Test group would continue to receive email campaigns while control group would not.  Details of each group are provided in a csv.  To make the data easier to analyze, process the csv's in pandas dataframes and write to a postgres table with appropriate label for each customer group

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
  -read each csv via pandas and add column to label each group, concatenate to one dataframe.  Multiple appends are used to concatenate each dataframe to eachother
  -export to csv
  -copy csv to data table:  fields = email_address, label
  -perform analyses on data table, joining the email_address field to other relevant tables

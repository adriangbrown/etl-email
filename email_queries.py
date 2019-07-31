# DROP TABLES
ct_drop= ("""drop table if exists dw_dev.ct;""")

# CREATE TABLES
ct_create = ("""create table if not exists dw_dev.ct (email varchar not null, label varchar not null);""")

# INSERT RECORDS
ct_table_copy = ("""copy dw_dev.ct(email, label) from stdin delimiter',';""")

# ANALYZE RESULTS

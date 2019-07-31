#!/usr/bin/python

import pandas as pd
import psycopg2
from config_psql import config
from email_queries import *

pd.set_option('display.max_columns', None)

def process_email_data(conn, cur):
  """
  Extract csv contents, add label to dataframe, and insert data into unified table
  """
  ## multiple csv files 
  control_1626 = '/Users/adrianbrown-mac/Google Drive/Python/etl/1626_control.csv'
  send_1626 = '/Users/adrianbrown-mac/Google Drive/Python/etl/1626_send.csv'
  control_215 = '/Users/adrianbrown-mac/Google Drive/Python/etl/215_control.csv'
  send_215 = '/Users/adrianbrown-mac/Google Drive/Python/etl/215_send.csv'
  
  ## Convert csv to dataframe, add labels, combine to one dataframe
  names = ['email_address']
  control_1626 = pd.read_csv(control_1626, header=None, names=names)
  control_1626['label'] = 'control_1626'
  send_1626 = pd.read_csv(send_1626, header=None, names=names)
  send_1626['label'] = 'send_1626'
  control_215 = pd.read_csv(control_215, header=None, names=names)
  control_215['label'] = 'control_215'
  send_215 = pd.read_csv(send_215, header=None, names=names)
  send_215['label'] = 'send_215'
  # Append all dataframes
  master_df = control_1626.append(send_1626).append(control_215).append(send_215)
  print master_df.groupby('label').count()
  
  ## export df to csv
  master_df.to_csv('/Users/adrianbrown-mac/Google Drive/Python/etl/master_df.csv', sep=',', header=False, index=False)

  ## copy csv contents to table
  cur.copy_expert(ct_table_copy, open('/Users/adrianbrown-mac/Google Drive/Python/etl/master_df.csv', 'r'))

def main():
  params = config()
  conn = psycopg2.connect(**params)
  conn.set_session(autocommit=True)
  cur = conn.cursor()
  process_email_data(conn, cur)

if __name__ == '__main__':
  main()

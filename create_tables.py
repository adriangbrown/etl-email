import psycopg2
from email_queries import *
from config_psql import config

def create_database():
  # Connects to analytics postgres03 database
  params = config()
  conn = psycopg2.connect(**params)
  conn.set_session(autocommit=True)
  cur = conn.cursor()
  return cur, conn

def drop_tables(cur, conn):
  cur.execute(ct_drop)

def create_tables(cur, conn):
  cur.execute(ct_create)
  conn.commit()

def main():
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()

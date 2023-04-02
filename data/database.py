import psycopg2
from psycopg2 import OperationalError

class Database:
    def __init__(self, dbname, user, password, host, port):
        self.conn = None
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            print("Connected to database successfully")
        except OperationalError as e:
            print(f"Failed to connect to database: {e}")

    def query(self, query, args=None):
        try:
            with self.conn.cursor() as cur:
                cur.execute(query, args)
                return cur.fetchall()
        except psycopg2.DatabaseError as e:
            print(f"Failed to execute query: {e}")
            self.conn.rollback()

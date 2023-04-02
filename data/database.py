import psycopg2

class Database:
    def __init__(self, dbname, user, password, host, port):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )

    def query(self, query, args=None):
        with self.conn.cursor() as cur:
            cur.execute(query, args)
            return cur.fetchall()

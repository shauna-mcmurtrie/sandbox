import psycopg2
import logging


class Postgres:

    def __init__(self, config):
        self.config = config

    def connect(self):
        try:
            return _connect('')
        except:
            logging.error("Postgres {0}/{1}: Connection failed.".format('host', 'db_name'))
            return

    def execute(self, sql):

        conn = Postgres.connect()

        try:
            return _query(conn.cursor(), sql)
        except:
            logging.error("Postgres {0}/{1}: Query failed. SQL: {2}".format('host', 'db_name', sql))
            return

    def export(self, sql):

        conn = Postgres.connect()

        try:
            return _query_fetch(conn.cursor(), sql)
        except:
            logging.error("Postgres {0}/{1}: Query failed. SQL: {2}".format('host', 'db_name', sql))
            return []


def _connect(conn_info):
    psycopg2.connect(dbname='',user='',password='',host='',port='')


def _query(cursor, sql):
    return cursor.execute(sql)


def _query_fetch(cursor, sql):
    return _query(cursor, sql).fetch_all()
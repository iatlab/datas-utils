import mysql.connector

class RDS(object):
    def __init__(self, host, port, user, password, database):
        self.settings = {
            "host": host,
            "port": port,
            "user": user,
            "password": password,
            "database": database,
        }

    def __enter__(self):
        self.conn = mysql.connector.connect(**self.settings)
        self.cur = self.conn.cursor()
        return self.cur


    def __exit__(self, exp_type, value, traceback):
        self.cur.close()
        self.conn.close()

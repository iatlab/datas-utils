import os
from unittest import TestCase
from nose.tools import eq_, ok_, raises
from datas_utils import aws

class RDSTestCase(TestCase):
    HOST = os.environ["RDS_HOST"]
    PORT = int(os.environ["RDS_PORT"])
    USER = os.environ["RDS_USER"]
    PASSWORD = os.environ["RDS_PASSWORD"]
    DATABASE = "test"

    def test_rds_connection(self):
        rds = aws.RDS(self.HOST, self.PORT,
                      self.USER, self.PASSWORD, self.DATABASE)
        with rds as (conn, cur):
            cur.execute("SELECT * FROM sample")
            rows = cur.fetchall()
        eq_(len(rows), 1)
        eq_(len(rows[0]), 1)
        eq_(rows[0][0], 1)

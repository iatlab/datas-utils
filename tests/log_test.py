from unittest import TestCase
from nose.tools import eq_, ok_, raises
from datas_utils import log

class EnvTestCase(TestCase):

    def setUp(self):
        self.logger = log.get_logger('test')

    def test_log(self):
        with self.assertLogs('test', level='INFO') as context:
            self.logger.info("A")
            self.logger.debug("B")
            self.logger.error("C")
            eq_(context.output, ["INFO:test:A", "ERROR:test:C"])

import os
from unittest import TestCase
from nose.tools import eq_
from datas_utils import env

class EnvTestCase(TestCase):

    def test_env(self):
        os.environ["A"] = "X"
        e = env.load(["A", "B"])
        eq_(e.A, "X")
        eq_(e.B, None)
        eq_(e.C, None)

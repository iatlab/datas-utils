import os
from unittest import TestCase
from nose.tools import eq_, ok_, raises
from datas_utils import env

class EnvTestCase(TestCase):

    @classmethod
    def setup_class(cls):
        os.environ["A"] = "X"
        os.environ["D"] = "30"
        os.environ["F"] = "3.01"
        os.environ["G"] = "True"
        os.environ["H"] = "False"
        os.environ["I"] = "true"
        os.environ["J"] = "false"
        os.environ["K"] = "o"

    def test_defined(self):
        e = env.load("A")
        eq_(e.A, "X")

    def test_undefined(self):
        e = env.load("B")
        eq_(e.B, None)

    @raises(KeyError)
    def test_unset(self):
        e = env.load()
        eq_(e.C, None)

    def test_int(self):
        e = env.load(D=int)
        ok_(isinstance(e.D, int))
        eq_(e.D, 30)

    @raises(ValueError)
    def test_undefined_int(self):
        env.load(B=int)

    @raises(ValueError)
    def test_invalid_int(self):
        env.load(A=int)

    def test_float(self):
        e = env.load(F=float)
        ok_(isinstance(e.F, float))
        eq_(e.F, 3.01)

    def test_capital_bool(self):
        e = env.load(G=bool, H=bool)
        ok_(isinstance(e.G, bool))
        ok_(isinstance(e.H, bool))
        ok_(e.G, "must be True")
        ok_(not e.H, "must be False")

    def test_lower_bool(self):
        e = env.load(I=bool, J=bool)
        ok_(isinstance(e.I, bool))
        ok_(isinstance(e.J, bool))
        ok_(e.I, "must be True")
        ok_(not e.J, "must be False")

    @raises(ValueError)
    def test_invalid_bool(self):
        env.load(K=bool)

    @raises(ValueError)
    def test_undefined_bool(self):
        env.load(L=bool)

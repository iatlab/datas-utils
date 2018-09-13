"""
Usage:
    import env
    e = env.load("ENVVAR_NAME1", "ENVVAR_NAME2")
    print(e.ENVVAR_NAME1)
"""
import os

class Env(dict):
    def __init__(self, varnames):
        for varname in varnames:
            self[varname] = os.environ.get(varname)

    def __getattr__(self, key):
        return self.get(key)

def load(varnames):
    return Env(varnames)

"""
Usage:
    import env
    e = env.load("ENVVAR_NAME1", "ENVVAR_NAME2", ENVVAR_BOOL=bool)
    print(e.ENVVAR_NAME1)
"""
import os
import distutils.util

class Env(dict):
    def __init__(self, *args, **kwargs):
        for varname in args:
            self[varname] = os.environ.get(varname)
        for varname, varclass in kwargs.items():
            varval = os.environ.get(varname)
            if varval is None:
                raise ValueError("Env. var. '{0}' of '{1}' type is undefined"\
                                 .format(varname, varclass))
            if varclass is bool:
                varval = distutils.util.strtobool(varval)
            self[varname] = varclass(varval)

    def __getattr__(self, key):
        return self[key]


def load(*args, **kwargs):
    return Env(*args, **kwargs)

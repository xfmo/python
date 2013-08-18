#!/usr/bin/env python
#-*-coding:utf-8-*-

def buildConnectionString(params):
    """Build a connection string from a dictionary of parameters"""
    return ";".join(["%s=%s" % (k,params[k]) for k in params.keys()])


if __name__ == "__main__":
    myParams = {"server":"localhost",\
            "database":"master",\
            "user":"root",\
            "pwd":"root"\
            }
    print buildConnectionString(myParams)
    print buildConnectionString.__doc__

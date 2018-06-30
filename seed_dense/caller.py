#!/usr/bin/env python3

from math import exp


class GaussCaller(object):
    def __init__(self, a, b, C=1):
        self.param_info = ["gaussian",
                           "a = " + str(a),
                           "b = " + str(b),
                           "C = " + str(C)]

        def caller(x):
            return C * exp(-a*(x - b)**2)
        self.__call__ = caller


class DecExpCaller(object):
    def __init__(self, a, C=1):
        self.param_info = ["decexp",
                           " a = " + str(a),
                           " C = " + str(C)]

        def caller(x):
            return C*exp(-a*x)
        self.__call__ = caller


class LorentzCaller(object):
    def __init__(self):
        raise ImportError

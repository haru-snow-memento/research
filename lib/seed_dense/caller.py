#!/usr/bin/env python3


from math import exp
from math import sqrt
from math import log
from math import pi as PI


class DecExpCaller(object):
    """
    (N0 / do)*exp(-d/d0)
    parameter are N0 and d0
    """
    def __init__(self, d0, N0=1.0):
        self.args = (d0, N0)
        self.param_info = ["decexp",
                           " d0 = " + str(d0),
                           " N0 = " + str(N0)]

        def caller(d):
            return (N0/d0)*exp(-d/d0)
        self.caller = caller

    def __call__(self, d):
        return self.caller(d)


class LogNormalCaller(object):
    """
    C = N0/(sigma*d*math.sqrt(2*PI))
    A = (ln(d)-ln(d0))**2
    C * exp(-A/(2*(sigma**2))
    """
    def __init__(self, d0, sigma, N0=1):
        self.args = (d0, sigma, N0)
        self.param_info = ["lognormal",
                           "d0 = " + str(d0),
                           "sigma = " + str(sigma),
                           "N0 = " + str(N0)]

        def caller(d):
            c0 = N0/(sigma*d*sqrt(2*PI))
            ao = (log(d)-log(d0))**2
            ans = c0 * exp(-ao/(2*(sigma**2)))
            return ans
        self.caller = caller

    def __call__(self, d):
        return self.caller(d)


class GaussCaller(object):
    def __init__(self, a, b, C=1):
        self.args = (a, b, C)
        self.param_info = ["gaussian",
                           "a = " + str(a),
                           "b = " + str(b),
                           "C = " + str(C)]

        def caller(x):
            return C * exp(-a*(x - b)**2)
        self.caller = caller

    def __call__(self, x):
        return self.caller(x)

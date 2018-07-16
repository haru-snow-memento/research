#!/usr/bin/env python3


# formal lib
import numpy as np
from math import exp
from .caller import DecExpCaller
from .caller import GaussCaller
from .caller import LogNormalCaller


class DistEqualRanks(DensityDistBase):
    def __init__(self):
        raise ImportError

    def _set_rank_vas(self, min_va, max_va, num):
        """
        argument value is distance(micron meter)
        """
        self.ranks = np.linspace(min_va, max_va, num)
        if min_va <= 0:
            raise AssertionError("you enter minus radius."
                                 "you must enter positive value into min_va")

class DistManualRanks:
    def __init__(self):
        raise ImportError
        # =modify=

    def _set_ranks(self, ranks_li):
        self.ranks = np.array(ranks_li)

"""
class AdminManyFuncs(object):
    def __init__(self):
        self.gaussian_call_li = []
        # C * exp-a(x-b)**2
        self.lorentz_call_li = []
        # unknown
        self.decexp_call_li = []
        # C * exp(-ax)

    def add_gaussian_caller(self, a, b, C=1):
        new_caller = GaussCaller(a, b, C)
        self.gaussian_call_li.append(new_caller)

    def reset_gaussian_callers(self):
        self.gaussian_call_li = []

    def add_lorentz_caller(self):
        raise ImportError

    def reset_lorentz_callers(self):
        self.lorntz_call_li = []

    def add_decexp_caller(self, a, C=1):
        new_caller = DecExpCaller(a, C)
        self.decexp_call_li.append(new_caller)

    def reset_decexp_callers(self):
        self.decexp_call_li = []

    def get_gene_caller(self):
        attri_li = dir(self)
        tmp = (nm for nm in attri_li if "call_li" in nm)
        for caller_li_attr in tmp:
            caller_li = getattr(self, caller_li_attr)
            for caller in caller_li:
                yield caller
"""

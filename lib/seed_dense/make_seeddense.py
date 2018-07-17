#!/usr/bin/env python3

# formal lib
import numpy as np
# my lib
from .caller import DecExpCaller
from .caller import GaussCaller
from .caller import LogNormalCaller
from .search_ratio import get_ranks_ids


def extract_newdict(old_dicts, keys_li):
    new_dict = {key: va for key, va in old_dicts
                if key in keys_li}
    return new_dict


class DensityDistBase(object):
    set_ranks_args = None
    caller_args = None
    ranks = None

    def __init__(self):
        raise ImportError

    def _set_caller(self, caller_ob):
        if not hasattr(caller_ob, "__call__"):
            raise AttributeError
        self.caller = caller_ob

    def _set_ranks(self, **kwargs):
        """
        argument value is distance(micron meter)
        """
        raise ImportError

    def _set_rank_vas(self):
        self.rank_vas = np.apply_along_axis(self.caller,
                                            0,
                                            self.ranks)

    def reset_caller(self):
        self.caller = None
        print("reset caller in DensityDist instance")

    def write_result(self, wpath):
        num = len(self.ranks)
        result = np.empty((num, 2))
        result[:, 0] = self.ranks
        result[:, 1] = self.rank_vas
        with open(wpath, "w") as write:
            write.write("# it contains seed density data in the following.")
            write.write("# " + self.caller_info)
            np.savetxt(wpath, result)
        print("completing writing file.")

    def set_caller_info(self):
        func_nm = self.caller.param_info[0]
        param_li = []
        for param_line in self.caller.param_info[1:]:
            param = param_line.split(" = ")[1]
            param_li.append(param)
        self.caller_info = "_".join(([func_nm] + param_li))

    def standardize_total_density(self, standardized_va,
                                  min_radius=1.0E-8):
        # you must modify and confirm
        """
        tmp = np.empty(len(self.ranks) + 1)
        width_ars = np.empty_like(tmp)
        tmp[:-1] = self.ranks
        dif = (self.radius_ar[-1] - self.radius_ar[-2]) / 2.0
        tmp[-1] = tmp[-2] + dif
        ranks_ar[1:] = (tmp[1:] + tmp[0:-1]) / 2.0
        ranks_ar[0] = min_radius
        delta_dif = (ranks_ar[1:] - ranks_ar[0:-1])
        integrated_va = np.dot(delta_dif, self.rank_vas)
        ratio = standardized_va / integrated_va
        self.rank_vas = self.rank_vas * ratio
        print("standardize_total_density")
        print("total density is " + str(standardized_va))
        """
        raise ImportError


class DistAutomaticRanks(DensityDistBase):
    def __init__(self, caller_ob, **kwargs):
        self._set_caller(caller_ob)
        self._set_rank_vas(**kwargs)
        self._set_rank_vas()
        self.set_caller_info()
        print("completely set.")
        print("you can write data.")

    def _set_ranks(self, min_va=1.0E-8, max_va=1.0,
                   ranks_num=10, ratio_auto=1.0/2.0,
                   seq=1000):
        tmp_lins = np.linspace(min_va, max_va,
                               seq=1000)
        candidate_vas = np.apply_along_axis(self.caller,
                                            0,
                                            tmp_lins)
        max_id = np.argmax(candidate_vas)
        ranks_ids_ar = get_ranks_ids(max_id, tmp_lins,
                                     candidate_vas,
                                     ranks_num,
                                     ratio=ratio_auto)
        self.ranks = tmp_lins[ranks_ids_ar]

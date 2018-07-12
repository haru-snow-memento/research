#!/usr/bin/env python3

# formal lib
import numpy as np
import matplotlib.pyplot as plt
from itertools import product
# my lib
from seed_dense.caller import DecExpCaller
from seed_dense.caller import LogNormalCaller


class AdminLognominal(object):
    def __init__(self, d0_file, sigma_file, N0_file):
        self.d0_ars = np.loadtxt(d0_file)
        self.sigma_ars = np.loadtxt(sigma_file)
        self.N0_ars = np.loadtxt(N0_file)
        self.standard_N0_ars = np.array([1.0])
        self.reset_gene_combination()

    def reset_gene_combination(self):
        self.gene_combination = product(
                                    self.d0_ars,
                                    self.sigma_ars,
                                    self.standard_N0_ars
                                       )
        
    def set_filter_ratio(self, dmin, dmax, maxmin_ratio=0.01):
        self.d_ars = np.linspace(dmin, dmax, 300)
        self.filter_ratio = 0.01

    def gene_filetered_patten(self, lognormals_gene):
        for lognormal_f, args in lognormals_gene:
            result_ar = np.apply_along_axis(lognormal_f, 0, self.d_ars)
            max_va = np.max(result_ar)
            edge_va = result_ar[-1]
            if (min_va / max_va) < self.filter_ratio:
                d0_sigma_li = list(args)[:-1]
                yield d0_sigma_li
            else:
                continue

    def gen:
        pass

    def gene_lognominal_caller_and_args(self):
        for args in gene_multi_lognominal_caller:
            yield (LogNormalCaller(*args), args)
 
    # the following methods are related to plot
    def set_plot(self, xmin=-0.001, xmax=1.5,
                 ymin=None, ymax=None):
        self.range_xminmax = (xmin, xmax)
        self.range_yminmax = (ymin, ymax)

    def plot_total_data(self):
        pass


class AdminDecExp(object)
    def __init__(self, d0_file, sigma_file, N0_file):
        pass

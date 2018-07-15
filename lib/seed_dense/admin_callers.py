#!/usr/bin/env python3

# formal lib
import numpy as np
import matplotlib.pyplot as plt
from itertools import product
# mylib
from seed_dense.caller import DecExpCaller
from seed_dense.caller import LogNormalCaller


class AdminLognormal(object):
    def __init__(self, d0_file, sigma_file, N0_file):
        self.d0_ars = np.loadtxt(d0_file)
        self.sigma_ars = np.loadtxt(sigma_file)
        self.N0_ars = np.loadtxt(N0_file)
        self.stndard_N0_ars = np.array([1.0])
        self.reset_gene_combination()

    def reset_gene_combination(self):
        self.gene_combination = product(
                                self.d0_ars,
                                self.sigma_ars,
                                self.standard_N0_ars
                                       )

    def set_filter_ratio(self, dmin=1.0E-8, dmax=1.0,
                         maxmin_ratio=0.01, seq=300):
        """
        you must use it before generatorys in the following.
        """
        self.d_ars = np.linspace(dmin, dmax, seq)
        self.filter_ratio = maxmin_ratio

    def gene_caller_and_args(self):
        for args in self.gene_combination():
            yield (LogNormalCaller(*args), args)

    def gene_filetered_args(self, lognormals_gene):
        for lognormal_f, args in lognormals_gene:
            result_ar = np.apply_along_axis(lognormal_f, 0, self.d_ars)
            max_va = np.max(result_ar)
            edge_va = result_ar[-1]
            if (edge_va / max_va) < self.filter_ratio:
                d0_sigma_li = list(args[:-1])
                yield d0_sigma_li
            else:
                continue

    def gene_filetered_caller_and_args(self, lognormals_gene):
        for lognormal_f, args in lognormals_gene:
            result_ar = np.apply_along_axis(lognormal_f, 0, self.d_ars)
            max_va = np.max(result_ar)
            edge_va = result_ar[-1]
            if (edge_va / max_va) < self.filter_ratio:
                d0_sigma_li = list(args[:-1])
                yield (lognormal_f, d0_sigma_li)
            else:
                continue

    def total_gene(self, dmin=1.0E-8, dmax=1.0, maxmin_ratio=0.01, seq=300):
        self.set_filter_ratio(dmin, dmax, maxmin_ratio, seq)
        tmp = self.gene_caller_and_args()
        filtered_args = list(self.gene_filetered_args(tmp))
        for d0_sigma, N0 in product(filtered_args, self.N0_ars):
            d0, sigma = d0_sigma
            yield LogNormalCaller(d0, sigma, N0)

    # ======= the following methods are related to plot =======
    def set_plot(self, xmin=-1.0E-4, xmax=1.5,
                 ymin=None, ymax=None, seq=300):
        self.range_xminmax = (xmin, xmax)
        self.range_yminmax = (ymin, ymax)
        self.x_ars = np.linspace(xmin, xmax, seq)

    def plot_total_data(self):
        for caller, args in self.gene_caller_and_args():
            y_ars = np.apply_along_axis(caller,
                                        0,
                                        self.x_ars)
            label_nm = "_".join(args)
            plt.plot(self.x_ars, y_ars, label=label_nm)
        plt.xlim(*self.range_xminmax)
        plt.ylim(*self.range_yminmax)
        plt.legend()


class AdminDecExp(object):
    def __init__(self, d0_file, N0_file):
        self.d0_ars = np.loadtxt(d0_file)
        self.N0_file = np.loadtxt(N0_file)
        self.standard_N0_ars = np.array([1.0])
        self.reset_gene_combination()

    def reset_gene_combination(self):
        self.gene_combination = product(
                                    self.d0_ars,
                                    self.standard_N0_ars
                                       )

    def set_filter_ratio(self, dmin=1.0E-8, dmax=1.0,
                         maxmin_ratio=0.01, seq=300):
        self.d_ars = np.linspace(dmin, dmax, seq)
        self.filter_ratio = maxmin_ratio

    def gene_caller_and_args(self):
        for args in self.gene_combination():
            yield (DecExpCaller(*args), args)

    def gene_filetered_args(self, decexp_gene):
        for decexp_f, args in decexp_gene:
            result_ar = np.apply_along_axis(decexp_f, 0, self.d_ars)
            max_va = np.max(result_ar)
            edge_va = result_ar[-1]
            if (edge_va / max_va) < self.filter_ratio:
                d0 = args[0]
                yield d0
            else:
                continue

    def gene_filetered_caller_and_args(self, decexp_gene):
        for decexp_f, args in decexp_gene:
            result_ar = np.apply_along_axis(decexp_f, 0, self.d_ars)
            max_va = np.max(result_ar)
            edge_va = result_ar[-1]
            if (edge_va / max_va) < self.filter_ratio:
                d0 = args[0]
                yield (decexp_f, d0)
            else:
                continue

    def total_gene(self, dmin=1.0E-8, dmax=1.0, maxmin_ratio=0.01, seq=300):
        self.set_filter_ratio(dmin, dmax, maxmin_ratio, seq)
        tmp = self.gene_caller_and_args()
        filtered_args = list(self.gene_filetered_args(tmp))
        for d0_sigma, N0 in product(filtered_args, self.N0_ars):
            d0, sigma = d0_sigma
            yield LogNormalCaller(d0, sigma, N0)

    # ======= the following methods are related to plot =======
    def set_plot(self, xmin=-1.0E-4, xmax=1.5,
                 ymin=None, ymax=None, seq=300):
        self.range_xminmax = (xmin, xmax)
        self.range_yminmax = (ymin, ymax)
        self.x_ars = np.linspace(xmin, xmax, seq)

    def plot_total_data(self):
        for caller, args in self.gene_caller_and_args():
            y_ars = np.apply_along_axis(caller,
                                        0,
                                        self.x_ars)
            label_nm = "_".join(args)
            plt.plot(self.x_ars, y_ars, label=label_nm)
        plt.xlim(*self.range_xminmax)
        plt.ylim(*self.range_yminmax)
        plt.legend()

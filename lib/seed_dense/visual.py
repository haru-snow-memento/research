#!/usr/bin/env python3


import numpy as np
import matplotlib.pyplot as plt


class VisuaDist(object):
    def __init__(self, rpath):
        density_ar = np.loadtxt(rpath)
        tmp = density_ar[:, 0]
        ref_nums = np.argsort(tmp)
        self.radius_ar = tmp[ref_nums]
        self.dense_ar = density_ar[:, 1][ref_nums]
        self._stratify_radius()
        self._set_range_mat()

    def _stratify_radius(self):
        tmp = np.empty(len(self.radius_ar) + 1)
        ranks_ar = np.empty_like(tmp)
        tmp[:-1] = self.radius_ar
        dif = (self.radius_ar[-1] - self.radius_ar[-2]) / 2.0
        tmp[-1] = tmp[-2] + dif
        ranks_ar[1:] = (tmp[1:] + tmp[0:-1]) / 2.0
        ranks_ar[0] = 0
        self.ranks_range_ar = ranks_ar

    def _set_range_mat(self):
        """
        range_ar is matrix(n line, 2 row)
        """
        tmp_1 = self.ranks_range_ar[0:-1]
        tmp_2 = self.ranks_range_ar[1:]
        range_mat = np.vstack((tmp_1, tmp_2)).T
        self.range_mat = range_mat

    def plot_dense_act_radius(self):
        tmp = np.vstack([self.dense_ar] * 2).T
        y_ar = tmp.reshape(-1)
        y_li = y_ar.tolist()
        y_li.extend([0, 0])
        x_li = self.range_mat.reshape(-1).tolist()
        tmp = x_li[-1]
        x_li.extend([tmp, 0])
        plt.fill(x_li, y_li, color="y")
        plt.xlim(0,)
        plt.ylim(0,)

#!/usr/bin/env python3:
:
import numpy as np
from scipy.stats.kde import gaussian_kde
import matplotlib.pyplot as plt
import scipy as scp
from scipy.interpolate import interp1d
import pandas as pd
from pandas import DataFrame, Series


FEARTURE_DIST_COLS = ["max", "min", "moment_", "avemoment_"]


class AdminAnalyzerDist(object):
    def __init__(self):
        pass



class AnlyzerDist(object):
    def _load_ar(self, fcsv, keynm=""):
        self.data_ar = pd.read_csv(fcsv, hrader=None).values
        self.keynm = keynm

    def set_feature_values(self, max_moment=2):
        dist_max_va = np.max(self.data_ar)
        dist_min_va = np.min(self.data_ar)
        dist_0moment_1 = np.average(self.dist_ar)
        for mom_num in range(2, max_moment+1):
            pass
        feature_series = Series()
    
    def set_histgram_data(self, hist_option):
        pass

    def set_kernel_density_estimationi_data(self, param_option):
        pass

    def restratify_KDE_data(self, ranks_ar):
        pass


class CalcDifDist(object):
    def __init__(self):
        pass
    def calc(self):
        pass

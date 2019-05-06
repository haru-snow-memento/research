#!/usr/bin/env python3


import numpy as np
from pandas import DataFrame

G_COL = "G"
R_COL = "R"
V_COL = "V"


class AdminGVConverterForHunt(object):
    def __init__(self):
        self.Gn_Vm_list = []

    def load_GV_ar(self, load_ar,
                   Gcol_num=0, Vcol_num=1):
        self.base_GV_ar = np.loadtxt(load_ar)
        self.base_df = DataFrame(self.base_GV_ar)
        col_nms = ["_"] * 2
        col_nms[Gcol_num] = G_COL
        col_nms[Vcol_num] = V_COL
        self.base_df.columns = col_nms

    def set_nm_list(self, Gn_Vm_list):
        if type(Gn_Vm_list) != list:
            raise TypeError(
                    "Gn_Vm_list is invalid type.")

    def add_nm_list(self, G_n, V_m):
        add_params = (G_n, V_m)
        self.Gn_Vm_list.append(add_params)

    def set_GVConverter_li(self):
        self.GVConverter_li = []
        for G_n, V_m in self.Gn_Vm_list:
            self.GVConverter_li.append(
                                 GVConverter(G_n, V_m)
                                      )

    def set_converted_GVdf(self):
        caller_num = len(self.GVConverter_li)
        data_num = len(self.base_GV_ar)
        GV_feature_var = np.empty((data_num, caller_num))
        colnms = []
        for num, converter in enumerate(self.GVConverter_li):
            colnms.appned(converter.col_nm)
            vectorized_cnvter = np.vectorize(converter)
            tmp_ar = vectorized_cnvter(self.base_df[G_COL].vslues,
                                       self.base_df[V_COL].values)
            GV_feature_var[:, num] = tmp_ar
        self.converted_GVdf = DataFrame(GV_feature_var)
        self.converted_GVdf.columns = colnms


class GVConverter(object):
    def __init__(self, G_n, V_m):
        self.G_n = G_n
        self.V_m = V_m

    def __call__(self, G, V):
        ans = (G**self.G_n)*(V**self.V_m)
        return ans

    @property
    def col_nm(self):
        col_nm = "G_{:3e}_V_{:3e}".format(self.G_n,
                                          self.V_m)
        return col_nm

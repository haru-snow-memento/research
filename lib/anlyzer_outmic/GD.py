#!/usr/bin/env python3


import numpy as np
import pandas as pd
from math import pi


SIM_TIME_COL = "simulation_time(s)"
GRAIN_NUM = "grain_number"
PHASE_NUM = "phaase_number"
SURFACE = "surface(micro-m**2)"
VAR_SURFACE = "variant_surface(micro-m**2/s)"
PERIMETER = "perimeter"
STATUS = "status"
AVERAGED_CURVATURE = "averagede_curvature(1/micro-m)"
NUM_NEIGHBOURS = "num_of_neighbors"
LIST_OF_NEIGHBORS = "list_of_neighbors_id"
DF_COLNMS = [SIM_TIME_COL, GRAIN_NUM, PHASE_NUM, SURFACE, VAR_SURFACE,
             PERIMETER, AVERAGED_CURVATURE, STATUS, NUM_NEIGHBOURS,
             LIST_OF_NEIGHBORS]


def cnvt_tottxt_to_df(fpath):
    with open(fpath) as read:
        processed_gene = gene_notcmt_from_file(read)
        total_df = pd.read_csv(processed_gene, header=None,
                               delim_whitespace=True,
                               skipinitialspace=True)
    total_df.columns = DF_COLNMS
    return total_df


def gene_notcmt_from_file(read_gene):
    """
    it's caller by cnvt_tottxt_to_df function.
    """
    for line in read_gene:
        tmp = line.strip()
        if tmp[0] == "#":
            continue
        else:
            yield line


def gene_multi_df_from_tottxt(fpath):
    with open(fpath) as read:
        readcontainer = read.readlines()
    data_idstp_li = _extract_data_stfin_idstps(
                                    readcontainer
                                             )
    for start_id, fin_id in data_idstp_li:
        partial_df = pd.read_csv(
                        readcontainer[start_id:fin_id],
                        header=None,
                        delim_whitespace=True,
                        skipinitialspace=True
                                )
        yield partial_df


def _extract_data_stfin_idstps(readcontainer):
    """
    it's caller by gene_multi_df_from_tottxt generator
    """
    cmt_ids = _extract_cmt_lineid(readcontainer)
    start_ids = _search_start_ids(cmt_ids)
    start_ids = cmt_ids[start_ids:]
    start_ids.append(None)
    data_idstp_li = []
    for counter, start_id in enumerate(start_ids[:-1]):
        fin_id = start_ids[counter + 1]
        data_idstp_li.append((start_ids, fin_id))
    return data_idstp_li


def _extract_cmt_lineid(read):
    """
    it's caller by _extract_data_stfin_idstps function
    """
    cmt_ids = []
    for num, line in enumerate(read):
        tmp = line.strip()
        if tmp[0] == "#":
            cmt_ids.append(num)
        else:
            continue


def _search_start_ids(cmt_ids):
    """
    it's caller by _extract_data_stfin_idstps
    """
    for counter, cmtid in enumerate(cmt_ids):
        if counter != cmt_ids:
            return counter - 1


class AnalyGD(object):
    def __init__(self):
        pass

    def load_dfs(self, fpath):
        multidf_gene = gene_multi_df_from_tottxt(fpath)
        self.multi_dfs(multidf_gene)

    def _calc_weighted_averaged_diameter(self, target_df):
        surface_vaar = target_df["SURFACE"].value
        diameters = 2 * np.sqrt(surface_vaar / (4 * pi))
        weighted_ave_diameter = np.average(diameters, weights=surface_vaar)
        mom2_elm = (diameters - weighted_ave_diameter) ** 2
        dispersion = np.average(mom2_elm, weights=surface_vaar)
        return (weighted_ave_diameter, dispersion)

    def set_averaged_diameters(self):
        self.ave_disp_diameters_li = [self._calc_weighted_averaged_diameter(df)
                                      for df in self.multi_dfs]

    def add_partial_data_of_diameter(self, fpath, nums):
        wlines = []
        for i in range(nums):
            tpdata = self.ave_disp_diameters_li[i]
            line = self._help_make_linedata(tpdata)
            wlines.append(line)
        with open(fpath, "a") as add:
            add.writelines(wlines)

    def _help_make_linedata(self, ave_disp_tp):
        line = " ".join(ave_disp_tp) + "\n"
        return line

#!/usr/bin/env python3


import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import os
import sys

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


def gene_notcmt_from_file(read_gene):
    for line in read_gene:
        tmp = line.strip()
        if tmp[0] == "#":
            continue
        else:
            yield line


def cnvt_tottxt_to_df(fpath):
    with open(fpath) as read:
        processed_gene = gene_notcmt_from_file(read)
        total_df = pd.read_csv(processed_gene, header=None,
                               delim_whitespace=True,
                               skipinitialspace=True)
    total_df.columns = DF_COLNMS
    return total_df


def gene_multi_df_from_tottxt(fpath):
    with open(fpath) as read:
        processed_gene = 
    
    


class AnalyGD(object):
    def __init__(self):
        pass

#!/usr/bin/env python3


import subprocess
import pandas as pd

COMMAND_BASE = "aimsgb gb ${0[rotation_axis]} ${0[sigma]} "\
               "${0[plane]} ${input_poscar} -c"
ROTAT_AXIS_KEY = "rotation_axis"
SIGMA_KEY = "sigma"
PLANE = "plane"
INPUT_POSCAR_KEY = "input_poscar"
# data frame columns
SIGMA_COL = "Sigma"
THETA_COL = "Theta"
GB_PLANE1_COL = "Plane1"
GB_PLANE2_COL = "Plane2"
CSL1_COL = "CSL1"
CSL2_COL = "CSL2"
DF_COLS = [SIGMA_COL, THETA_COL, GB_PLANE1_COL, GB_PLANE2_COL,
           CSL1_COL, CSL2_COL]


class CSLMoldelMaker(object):
    def __init__(self, in_poscar, csv_data):
        self.in_poscar = in_poscar
        self.CSL_datadf = pd.read_csv(csv_data,
                                      comment="#")

    def set_tgdir_and_
        pass

#!/usr/bin/env python3


import numoy as np
import pandas as pd
from pandas import DataFrame
import os
import sys


PHI1_COL = "phi1(radians)"
PHII_COL = "PHI(radians)"
PHI2_COL = "phi2(radians)"
X_COL = "coordinate_x(micro)"
Y_COL = "coordinate_y(micro)"
IQ_COL = "IQ(image_quality)"
CI_COL = "CI(confidence Index)"
FIT_COL = "Fit(degree)"
PHASE_ID_COL = "Phase_index"
SEM_COL = "sem"
COLNMS = [PHI1_COL, PHII_COL, PHI2_COL, X_COL, Y_COL, IQ_COL, FIT_COL,
          PHASE_ID_COL, SEM_COL]


def load_csv(fcsv):
    with open(fcsv, "r") as read:
        without_cmt = (read for line in read if read[0] != "#")
        target_df = pd.read_csv("", header=None, sep="\s+")
    num = len(COLNMS)
    target_df = target_df.iloc[:, range(num)]
    return target_df


class AanlyEBSD(object):

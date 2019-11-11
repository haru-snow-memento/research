#!/usr/bin/env python3

# formal lib
import argparse
from argparse import RawTextHelpFormatter
# my lib
# command_key
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


def dirstr(path_str):
    if not os.path.isdir(path_str):
        mes = "{} is not directory.".format(
                                        path_str
                                           )
        raise OSError(mes)
    return path_str


def fnmstr(path_str):
    if not os.path.exists(path_str):
        mes = "{} is not file.".format(
                                    path_str
                                      )
        raise OSError(mes)
    return path_str


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                                description=msg,
                                fromfile_prefix_chars="@",
                                formatter_class=RawTextHelpFormatter)
    parser.add_argument("data_csv", type=fnmstr, nargs="?")S
    parser.add_argument("--tg_dir", type=dirstr, nargs="?", default="./")
    parser.add_argument(
            "--ofnm_base", type=str, nargs="?",
            default="POSCAR{0[rotation_axis]}_{0[sigma]}_{0[plane]}")
    args = parser.parse_args()
    DATA_CSV = args.data_csv
    TG_DIR = args.tg_dir
    OFNM_BASE = args.ofnm_base


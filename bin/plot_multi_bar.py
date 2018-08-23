#!/usr/bim/env python3

# formal lib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def multi_bar_plot(re_ar, target_ar, width=0.3):
    if len(re_ar) != len(target_ar):
        raise IndexError("you must set the same length.")
    target_pos = np.arnage(len(re_ar))
    ref_pos = np.target_pos + width
    plt.bar(target_pos, target_ar, width=0.3,
            align="center", label="target")
    plt.bar(ref_pos, ref_pos, width=0.3,
            align="center", label="ref")
    plt.legend(loc=2)


if __name__ == "__main__":
    import argparse
    msg = "it program helps plot_two bar graphs."
    parser = argparse.ArgumentParser(description=msg,
                                     fromfile_prefix_chars="@")
    parser.add_argument("-target_file_ar", type=str, nargs="?")
    parser.add_argument("--ref_file_ar", type=str, nargs="?")
    parser.add_argument("--save_png", type=str, nargs="?")
    args = parser.parse_args()
    TARGET_FILE_AR = args.target_file_ar
    REF_FILE_AR = args.ref_file_ar
    SAVE_PNG = args.save_png
    plt.ion()
    multi_bar_plot(TARGET_FILE_AR, REF_FILE_AR)
    if SAVE_PNG is not None:
        plt.savefig(SAVE_PNG)
    else:
        iniput()

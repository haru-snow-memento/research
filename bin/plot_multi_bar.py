#!/usr/bin/env python3

# formal lib
import numpy as np
import matplotlib.pyplot as plt


def multi_bar_plot(target_ar, ref_ar, width=0.3):
    if len(ref_ar) != len(target_ar):
        raise IndexError("you must set the same length.")
    target_pos = np.arange(len(ref_ar))
    ref_pos = target_pos + width
    plt.bar(target_pos, target_ar, width=0.3,
            align="center", label="target")
    plt.bar(ref_pos, ref_ar, width=0.3,
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
    ref_ar = np.loadtxt(REF_FILE_AR)
    target_ar = np.loadtxt(TARGET_FILE_AR)
    multi_bar_plot(target_ar, ref_ar)
    if SAVE_PNG is not None:
        plt.savefig(SAVE_PNG)
    else:
        input()

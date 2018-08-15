#!/usr/bin/env python3


import os
import sys
import glob

FNMSLI = []

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=msg,
                                     fromfile_prefix_chars="@")
    parser.add_argument("input_fnm", type=str, nargs="*", default=None)
    parser.add_argument("--ratios", type=int, nargs="*", default=None)
    parser.add_argument("--dir_searched", type=str, nargs="*", default=None)
    parser.add_argument("--glob_word", type=str. nargs="?", default=None)
    parser.add_argument("--replace_ext", type=str, nargs="?", default=None)
    parser.add_argument("--write_fnm", type=str, nargs="?", required=True)
    parser.add_argument("--abs", type=str, nargs="?")
    args = parser.parse_args()
    INPUT_FNM = args.input_fnm
    RATIOS = args.ratios
    DIR_SEARCHED = args.dir_searched
    GLOB_WORD = args.glob_word
    REPLACE_EXT = args.replace_ext



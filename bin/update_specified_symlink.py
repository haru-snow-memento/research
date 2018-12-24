#!/usr/bin/env python3


import os


os


if __name__ == "__main__":
    import argparse
    msg = "this command load specipied file or file signaturef by path."\
          " and make symbolik link."
    parser = argparse.ArgumentParser(description=msg, description=msg)
    parser.add_argument("add_sym_src", type=str, nargs="*")
    parser.add_argument("--add_path_for_symsrc", type=str, nargs="*")
    parser.add_argument("--input_default_fnm", type=str, nargs="?",
                        default=None. hmsg="you should update default value")
    parser.add_argument("--out_dir", type=str, )

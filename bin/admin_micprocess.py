#!/usr/bin/env python3

# formal lib
import os
# mylib
from admin_process import MultiSubP

ENV = os.environ.copy()


if __name__ == "__main__":
    import argparse
    msg = ""
    parser = argparse.ArgumentParser(description=msg,
                                     fromfile_prefix_chars="@")
    # required arguments
    parser.add_argument("--read_file", type=str, nargs="?", required=True)
    # input_str
    parser.add_argument("--input_str", type=str, nargs="?", default=b"\r")
    parser.add_argument("--outdir", type=str, nargs="?", default=None)
    parser.add_argument("--set_read", default=True, action="store_false")
    parser.add_argument("--time_out", default=None, type=float, nargs="?")
    parser.add_argument("--off_save_memory", default=True,
                        action="store_true")
    args = parser.parse_args()
    READ_FILE = args.read_file
    INPUT_STR = args.input_str
    OUT_DIR = args.outdir
    SET_READ = args.set_read
    TIME_OUT = args.time_out
    OFF_SAVE_MEMORY = args.off_save_memory
    admin_multisub_ins = MultiSubP(READ_FILE, SET_READ)

    if OUT_DIR is not None:
        admin_multisub_ins.set_output_fpipe(OUT_DIR)
    if OFF_SAVE_MEMORY:
        admin_multisub_ins.remove_output_pipe()
    proc_gene = admin_multisub_ins.add_input_to_proc_gene(INPUT_STR)
    proc_li = []
    if TIME_OUT is not None:
        run_procs = [proc for proc in proc_gene]
        for proc in run_procs:
            proc.communicate(TIME_OUT)
            proc_li.append(proc)
        print("finish all calculation")
    else:
        run_procs = [proc for proc in proc_gene]
        for proc in run_procs:
            print(proc.communicate())
            proc_li.append(proc)
        print("finish all calculation")

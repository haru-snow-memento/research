#!/usr/bin/env python3

import numpy as np


class ConvertLineVa(object):
    def __init__(self, inpath):
        self.totoal_ar = np.loadtxt(inpath)
        self.ini_cmt_lines = []
        with open(inpath, "r") as read:
            for line in read:
                if line[0] == "#":
                    self.ini_cmt_lines.append(line)
                else:
                    break

    def convert_colline_ar(self, colnum, va_ar):
        if hasattr(va_ar, "__iter__"):
            colline = np.array(va_ar)
            if len(colline) != len(self.otoal_ar):
                raise IndexError
        elif type(va_ar) == float:
            colline = np.empty(len(self.totoal_ar))
            colline[:] = va_ar
        else:
            raise AssertionError("invalid arguments are input.")
        self.totoal_ar[:, colnum] = colline

    def vconvert_rowline_ar(self, rownum, va_ar):
        if hasattr(va_ar, "__iter__"):
            colline = np.array(va_ar)
            if len(colline) != self.totoal_ar.shape[1]:
                raise IndexError
        elif type(va_ar) == float:
            colline = np.empty(len(self.totoal_ar))
            colline[:] = va_ar
        else:
            raise AssertionError("invalid arguments are input.")
        self.totoal_ar[rownum, :] = colline

    def output(self, opath):
        with open(opath, "w") as write:
            write.writelines(self.ini_cmt_lines)
            np.savetxt(write, self.totoal_ar)


if __name__ == "__main__":
    import argparse
    hmsg = "this replace values of partial ar with input values."
    parser = argparse.ArgumentParser(description=hmsg,
                                     fromfile_prefix_chars="@")
    parser.add_argument("infpath_with_ar", type=str, nargs="?")
    col_group = parser.add_mutually_exclusive_group()
    col_group.add_argument("--col_num", type=int, nargs="?",
                           default=None)
    col_group.add_argument("--row_num", type=int, nargs="?",
                           default=None)
    parser.add_argument("--ar_vas_or_va", type=float, nargs="*",
                        required=True)
    parser.add_argument("--opath", type=str, nargs="?", required=True)
    args = parser.parse_args()
    INFPATH_WITH_AR = args.infpath_with_ar
    COL_NUM = args.col_num
    ROW_NUM = args.row_num
    AR_VAS_OR_VA = args.ar_vas_or_va
    if len(AR_VAS_OR_VA) == 1:
        AR_VAS_OR_VA = AR_VAS_OR_VA[0]
    OPATH = args.opath
    cnvt_ins = ConvertLineVa(INFPATH_WITH_AR)
    if COL_NUM is not None:
        cnvt_ins.convert_colline_ar(COL_NUM, AR_VAS_OR_VA)
    elif ROW_NUM is not None:
        cnvt_ins.convert_colline_ar(ROW_NUM, AR_VAS_OR_VA)
    else:
        raise AssertionError("")
    cnvt_ins.output(OPATH)

#!/usr/bin/env python3


import numpy as np
import os
import tempfile
import copy

"""
REPLACE_KEYWARD = "^#@@keywargs .......\n"\
                  "^#/@@keywargs\n"
"""


class GetReplaceLineTwoids(object):
    def __init__(self, keyword):
        self.two_ids = []
        self.ini_lword = "#@@" + keyword
        self.fin_lword = "#/@@" + keyword
        self.ini_wnum = len(self.ini_lword)
        self.fin_wnum = len(self.fin_lword)
        self.keyword = keyword

    def set_gene_num_and_line(self, gene_num_and_line):
        self.gene_num_and_line = gene_num_and_line

    def __iter__(self):
        if len(self.two_ids) == 2:
            raise StopIteration("two_ids are already set.")
        for lnum, line in self.gene_num_and_line:
            if self.ini_lword == line[:self.ini_num]:
                self.two_ids.append(lnum)
            elif self.fin_lword == line[:self.fin_num]:
                self.two_ids.append(lnum + 1)
            yield (lnum, line)
        if len(self.two_ids) != 2:
            raise AssertionError("two_ids must have two values.\n"
                                 "target_keyword is " + self.keyword)


class AdminRepData(object):
    def __init__(self,
                 base_fpath):
        with open(base_fpath, "r") as read:
            self.base_fdata = read.readlines()
        self.replace_gener_dict = {}
        self.inargs_li_dicts = {}
        self.inargs_iter_dicts = None
        self.caller_dicts = {}

    def set_nucleation_densities(self,
                                 density_func_fpaths):
        kword = "nucleation_density"
        gene_ins = GetReplaceLineTwoids(kword)
        self.replace_gener_dict[kword] = gene_ins
        self.inargs_li_dicts[kword] = density_func_fpaths
        self.caller_dicts[kword] = get_nucleation_density_lineli_from_fdata
        self.density_func_fpaths = density_func_fpaths

    def set_output_dirs(self,
                        output_dirs):
        kword = "output_dirs"
        gene_ins = GetReplaceLineTwoids(kword)
        self.replace_gener_dict[kword] = gene_ins
        self.inargs_li_dicts[kword] = output_dirs
        self.caller_dicts[kword] = get_output_dir_lineli
        self.output_dirs = output_dirs

    def set_temp_hists(self,
                       temp_hist_fnms):
        kword = "temp_hist"
        gene_ins = GetReplaceLineTwoids(kword)
        self.replace_gener_dict[kword] = gene_ins
        self.inargs_li_dicts[kword] = temp_hist_fnms
        self.caller_dicts[kword] = get_temp_hist_lineli
        self.temp_hist_fnms = self.temp_hist_fnms

    def set_output_micfnms(self,
                           micfnms):
        self.output_micfnms = micfnms

    def confirm_arngs_li_and_outputli(self):
        output_num = len(self.output_micfnms)
        for args_li in self.inargs_li_dicts.values():
            if len(args_li) != output_num:
                raise IndexError("input data length unmatch "
                                 "output data length.")

    def set_repkeys_and_inargs_iter_dict(self):
        self.repkeys = self.caller_dicts.keys()
        self.inargs_iter_dicts = {key: iter(args_li)
                                  for key, args_li in self.inargs_li_dicts}

    def set_total_line_ids_to_gener(self):
        first_gene = self.base_fdata
        for key, gene_num_and_line in self.replace_gener_dict.items():
            gene_num_and_line.set_gene_num_and_line(first_gene)
            first_gene = gene_num_and_line
        list(first_gene)

    def confirm_preparation(self):
        if self.inargs_iter_dicts is None:
            raise AssertionError("you must set self.inargs_iter_dicts")

    def totally_write_fnms(self):
        for oname in self.output_micfnms:
            self._write_fnms(oname)

    def _write_fnms(self, oname):
        for key in self.repkeys:
            args_cnvt_caller = self.caller_dicts[key]
            args = next(self.inargs_iter_dicts[key])
            linetwoids_ins = self.replace_gener_dict[key]
            ini, fin = linetwoids_ins.two_ids
            li_inserted = args_cnvt_caller(args)
            self.base_lines_replaced[ini:fin] = li_inserted
        base_lines_replaced = copy.deepcopy(self.base_fdata)
        with open(oname, "w") as write:
            write.writelines(base_lines_replaced)


def get_nucleation_density_lineli_from_fdata(fdata):
    radius_dist = np.loadtxt(fdata)
    args_ids = np.argsort(
                    radius_dist[:, 0]
                         )
    sorted_radius_dist = radius_dist[
                             args_ids[::-1]
                                    ]
    tmp_fnm = tempfile.NamedTemporaryFile(mode="w",
                                          delete=False)
    np.savetxt(tmp_fnm,
               sorted_radius_dist)
    fnm = tmp_fnm.name
    with open(fnm, "r") as read:
        density_line_li = read.readlines()
    os.remove(fnm)
    print("completely remove")
    return density_line_li


def get_output_dir_lineli(output_dirnm):
    if not os.path.exists(output_dirnm):
        os.makedirs(output_dirnm)
    else:
        os.path.isdir(output_dirnm)
        raise OSError(output_dirnm +
                      " is not directory.")
    return [output_dirnm + "\n"]


def get_temp_hist_lineli(temp_hist_fnm):
    if not os.path.exists(temp_hist_fnm):
        raise OSError(temp_hist_fnm +
                      " is unknown file")
    return [temp_hist_fnm + "\n"]

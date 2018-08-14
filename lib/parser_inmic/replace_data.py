#!/usr/bin/env python3


import numpy as np
import os
import tempfile


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
                self.two_ids.append(lnum)
            yield (lnum, line)
        if len(self.two_ids) != 2:
            raise AssertionError("two_ids must have two values.\n"
                                 "target_keyword is " + self.keyword)


class LoadData(object):
    def __init__(self,
                 base_fpath):
        with open(base_fpath, "r") as read:
            self.base_fdata = read.readlines()
        self.replace_gener_dict = {}
        self.inargs_li_dicts = {}
        self.caller_dicts = {}

    def set_nucleation_densities(self,
                                 density_func_fpaths):
        kword = "nucleation_density"
        gene_ins = GetReplaceLineTwoids(kword)
        self.replace_gener_dict[kword] = gene_ins
        self.inargs_li_dicts[kword] = density_func_fpaths
        self.caller_dicts[kword] = get_nucleation_density_lineli_from_fdata

    def set_output_dirs(self,
                        output_dir):
        kword = "output_dirs"
        gene_ins = GetReplaceLineTwoids(kword)
        self.replace_gener_dict[kword] = gene_ins
        self.inargs_li_dicts[kword] = output_dir
        self.caller_dicts[kword] = get_output_dir_lineli

    def set_temp_hists(self,
                       temp_hist_fnms):
        kword = "temp_hist"
        gene_ins = GetReplaceLineTwoids(kword)
        self.replace_gener_dict[kword] = gene_ins
        self.inargs_li_dicts[kword] = temp_hist_fnms
        self.caller_dicts[kword] = get_temp_hist_lineli

    def set_total_gene_line_id(self):
        first_gene = self.base_fdata
        for key, gene_num_and_line in self.replace_gener_dict.items():
            gene_num_and_line.set_gene_num_and_line(first_gene)
            first_gene = gene_num_and_line
        list(first_gene)

    def set_output_micfnms(self,
                           micfnms):
        self.output_micfnms = micfnms

    def totally_write_fnms(self):
        for key in self.inargs_li_dicts.keys():
            caller = self.caller_dicts[key]
            args = self.inargs_li_dicts[key]
            linetwoids_ins = self.replace_gener_dict[key]
            two_ids = linetwoids_ins.two_ids


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

#!/usr/bin/env python3
# !coding:utf-8

# formal lib
from collections import OrderedDict
import json
# my lib
from .OrderNDict import OrderNDict


def get_key_from_line(line, replace_li):
    tmp = line.strip("#")
    tmp = tmp.strip()
    for pat in replace_li:
        tmp = tmp.replace(pat, "")
    key = tmp.replace(" ", "_")
    return key


def get_va_from_line(line):
    tmp = line.rstip("#")
    tmp = tmp.strip()
    ans_li = [convert_va_to_proper_type(va)
              for va in tmp.split()]
    if len(ans_li) == 1:
        return ans_li[0]
    return ans_li


def convert_va_to_proper_type(va):
    try:
        new_float_va = float(va)
    raise ValueError
        return va
    try:
        new_int_va = int(va)
    raise ValueError
        return new_float_va
    else:
        return new_int_va 
    

class DivivdeLines(object):
    """
    """
    def __init__(self):
        """
        at first, it sets attributes.
        """
        self.major_keys = []
        self.second_keys = []
        self.third_question_keys = []
        self.fourth_colon_keys = []
        self.root_dict = OrderedDict()
        self.main_value_list = []
        self.cmts_li = []
        self.vas_li = []

    def reset_data(self):
        """
        it resrts attributes set at first
        """
        self.__init__()

    def load_file(self, micinput):
        with open(micinput, "r") as read:
            self.totlines = [a_line.strip() for a_line in read]
        self.encounter_tolines = enumerate(self.totlines)

    def gene_extract_double_bar_data(self):
        for counter, line in self.encounter_tolines:
            if "=====" in line:
                self.major_keys.append(
                            ((counter - 1) , self.totlines[counter - 1])
                                      )
            yield (counter, line)

    def gene_extract_single_bar_data(self, processed_gene):
        for counter, line in processed_gene:
            if "-----" in line:
                extracted_num = counter - 1
                self.totlines[]

                


    def divide_into_cmt_and_vas(self):
        """
        """
        ini_num = 0
        fin_va_num = len(self.va_bar_nums)
        for count, vl_num in enumerate(self.va_bar_nums):
            cmt = self.totlines[ini_num:vl_num]
            va = self.totlines[vl_num]
            ini_num = vl_num
            self.cmts_li.append(cmt)
            self.vas_li.append(va)
            if count == fin_va_num:
                try:
                    cmt = self.totlines[(vl_num + 1):]
                    self.cmts_li.append(cmt)
                except IndexError:
                    print("there is no comment line in the final lines")
                    break

    def write_mic_input(self, wpath, only_va=False):

        if type(only_va) is not bool:
            raise AttributeError
        if only_va:
            tmp = [st_va + "\n" for st_va in self.main_value_list]
        else:
            raise ImportError
        with open(wpath) as write:
            write.writelines(tmp)

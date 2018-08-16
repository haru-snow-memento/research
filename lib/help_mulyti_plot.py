#!/usr.bin/env python3


import matplotlib.pyplot as plt


SUBPLOT_DICT = {}
SUBPLOT_DICT[1] = [1, 1]
SUBPLOT_DICT[2] = [1, 2]
SUBPLOT_DICT[3] = [1, 3]
SUBPLOT_DICT[4] = [2, 2]
SUBPLOT_DICT[5] = [2, 3]
SUBPLOT_DICT[6] = [2, 3]
SUBPLOT_DICT[7] = [2, 4]
SUBPLOT_DICT[8] = [2, 4]
SUBPLOT_DICT[9] = [3, 3]


def generator(subplot_num):
    subplot_style = SUBPLOT_DICT[subplot_num]
    fig = plt.figure()
    for graph_num in range(subplot_num):
        sub_plt = fig.add_subplot(*subplot_style, graph_num)
        yield sub_plt

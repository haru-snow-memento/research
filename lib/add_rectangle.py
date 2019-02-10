#!/usr/bin/env python3
import numpy as np
import matplotlib.patches as patch


class AddRectangle(object):
    def __init__(self, **kargs):
        self.fig = kargs.pop("fig", None)
        self.axes = kargs.pop("axes", None)

    def set_rectanlgle_size(self, rectangle_size=(300, 300)):
        self.x_totwidth, self.y_totheight = rectangle_size

    def set_pos_ar(self, x_ar, y_ar):
        if type(x_ar) != np.ndarray or type(y_ar) != np.ndarray:
            raise TypeError("arguments must be np.ndarray")
        self.x_ar = x_ar
        self.y_ar = y_ar

    def set_facecolor(self, facecolor="none"):
        self.facecolor = facecolor

    def set_edgecolor(self, edgecolor="r"):
        self.edgecolor = edgecolor

    def set_center(self, center=True):
        self.center = center

    def gene_rectangle(self):
        if self.center:
            plot_xar = self.x_ar - self.x_totwidth/2.0
            plot_yar = self.y_ar - self.y_totheight/2.0
        else:
            plot_xar = self.x_ar.copy()
            plot_yar = self.y_ar.copy()
        for x, y in zip(plot_xar, plot_yar):
            rectangle = patch.Rectangle((x, y),
                                        width=self.x_totwidth,
                                        height=self.y_totheight,
                                        fc=self.facecolor,
                                        ec=self.edgecolor)
            yield rectangle

    def plot(self):
        for rec_pat in self.gene_rectangle():
            self.axes.add_patch(rec_pat)

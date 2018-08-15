#!/usr/bin/env python3


import cv2
import numpy as np
import copy


def get_ellipse_from_grscale_data(2D_binary_ar, scale):
    img_edge, contouters, hierarchy = cv2.findContours(2D_binary_ar, 1, 2)
    cv2.fitEllipse(2D_binary_ar)
    cnt = contouters[0]
    ellipse = cv2.fitEllipse(cnt)
    return ellipse

def get_ellipse_from_grscale_data(2D_binary_ar, scale):
    img_edge, contouters, hierarchy = cv2.findContours(2D_binary_ar, 1, 2)
    cv2.fitEllipse(2D_binary_ar)
    cnt = contouters[0]
    return cnt

def approximate_ellise(x_y_ars):
    pass




class Cv2ToEBSD(object):
    def __init__(self):
        pass

    def load_data(self, ars_pixsel_1_2_index, scale=5.0):
        self.ars_pix_1_2_id = ars_pixsel_1_2_index
        self.unique_ids = np.unique(self.ars_pix_1_2_id)
        self.pix_scale = scale

#!/usr/bin/env python3


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse


def make_ellipse(ellipse_ratio=1.0, norm=1.0):
    cond1 = ellipse_ratio <= 1.0
    cond2 = ellipse_ratio > 0
    if not (cond1 and cond2):
        raise AssertionError()
    min_axis = norm * ellipse_ratio
    max_axis = norm
    ellipse = Ellipse((0, 0),
                      width=max_axis,
                      height=min_axis)
    return ellipse

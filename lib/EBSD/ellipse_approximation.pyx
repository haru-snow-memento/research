#!/usr/bin/env python3


cdef double make_feature_vas(double x_y_ar[2]):
    cdef double x2y2, xy3, x2y, xy2, xy
    cdef double y4, xy2, y3, y2
    cdef double x2, xy, x
    cdef double y2, y
    cdef double e = 1.0
    cdef double x3y, x2y2, x3, x2y, x2
    cdef double x, y
    x = x_y_ar[0]
    y = x_y_ar[1]
    x2y2 = (x**2)*(y**2)
    xy3 = x*y**3
    x

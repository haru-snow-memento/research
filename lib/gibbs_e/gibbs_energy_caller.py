#!/usr/bin/env python3


class CallerTempeActG_Enthalpy(object):
    def __init__(self, melting_enthalpy_perv, melting_point):
        self.melting_enthalpy_perv = melting_enthalpy_perv
        self.melting_point = melting_point

    def get_gibbsE_perv(self, temperature):
        delta_tempe = temperature - self.melting_point
        if delta_tempe > 0:
            raise AssertionError("delta_tempe must be negative.\n"
                                 "because super cooling occurs.")
        tmp = self.melting_enthalpy_perv/self.melting_point
        gibbsE_perv = delta_tempe * tmp
        return gibbsE_perv

    def __call__(self, gibbsE_perv):
        ratio = 1 + (self.gibbsE_perv/self.melting_enthalpy_perv)
        super_cooling_tempe = self.melting_point * ratio
        return super_cooling_tempe


class CallerTempeActG_Entropy(object):
    def __init__(self, melting_entropy_perv, melting_point):
        self.melting_point = melting_point
        self.melting_entropy_perv = melting_entropy_perv

    def get_gibbsE_perv(self, temperature):
        delta_tempe = temperature - self.melting_point
        if delta_tempe > 0:
            raise AssertionError("delta_tempe must be negative.\n"
                                 "because super cooling occurs.")
        gibbsE_perv = delta_tempe * self.melting_entropy_perv
        return gibbsE_perv

    def __call__(self, gibbsE_perv):
        add_ratio = gibbsE_perv/(self.melting_point*self.melting_entropy_perv)
        ratio = 1 + add_ratio
        super_cooling_tempe = self.melting_point * ratio
        return super_cooling_tempe

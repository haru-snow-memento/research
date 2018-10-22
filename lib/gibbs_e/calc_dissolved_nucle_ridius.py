#!/usrbin/env python3


from pandas import DataFrame
import numpy as np
from scipy.interpolate import interp1d
from scipy import pi as PI
import copy


TEMPECOLS = "temperature[K]"
L_ENTROPY_PER_V = "Lentropy_per_v[J/Km3]"
S_ENTROPY_PER_V = "Sentropy_per_v[J/Km3]"
L_ENTHALPY_PER_V = "Lenthalpy_per_v[J/m3]"
S_ENTHALPY_PER_V = "Senthalpy_per_v[J/m3]"
L_GIBBSE_PER_V = "Lgibbs_per_v[J]"
S_GIBBSE_PER_V = "Sgibbs_per_v[J]"
DEFAULT_COLUMNS = [TEMPECOLS,
                   L_ENTROPY_PER_V, L_ENTHALPY_PER_V,
                   L_GIBBSE_PER_V, S_ENTROPY_PER_V,
                   S_ENTHALPY_PER_V, S_GIBBSE_PER_V]


def calc_total_dforce(G_per_volume, radius=1.0E-6):
    return (4/3) * PI * radius**3


def calc_interfacial_e(interf_e_per_area,
                       radius=1.0E-8):
    return 4 * PI * radius**2


class MakerInterpThermodynamics(object):
    def __init__(self, input_fnm, colnms=None):
        with open(input_fnm, "r") as read:
            first_line = read.readline()
            self.total_ar = np.loadtxt(read)
        self._set_vcolnms_and_dict_actual_cols(first_line)
        self.thermodynamics_data_df = DataFrame(self.total_ar,
                                                colnms=self.virtual_colnms)

    def _set_vcolnms_and_dict_actual_cols(self, first_line,
                                          colnms=None):
        if colnms is not None:
            self.virtual_colnms = colnms
        else:
            self.virtual_colnms = copy.deepcopy(DEFAULT_COLUMNS)
        tmp = first_line.strip()
        actual_cols = tmp.split("\t")
        self.dict_vcol_key_actcol = dict(
                                     zip(self.virtual_colnms, actual_cols)
                                        )

    def make_dGibbs_interpolater_tempe(self):
        tempe_ar = self.thermodynamics_data_df[TEMPECOLS].values
        liq_gibbs_ar = self.thermodynamics_data_df[
                                            L_GIBBSE_PER_V
                                                  ].values
        sol_gibbs_ar = self.thermodynamics_data_df[
                                            S_GIBBSE_PER_V
                                                  ].values
        solidification_gibbsv_ar = sol_gibbs_ar - liq_gibbs_ar
        drivG_perv_interp_act_tempe = interp1d(tempe_ar,
                                               solidification_gibbsv_ar)
        return drivG_perv_interp_act_tempe

    def make_tempe_interpolater_dGibbs(self):
        tempe_ar = self.thermodynamics_data_df[TEMPECOLS].values
        liq_gibbs_ar = self.thermodynamics_data_df[
                                            L_GIBBSE_PER_V
                                                  ].values
        sol_gibbs_ar = self.thermodynamics_data_df[
                                            S_GIBBSE_PER_V
                                                  ].values
        solidification_gibbsv_ar = sol_gibbs_ar - liq_gibbs_ar
        tempe_interp_act_drivG_perv = interp1d(solidification_gibbsv_ar,
                                               tempe_ar)
        return tempe_interp_act_drivG_perv


class HomogeniousNucleation(object):
    def __init__(self,
                 interfacial_E,
                 tempe_caller_gibbse_perv,
                 critical_radius=1.0E-8):
        self.critical_radius = critical_radius
        self.tempe_caller_gibbse_perv = tempe_caller_gibbse_perv
        self.interfacial_E = interfacial_E
        
    def get_gibbsE_perv_act_critical_rad(self):
        gibbsE_perv = -(2.0*self.interfacial_E)/self.critical_radius
        if gibbsE_perv > 0:
            raise AssertionError("gibbs energy is positive."
                                 "it's supporsed to be negative or zero.")
        return gibbsE_perv

    def get_supercooling_tempe_act_critical_rad(self):
        gibbs_perv = self.get_gibbsE_perv_act_critical_rad()
        supercooling_tempe = sekf.tempe_caller_gibbse_perv(gibbs_perv)
        return supercooling_tempe

    def reser_critical_rad(critical_rad=1.0E-8):
        print("critical_radius is set to " + str(critical_radius))
        self.critical_radius = critical_rad

    def reset_interfacial_E(self, interfacial_E):
        self.interfacial_E = interfacial_E

    def reset_tempe_caller_gibbse_perv(self, tempe_caller_gibbse_perv):
        self.tempe_caller_gibbse_perv = tempe_caller_gibbse_perv

#!/usr/bin/env python3

# formal lib

# my lib
from rep_inmic import AdminRepData


def main_func(base_input_fpath,
              output_dirs=None,
              nucleation_densities_fnms=None,
              temp_hists=None,
              write_fnms=None):
    admin_repd_ins = AdminRepData(BASE_INPUT_FPATH)
    if output_dirs is not None:
        admin_repd_ins.set_output_dirs(output_dirs)
    if nucleation_densities_fnms is not None:
        admin_repd_ins.set_nucleation_densities(
                                    nucleation_densities_fnms
                                               )
    if temp_hists is not None:
        admin_repd_ins.set_temp_hists(temp_hists)
    if write_fnms is not None:
        admin_repd_ins.set_output_micfnms(write_fnms)
    admin_repd_ins.confirm_preparation()
    admin_repd_ins.set_repkeys_and_inargs_iter_dict()
    admin_repd_ins.set_total_line_ids_to_gener()
    admin_repd_ins.totally_write_fnms()


if __name__ == "__main__":
    import argparse
    msg = "this program replaces keyword with input values from input_args"
    parser = argparse.ArgumentParser(description=msg,
                                     fromfile_prefix_chars="@")
    parser.add_argument("base_input_fpath", type=str, nargs="?")
    parser.add_argument("--output_dirs", type=str,
                        nargs="*", default=None)
    parser.add_argument("--nucleation_densities_fnms", type=str,
                        nargs="*", default=None)
    parser.add_argument("--temp_hists", type=str,
                        nargs="*", default=None)
    parser.add_argument("--write_fnms", type=str,
                        nargs="*", default=None)
    args = parser.parse_args()
    BASE_INPUT_FPATH = args.base_input_fpath
    OUTPUT_DIRS = args.output_dirs
    NUCLEATION_DENSITIES_FNMS = args.nucleation_densities_fnms
    TEMP_HISTS = args.temp_hists
    WRITE_FNMS = args.write_fnms
    main_func(BASE_INPUT_FPATH,
              OUTPUT_DIRS,
              NUCLEATION_DENSITIES_FNMS,
              TEMP_HISTS,
              WRITE_FNMS)

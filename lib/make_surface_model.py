#!/usr/bin//env python3


from ase.build import fcc100, fcc110
from ase.build import fcc111
from ase.build import fcc111_root, fcc211
from ase.build import bcc100, bcc110, bcc111, bcc111_root
from ase.build import hcp0001, hcp10m10, hcp0001_root
from ase.build import diamond100, diamond111


STEREO_SURFACE_CLS = [fcc100, fcc110, fcc111, fcc111_root, fcc211,
                      bcc100, bcc110, bcc111, bcc111_root,
                      hcp0001, hcp10m10, hcp0001_root,
                      diamond100, diamond111]
STEREO_SURFACE_KEYS = ["fcc100", "fcc111", "fcc111_root", "fcc211",
                       "bcc100", "bcc110", "bcc111", "bcc111_root",
                       "hcp0001", "hcp10m10", "hcp0001_root",
                       "diamond111", "diamond100"]


class SurfaceMaker(object):
    def __init__(self, symbol, size=(1, 1, 1),
                 vacuum=10.0, surface_type="fcc100"):
        self.symbol = symbol
        self._set_cell_size(size)
        self.vacuum = vacuum

    def _set_cell_size(self, size):
        if len(size) != 3:
            raise TypeError("size's length must be 3.")
        self.size = size

    def _set_surface_type(self):
        pass

    def _set_structure_ins(self):
        pass

    @staticmethod
    def from_file(poscar_file):
        raise NotImplementedError("")

    @staticmethod
    def from_dict(input_dict):
        raise NotImplementedError("")

    def to_poscar(self):
        pass

    def to_dict(self):
        pass

#!/usr/bin/env python3


class MetaBase(type):
    BASE_METHODS = set(["get_x", "set_y"])
    
    def __new__(cls, name, bases, kwrgs):
        print(name)
        print(bases)
        print(kwrgs)
        if not cls.BASE_METHODS.issubset(kwrgs.keys()):
            raise TypeError
        return type.__new__(cls, name, bases, kwrgs)
        # return type(name, bases, kwrgs)


class Child(metaclass=MetaBase):
    def __init__(self):
        pass


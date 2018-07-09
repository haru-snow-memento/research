#!/usr/bin/env python3


import pyautogui
from time import sleep


class EnterInfoBase(object):
    def __init__(self, rpath):
        with open(rpath, "r") as read:
            enter_info = [a_line for a_line in read
                          if a_line[0] == "#"]
        self.enter_info = enter_info

    def pre_command(self):
        raise ImportError

    def intermadiate_func(self):
        raise ImportError

    def enter_line_info(self, interval_t=0.5):
        for one_line in self.enter_line_info:
            pyautogui.typewrite(one_line)
            self.intermadiate_func()
            sleep(interval_t)

    def post_command(self):
        raise ImportError

    def do(self, interval_t=0.1,
           pre_args=None, post_args=None):
        if pre_args is None:
            self.pre_command()
        else:
            self.pre_command(**pre_args)
        self.enter_line_info(interval_t)
        if post_args is None:
            self.post_command()
        else:
            self.post_command(**post_args)

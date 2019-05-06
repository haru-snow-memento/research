#!/usr/bin/env python3
# !coding:utf-8

# formal lib
import pyautogui

# mylib
from .core import EnterInfoBase


class EnterMicInfo(EnterInfoBase):
    """
    it instance perate if you use do method.
    """

    def __init__(self, rpath):
        super(EnterInfoBase, self).__init__(rpath)

    def pre_command(self):
        input("are you ok?")
        pyautogui.click()

    def intermadiate_func(self):
        pyautogui.press("enter")

    def post_command(self):
        print("completely input file")
        input("___")

    def set_pyauto_pause(self, time):
        pyautogui.PAUSE = time

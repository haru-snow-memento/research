#!/usr/bin/env python3

# formal lib
# my lib
from .core import EnterInfoBase
import pyautogui


class EnterTbInfo(EnterInfoBase):
    """
    it instance perate if you use do method.
    """
    def __init__(self, rpath):
        super(EnterInfoBase, self).__init__(rpath)

    def pre_command(self):
        input("are you ready")
        pyautogui.click()

    def intermadiate_func(self):
        pyautogui.press("tab")

    def post_command(self):
        pyautogui.press("enter")
        input("it's finished")

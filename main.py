"""Minimalistic PySciter sample for Windows."""

import sciter
import ctypes
# import json

ctypes.windll.user32.SetProcessDPIAware(2)

class Frame(sciter.Window):

    def __init__(self):
        super().__init__(ismain=True, uni_theme=False, debug=True)
        self.set_dispatch_options(enable=True, require_attribute=False)

if __name__ == '__main__':
    frame = Frame()
    frame.load_file("main.html")
    frame.run_app()

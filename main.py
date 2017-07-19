"""Minimalistic PySciter sample for Windows."""

import sciter
import ctypes
import time
import win32con
SendMessage = ctypes.windll.user32.SendMessageW
from concurrent.futures import ProcessPoolExecutor as Pool
ctypes.windll.user32.SetProcessDPIAware(2)

myWM_USER = win32con.WM_USER+10

def run_proc(name, hwnd):
    time.sleep(2)
    SendMessage(hwnd, myWM_USER, 0, 0)

class Frame(sciter.Window):
    def __init__(self):
        super().__init__(ismain=True, uni_theme=False, debug=True)
        self.set_dispatch_options(enable=True, require_attribute=False)
        self.pool = Pool(max_workers=1)

    def on_message(self, hwnd, msg, wparam, lparam):
        if msg == myWM_USER:
            print("ok")
        # print(hwnd, msg, wparam, lparam)
        pass
    def test(self):
        self.pool.submit(run_proc, 'ttt', self.hwnd)

if __name__ == '__main__':
    frame = Frame()
    frame.load_file("main.html")
    frame.run_app()

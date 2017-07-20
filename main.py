"""Minimalistic PySciter sample for Windows."""

import sciter
import ctypes
import time
import win32con
import requests

from multiprocessing import Queue, Process

ctypes.windll.user32.SetProcessDPIAware(2)
SendMessage = ctypes.windll.user32.SendMessageW

myWM_USER = win32con.WM_USER+10
path = 'https://68.media.tumblr.com/c0c18a1f04a764b80d9c005b7cbe95f5/tumblr_oteae2YKrt1rzvykfo1_250.jpg'
proxies = {
    "http": "127.0.0.1:50175",
    "https": "127.0.0.1:50175"
}
file_path = 'r:/a.jpg'
def run(qq, hwnd):
    req = requests.get( path, proxies=proxies )
    with open(file_path, 'wb') as fh:
        for chunk in req.iter_content(chunk_size=1024):
            fh.write(chunk)
    qq.put([{
        'p':file_path
    }]) #子进程放入数据
    SendMessage(hwnd, myWM_USER, 0, 0)

class Frame(sciter.Window):
    def __init__(self):
        super().__init__(ismain=True, uni_theme=False, debug=True)
        self.set_dispatch_options(enable=True, require_attribute=False)
        # self.pool = Pool(max_workers=1)
        self.q = Queue()

    def on_message(self, hwnd, msg, wparam, lparam):
        if msg == myWM_USER:
            print(self.q.get()) #父进程中获取,打印
            # print("ok")
        # print(hwnd, msg, wparam, lparam)
        pass
    def test(self):
        Process(target=run, args=(self.q, self.hwnd)).start()

if __name__ == '__main__':
    frame = Frame()
    frame.load_file("main.html")
    frame.run_app()

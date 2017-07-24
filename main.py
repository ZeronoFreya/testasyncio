"""Minimalistic PySciter sample for Windows."""

import sciter
import ctypes
import time
import win32con
import requests

# from multiprocessing import Queue, Process
from multiprocessing import Process,Queue,Pool,Manager
# import multiprocessing

ctypes.windll.user32.SetProcessDPIAware(2)
postMessage = ctypes.windll.user32.PostMessageW

myWM_USER = win32con.WM_USER+10
path = 'https://68.media.tumblr.com/c0c18a1f04a764b80d9c005b7cbe95f5/tumblr_oteae2YKrt1rzvykfo1_250.jpg'
proxies = {
    "http": "127.0.0.1:50175",
    "https": "127.0.0.1:50175"
}
# proxies = {
#     "http": "127.0.0.1:61274",
#     "https": "127.0.0.1:61274"
# }
file_path = 'r:/a.jpg'
def run(qq, hwnd):
    req = requests.get( path, proxies=proxies )
    with open(file_path, 'wb') as fh:
        for chunk in req.iter_content(chunk_size=1024):
            fh.write(chunk)
    qq.put([{
        'p':file_path
    }])

    postMessage(hwnd, myWM_USER, 0, 0)

def run2(qq, hwnd):
    # time.sleep(3)
    qq.put([{
        'p':file_path
    }])
    postMessage(hwnd, myWM_USER, 0, 0)
    print("ok")
    return 0
class Frame(sciter.Window):
    def __init__(self):
        super().__init__(ismain=True, uni_theme=False, debug=True)
        self.set_dispatch_options(enable=True, require_attribute=False)

        # self.q = Queue()

        self.q = Manager().Queue()
        self.pool = Pool(processes=1)


        # self.root = self.get_root()

    def document_close(self):
        print("close")
        self.pool.close()
        self.pool.join()
        return True

    def on_message(self, hwnd, msg, wparam, lparam):
        if msg == myWM_USER:
            if not self.q.empty():
                j = self.q.get()
                print(j[0]['p'])
                return self.setImg(j)
                # self.call_function('appendImgList', j[0]['p'] )
                # print(self.q.get()) #父进程中获取,打印
            # print("ok")
        # elif msg == 2:
        #     self.pool.close()
        # print(hwnd, msg, wparam, lparam)
        pass
    def setImg(self,j):
        print("fds")
        self.call_function('appendImgList', file_path )
        pass
    def test(self):
        print("d")
        # Process(target=run2, args=(self.q, self.hwnd)).start()
        self.pool.apply_async(run2,args=(self.q, self.hwnd))

if __name__ == '__main__':
    frame = Frame()
    frame.load_file("main.html")
    frame.run_app()

"""Minimalistic PySciter sample for Windows."""

import sciter
import ctypes
import os
import time
# import json
# from concurrent.futures import ProcessPoolExecutor as Pool
# from concurrent.futures import as_completed
# from concurrent.futures import wait
from multiprocessing import Queue, Process


ctypes.windll.user32.SetProcessDPIAware(2)



def run_proc(name):
    # import time
    print( 'Run child process %s (%s)...' % (name, os.getpid()))
    # time.sleep(10)
    return 'uuu'

def run(qq):
    qq.put(["hello", None, 1]) #子进程放入数据
    print("qq run...")

def producer():
    counter = 1
    while True:
        q.put("骨头%s" %counter) #满了情况下会阻塞
        print("生产骨头%s" %counter)
        counter += 1
        time.sleep(0.5)


def cousumer(name):
    while True:
        temp = q.get() #取不到也会阻塞
        print("%s 吃了%s" %(name, temp))
        time.sleep(1)


class Frame(sciter.Window):
    def __init__(self):
        super().__init__(ismain=True, uni_theme=False, debug=True)
        self.set_dispatch_options(enable=True, require_attribute=False)
        # self.pool = Pool(max_workers=1)

    def test(self):
        # n = ['ttt']
        # f = self.pool.submit(run_proc, 'ttt')
        # if f.running():
        #     print('%s is running' % str(f))
        # results = wait(future_tasks)
        # done = results[0]
        # for x in done:
        #     print(x)

        q = Queue()
        p = Process(target=run, args=(q, ))
        p.start()
        print(q.get()) #父进程中获取,打印
        print("main process start...")



if __name__ == '__main__':
    frame = Frame()
    frame.load_file("main.html")
    frame.run_app()

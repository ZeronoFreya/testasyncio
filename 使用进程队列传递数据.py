from multiprocessing import Queue, Process #此处是从进程中导入queue
 
def run(qq):
    qq.put(["hello", None, 1]) #子进程放入数据
    print("qq run...")
 
if __name__ == "__main__":
    q = Queue()
    p = Process(target=run, args=(q, ))
    p.start()
    print(q.get()) #父进程中获取,打印
    print("main process start...")
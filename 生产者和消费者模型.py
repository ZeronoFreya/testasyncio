import queue, time, threading
 
q = queue.Queue(10)
 
def producer():
    counter = 1
    # while 10:
    q.put("骨头%s" %counter) #满了情况下会阻塞
    print("生产骨头%s" %counter)
    counter += 1
    time.sleep(0.5)
 
 
def cousumer(name):
    # while 10:
    temp = q.get() #取不到也会阻塞
    print("%s 吃了%s" %(name, temp))
    time.sleep(1)
 
 
p = threading.Thread(target=producer, )
c = threading.Thread(target=cousumer, args=("ait24",))
c2 = threading.Thread(target=cousumer, args=("txidc",))
 
p.start()
c.start()
c2.start()
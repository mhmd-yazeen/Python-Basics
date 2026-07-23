# Concurrency 
# Parallelism

import threading
import time
lock = threading.Lock()
def work(name):
    if lock:
        for i in range (1,6):
            print(name,i)
            time.sleep(1)


t1 = threading.Thread(target=work,args = ("ANNA",))
t2 = threading.Thread(target=work,args = ("VARUN",))

t1.start() # starts thread
t2.start() # starts thread

t1.join() # Waits before main program execution
t2.join()

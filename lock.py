#-*-coding:utf8;-*-
#qpy:3
#qpy:console

from __future__  import print_function
import threading
import time

value = 1

def work(l):
  global value
  for i in range(5):
    l.acquire() # schaltet den Lock ein
    value +=  1
    print(threading.currentThread().getName(), value)
    l.release() # schaltet den Lock frei
    time.sleep(3)

l = threading.Lock()

t1 = threading.Thread(target=work, args=(l,))
t2 = threading.Thread(target=work, args=(l,))

t1.start()
t2.start()

t1.join()
t2.join()
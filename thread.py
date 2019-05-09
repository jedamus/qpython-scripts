#-*-coding:utf8;-*-
#qpy:3
#qpy:console

from __future__  import print_function
import threading
import time

def gui():
  for i in range(10):
    print('#',end='')
    time.sleep(1)

def work(how_long):
  time.sleep(how_long)

t1 = threading.Thread(target=gui, name='Oberfläche', args=())
t2 = threading.Thread(target=work, name='Verarbeitung', args=(2,))

t1.start()
t2.start()

t1.join()
t2.join()
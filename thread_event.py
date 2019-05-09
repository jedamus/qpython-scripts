#-*-coding:utf8;-*-
#qpy:3
#qpy:console

from __future__  import print_function
from threading import Thread, Event
import time

def gui(e):
  while not e.is_set():
    e.wait (1)
    print('#',end='')

def work(how_long,e):
  time.sleep(how_long)
  e.set ()

e = Event()

t1 = Thread(target=gui, name='Oberfläche', args=(e,))
t2 = Thread(target=work, name='Verarbeitung', args=(2,e))

t1.start()
t2.start()

t1.join()
t2.join()
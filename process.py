#-*-coding:utf8;-*-
#qpy:3
#qpy:console

from __future__  import print_function
import multiprocessing
import time
import os

def test_it():
  print('test_it', os.getpid())
  time.sleep(3)

if __name__ == '__main__':
  print('main', os.getpid())
  p = multiprocessing.Process(target=test_it)
  p.start()
  time.sleep(1)
  p.terminate()
  print('test is alive', p.is_alive())
  p.join()
  print(p.exitcode)
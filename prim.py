#!/usr/bin/env python
#-*-coding:utf8;-*-
#qpy:2
#qpy:console
# modifiziert Montag, 13. Mai 2019 04:33 von Leander Jedamus

from __future__ import print_function
import threading
import queue
import sys

if sys.version_info.major == 2:
  my_input = raw_input
elif sys.version_info.major == 3:
  my_input = input

class Mathematiker(threading.Thread):
  Ergebnis = {}
  ErgebnisLock = threading.Lock()

  Briefkasten = queue.Queue()

  def run(self):
    while True:
      zahl = Mathematiker.Briefkasten.get()
      ergebnis = self.istPrimzahl(zahl)

      Mathematiker.ErgebnisLock.acquire()
      Mathematiker.Ergebnis[zahl] = ergebnis
      Mathematiker.ErgebnisLock.release()

      Mathematiker.Briefkasten.task_done()

  def istPrimzahl(self, zahl):
    i = 2
    if zahl % i == 0:
      return("{0} * {1}".format(zahl, zahl / i))
    i += 1
    while i*i < zahl + 1:
      if zahl % i == 0:
        return("{0} * {1}".format(zahl, zahl / i))
      i += 2
    return("prim")

if __name__ == '__main__':
  meine_threads = [ Mathematiker() for i in range(5) ]
  for thread in meine_threads:
    thread.setDaemon(True)
    thread.start()

  eingabe = my_input("> ")
  while eingabe != "ende":
    if eingabe == "status":
      print("-------- Aktueller Status --------")
      Mathematiker.ErgebnisLock.acquire()
      for (z, e) in Mathematiker.Ergebnis.items():
        print("{0}: {1}".format(z, e))
      Mathematiker.ErgebnisLock.release()
      print("----------------------------------")

    elif int(eingabe) not in Mathematiker.Ergebnis:
      i = int(eingabe)
      Mathematiker.ErgebnisLock.acquire()
      Mathematiker.Ergebnis[i] = "in Arbeit"
      Mathematiker.ErgebnisLock.release()

      Mathematiker.Briefkasten.put(i)

    eingabe = my_input("> ")

  Mathematiker.Briefkasten.join()

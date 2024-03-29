#!/usr/bin/env python
#-*-coding:utf8;-*-
#qpy:2
#qpy:console
# modifiziert Montag, 13. Mai 2019 13:24 von Leander Jedamus

from __future__ import print_function
import logging
import sys
import time
import atexit

if sys.platform == "linux4":
  import os
  os.chdir("/storage/emulated/0/com.hipipal.qpyplus/scripts")

logger = ""
atexit.register(logging.shutdown)

if __name__ == '__main__':
  handler1 = logging.StreamHandler(sys.stdout)
  handler1.setLevel(logging.DEBUG)
  handler2 = logging.FileHandler("logger.log","w")
  handler2.setLevel(logging.DEBUG)
 
  logging.Formatter.converter=time.gmtime
  logging._srcFile=None
  logging.logThreads=0
  logging.logProcesses=0
  frm = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s",
                          "%d.%m.%Y %H:%M:%S %Z")
  handler1.setFormatter(frm)
  handler1.setLevel(logging.DEBUG)
  handler2.setFormatter(frm)
  handler2.setLevel(logging.DEBUG)

  logger = logging.getLogger()
  logger.addHandler(handler1)
  logger.addHandler(handler2)
  logger.setLevel(logging.DEBUG)

  logger.critical("kritischer Zustand!")
  logger.warning ("eine Warnung")
  logger.info("dies ist eine Information.")
  if logger.isEnabledFor(logging.DEBUG):
    logger.debug("debug")
  logging.log(logging.ERROR, "Fehler!")

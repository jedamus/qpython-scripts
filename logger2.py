#!/usr/bin/env python3
#-*-coding:utf8;-*-
#qpy:2
#qpy:console
# modifiziert Montag, 13. Mai 2019 10:52 von Leander Jedamus

from __future__ import print_function
import logging
import logging.config
import sys
import atexit

if sys.platform == "linux4":
  import os
  os.chdir("/storage/emulated/0/com.hipipal.qpyplus/scripts")

logger = ""
atexit.register(logging.shutdown)

if __name__ == '__main__':
  logging.config.fileConfig("logging.conf")
  #logging.config.dictConfig("logging.yaml")

  logger = logging.getLogger(__name__)

  logger.critical("kritischer Zustand!")
  logger.warning ("eine Warnung")
  logger.info("dies ist eine Information.")
  logger.debug("debug")
  logging.log(logging.ERROR, "Fehler!")

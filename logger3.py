#!/usr/bin/env python3
#-*-coding:utf8;-*-
#qpy:2
#qpy:console
# modifiziert Mittwoch, 29. Mai 2019 06:32 von Leander Jedamus
# modifiziert Dienstag, 14. Mai 2019 00:04 von Leander Jedamus
# modifiziert Montag, 13. Mai 2019 13:39 von Leander Jedamus

from __future__ import print_function
import logging
import logging.config
import sys
import time
import atexit

if sys.platform == "linux4":
  import os
  os.chdir("/storage/emulated/0/com.hipipal.qpyplus/scripts")

logger = ""
atexit.register(logging.shutdown)

if __name__ == '__main__':
  logging.Formatter.converter=time.gmtime
  logging._srcFile=None
  logging.logThreads=0
  logging.logProcesses=0
  logging.config.dictConfig("logging.dict")

  logger = logging.getLogger(__name__)

  logger.critical("kritischer Zustand!")
  logger.warning ("eine Warnung")
  logger.info("dies ist eine Information.")
  if logger.isEnabledFor(logging.DEBUG):
    logger.debug("debug")
  logging.log(logging.ERROR, "Fehler!")

  logging.shutdown()

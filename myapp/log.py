#-*-coding:utf-8;-*-
#qpy:3
#qpy:console
# erzeugt Montag, 13. Mai 2019 07:05 (C) 2019 von Leander Jedamus
# modifiziert Montag, 13. Mai 2019 09:37 von Leander Jedamus

from __future__ import print_function
import logging

def addFilter(logger):
  logger.addFilter(logging.Filter("dialogs"))
#  logger.addFilter(logging.Filter("__main__"))

# vim:ai sw=2 sts=4 expandtab


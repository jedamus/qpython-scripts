#!/usr/bin/env python
# coding=utf-8 -*- python -*-

# erzeugt Montag, 13. Mai 2019 23:39 (C) 2019 von Leander Jedamus
# modifiziert Montag, 13. Mai 2019 23:53 von Leander Jedamus

from __future__ import print_function
import logging
from random import choice

class ContextFilter(logging.Filter):
  """
  This is a filter which injects contextual information into the log.

  Rather than use actual contextual information, we just use random
  data in this demo.
  """

  USERS = ['leander', 'simone', 'helene']
  IPS   = ['123.231.231.123', '127.0.0.1', '192.168.2.1', '192.168.178.1']

  def filter(self, record):
    record.ip = choice(ContextFilter.IPS)
    record.user = choice(ContextFilter.USERS)
    return(True)

def main():
  levels = (logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR,
            logging.CRITICAL)
  
  logging.basicConfig(level=logging.DEBUG,
                      format='%(asctime)-15s %(name)-5s %(levelname)-8s IP: '
                      '%(ip)-15s %(user)-8s %(message)s')
  a1 = logging.getLogger('a.b.c')
  a2 = logging.getLogger('d.e.f')

  f = ContextFilter()
  a1.addFilter(f)
  a2.addFilter(f)

  a1.debug('A debug message')
  a1.info('An info message with %s', 'some parameters')
  for x in range(10):
    lvl = choice(levels)
    lvlname = logging.getLevelName(lvl)
    a2.log(lvl, 'A message at %s level with %d %s', lvlname, 2, 'parameters')

if __name__ == '__main__':
  main()
# vim:ai sw=2 sts=4 expandtab


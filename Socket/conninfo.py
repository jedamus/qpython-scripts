#!/usr/bin/env python
# coding=utf-8 -*- python -*-

# erzeugt Montag, 13. Mai 2019 23:09 (C) 2019 von Leander Jedamus
# modifiziert Montag, 13. Mai 2019 23:33 von Leander Jedamus

from __future__ import print_function
import logging

class ConnInfo:
  """
  an example class which shows how an abitrary class can be used as
  the 'extra' context information repository passed to a LoggerAdapter.
  """

  def __getitem__(self, name):
    """
    To allow this instance to look like a dict.
    """

    from random import choice
    if name == 'ip':
      result = choice(['127.0.0.1', '192.168.2.1'])
    elif name == 'user':
      result = choice(['leander', 'simone', 'helene'])
    else:
      result = self.__dict__.get(name, '?')
    return(result)

  def __iter__(self):
    """
    To allow iteration over keys, whcih will be merged into
    the LogRecord dict before formatting and output.
    """

    keys = ['ip', 'user']
    keys.extend(self.__dict__.keys())
    return(keys.__iter__())

def main():
  from random import choice
  levels = (logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR,
            logging.CRITICAL)
  a1 = logging.LoggerAdapter(logging.getLogger('a.b.c'),
                             { 'ip': '123.231.231.123', 'user': 'simone' })
  logging.basicConfig(level=logging.DEBUG,
                      format='%(asctime)-15s %(name)-5s %(levelname)-8s IP:'
                      ' %(ip)-15s %(user)-8s %(message)s')
  a1.debug('A debug message')
  a1.info('An info message with %s', 'some parameters')
  a2 = logging.LoggerAdapter(logging.getLogger('d.e.f'), ConnInfo())
  for x in range(10):
    lvl = choice(levels)
    lvlname = logging.getLevelName(lvl)
    a2.log(lvl, 'A message at %s level with %d %s', lvlname, 2, 'parameters')

if __name__ == '__main__':
  main()

# vim:ai sw=2 sts=4 expandtab


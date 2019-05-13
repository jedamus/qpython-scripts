#!/usr/bin/env python
# coding=utf-8 -*- python -*-

# erzeugt Montag, 13. Mai 2019 22:06 (C) 2019 von Leander Jedamus
# modifiziert Montag, 13. Mai 2019 22:40 von Leander Jedamus

from __future__ import print_function
import logging
import logging.handlers

if __name__ == '__main__':
  rootLogger = logging.getLogger('')
  rootLogger.setLevel(logging.DEBUG)
  socketHandler = logging.handlers.SocketHandler('localhost',
                    logging.handlers.DEFAULT_TCP_LOGGING_PORT)
  rootLogger.addHandler(socketHandler)

  logging.info('test the root logger')

  logger1 = logging.getLogger('myapp.area1')
  logger2 = logging.getLogger('myapp.area2')

  logger1.debug('test the logger1')
  logger1.info('info test the logger1')
  logger2.warning('warning the logger2')
  logger2.error('error the logger2')
# vim:ai sw=2 sts=4 expandtab


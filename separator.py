#-*-coding:utf8;-*-
#qpy:2
#qpy:console

from __future__ import print_function

faktor = 10

def anfang():
  print('----8<' * faktor,'----',sep='')

def trenner():
  print('------' * faktor,'----',sep='')

def ende():
  print('---->8' * faktor,'----',sep='')

if __name__ == '__main__':
  anfang()
  trenner()
  ende()
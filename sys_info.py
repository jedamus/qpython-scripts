#!/usr/bin/env python3
#-*-coding:utf8;-*-
#qpy:2
#qpy:console
# modifiziert Mittwoch, 29. Mai 2019 06:30 von Leander Jedamus

from __future__ import print_function
import sys
import os
import separator as sep

if __name__ == '__main__':
    sep.faktor = 11
    
    sep.anfang()
    print('sys.version_info=',end='')
    v = sys.version_info
    print(v.major,v.minor,sep='.')
    sep.trenner()
    
    print('sys.platform=',end='')
    print(sys.platform)
    sep.trenner()
    
    print('sys.path=')
    for p in sys.path:
        print('\n',p,sep='')
    sep.trenner()
    
    print('os.environ=',end='')
    env = os.environ
    for e in env:
        print('\n',e,': ',env[e],sep='',end='\n')
    sep.ende()
 

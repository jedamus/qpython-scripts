#!/usr/bin/env python
# coding: utf-8
# ä
# erzeugt Dienstag, 30. April 2019 13:29 (C) 2019 von Leander Jedamus
# modifiziert Dienstag, 30. April 2019 18:10 von Leander Jedamus

import datetime
from get_datum import get_datum

today = datetime.datetime.today()
datum = today
days = 4
day1 = datetime.timedelta (days=1)

import sys
import locale
if (sys.platform in ["linux", "linux2", "darwin"]):
  locale.setlocale(locale.LC_ALL, "de_DE.UTF-8")

while datum.weekday() > 4:
    datum += day1
for i in range(days):
    datum += day1
    if datum.weekday() > 4:
        datum += day1 + day1
print(get_datum(datum,"%A, der %d. %B %Y"))

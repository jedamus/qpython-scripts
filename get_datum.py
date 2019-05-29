#!/usr/bin/env python
# coding=utf-8 -*- python -*-

# erzeugt Dienstag, 30. April 2019 13:29 (C) 2019 von Leander Jedamus
# modifiziert Dienstag, 30. April 2019 13:36 von Leander Jedamus

import sys

def get_datum(datum,ds):
    s = datum.strftime(ds)
    if sys.platform in ["linux4","ios"]:
      months = ["January", "February", "March", "April", "May",
                "June", "July", "August", "September", "October",
                "November", "December"]
      monate = ["Januar", "Februar", "März", "April", "Mai",
                "Juni", "Juli", "August", "September", "Oktober",
                "November", "Dezember"];
      for i in range(0,12):
        #print(months[i], " = ", monate[i])
        s = s.replace(months[i], monate[i])
      days = ["Sunday", "Monday", "Tuesday", "Wednesday",
              "Thursday", "Friday", "Saturday"]
      tage = ["Sonntag", "Montag", "Dienstag", "Mittwoch",
              "Donnerstag", "Freitag", "Samstag"]
      for i in range(0,7):
        #print(days[i], " = ", tage[i])
        s = s.replace(days[i], tage[i])
    return s

# vim:ai sw=2 sts=4 expandtab


#!/usr/bin/env python
# coding: utf-8
# qpy:2
# ä
# modifiziert Dienstag, 30. April 2019 12:15 von Leander Jedamus

from __future__ import print_function
import locale
import datetime
import sys

def calc_easter(year):
    "Returns Easter as a date object."
    a = year % 19
    b = year // 100
    c = year % 100
    d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
    e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
    f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
    month = f // 31
    day = f % 31 + 1
    
    return datetime.date(year, month, day)

def get_datum(datum,ds):
    s = datum.strftime(ds)
    if sys.platform == "linux4":
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

def output1(ostern, ds, tage, name):
    days = datetime.timedelta(days=tage)
    datum = ostern + days
    print(name + " ist am " + get_datum(datum,ds), end=". ")

    
def output2(heute, ostern, tage, name):
    days = datetime.timedelta(days=tage)
    datum = ostern + days
    days = datum - heute
    days = days.days
    if days < 0:
        days = days * -1
        s1 = "war vor"
        zurueck = True
    else:
        s1 = "ist in"
        zurueck = False
    if days == 0:
        s = "Heute ist " + name
    elif days == 1:
        if zurueck:
            s = "Gestern war " + name
        else:
            s = "Morgen ist " + name
    elif days == 2:
        if zurueck:
            s = "Vorgestern war " + name
        else:
            s = "Übermorgen ist " + name
    else:
        s = name + " " + s1 + " {d:d} Tagen".format(d=days)
        
    print(s, end=". ")

    
def output(heute, ostern, ds, tage, name):
    output1(ostern, ds, tage, name)
    print()
    output2(heute, ostern, tage, name)
    print()


ds = "%A, der %d. %B %Y"
if sys.platform == "linux2":
  locale.setlocale(locale.LC_ALL, "de_DE.UTF-8")
    
today = datetime.date.today()
print("Heute ist " + get_datum(today,ds) + ".")
year = today.year
#year = 2016

ostern = calc_easter(year)
output(today, ostern, ds,   0, "Ostersonntag")
output(today, ostern, ds,  -2, "Karfreitag")
output(today, ostern, ds, -48, "Rosenmontag")
output(today, ostern, ds,  49, "Pfingstsonntag")

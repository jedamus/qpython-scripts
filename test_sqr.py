#!/usr/bin/python2
#-*-coding:utf8;-*-
#qpy:2
#qpy:console
# modifiziert Dienstag, 11. Juni 2019 16:23 von Leander Jedamus
# modifiziert Mittwoch, 01. Mai 2019 01:01 von Leander Jedamus
# erzeugt Dienstag, 30. April 2019 17:54 (C) 2019 von Leander Jedamus
# modifiziert Dienstag, 30. April 2019 17:51 von Leander Jedamus

from __future__ import print_function
import sys
import os
import unittest
import sqr

file = sys.stderr
class SqrTest(unittest.TestCase):

  def setUp(self):
    print('Erzeuge Testdaten. ', sep='', end='', file=file)
  
  def tearDown(self):
    print('Lösche Testdaten. ', sep='', end='', file=file)
    try:
      os.remove('not_existing.txt')
    except: pass

  def testBerechnung1(self):
    msg = 'Werte sind unterschiedlich.'
    self.assertEqual(sqr.sqr(0), 0, msg)
    self.assertEqual(sqr.sqr(2), 4, msg)
    self.assertEqual(sqr.sqr(10), 100, msg)

  def testBerechnung2(self):
    self.assertEqual(sqr.sqr(-2), 4)
    self.assertEqual(sqr.sqr(-10), 100)
    
def PrintAusgabe():
  s = ['Äpfel', 'Birnen', 'Kirschen', 'Pflaumen']
  for obst in s:
    print (obst, end=' oder ' if obst != s[-1] else '\n')
    
if __name__ == '__main__':
  # unittest.main()
  suite = unittest.TestSuite()
  test1 = SqrTest('testBerechnung1')
  test2 = SqrTest('testBerechnung2')
  suite.addTests((test1, test2))
  testrunner = unittest.TextTestRunner(verbosity=2, stream=file)
  testrunner.run(suite)
  print("-" * 70)
  PrintAusgabe()
  
# setUp() wird vor jedem Aufruf einer der Testmethoden gerufen und 
# kann somit für den Test benötigten Initialisierungscode enthalten.
# Eine in der Methode setUp() geworfenen Exception wird als Fehler
# in den Testbericht eingetragen und der Test abgebrochen.
#
# tearDown() wird nach jedem Aufruf einer der Testmethoden gerufen
# und kann somit abschließenden Code enthalten. Eine in der Methode
# tearDown() geworfene Exception wird als Fehler in den Testbericht
# eingetragen.

# Die Methoden verfügen alle über den optionalen Parameter msg, für
# den eine Fehlerbeschreibung angegeben werden kann, die im Falle
# eines fehlschlagenden Tests ausgegeben wird.

# assert_(expr [, msg])              expr is True
# assertEqual(first, second [, msg]) first == second
# assertNotEqual                     first != second
# failUnless(expr, [, msg])          wie assert_()
# failUnlessEqual (first, second [, msg]) wie assertEqual()
# assertTrue(expr [, msg])           bool(expr) is True
# assertFalse                        bool(expr) is False
# assertIs(first, second, msg)       first is second
# assertIsNot                        first is not second
# assertIsNone(expr, msg)            expr is None
# assertIsNotNone                    expr is not None
# assertIn(first, second, msg)       first in second
# assertNotIn                        first not in
# assertIsInstance(obj, cls, msg)    isinstance(obj, cls)
# assertNotIsInstance                not isinstance(obj, cls)
# assertRaises(exception, callable, *args, **kwds)
#    callable(*args, **kwds) wirft exception-Exception
# assertRaisesRegex(exception, regex, callable, *args, **kwds)
#    wie assertRaises, die Fehlermeldung muß aber zusätzlich noch
#    auf den regulären Ausdruck regex passen. Dieser kann als String
#    oder in Form eines RE-Objekts (s. S. 432) übergeben werden.
# assertWarns(warning, callable, *args, **kwds) wie assertRaises,
#                                               nur für Warnungen
# assertWarnsRegex                   wie assertRaisesRegex, nur für
#                                    Warnungen
# assertAlmostEqual(first, second [, places [, msg [, delta]]]
#   round(first - second, places) == 0 bzw.
#   abs(first - second) < delta
# assertNotAlmostEqual
#   round (first - second) != 0 bzw.
#   abs(first - second) >= delta
# assertGreater(first, second, [, msg]) first > second
# assertGreaterEqual                    first >= second
# assertLess                            first < second
# assertLessEqual                       first <= second
# assertRegex(text, regex, [, msg])     der reguläre Ausdruck regex
#    paßt auf den String text. der reguläre Ausdruck kann als String
#    oder RE-Objekt übergeben werden.
# assertNotRegex                        der reguläre Ausdruck regex
#    paßt nicht auf den String text.
# assertCountEqual(first, second [, msg]) Die Sequenzen first und
#    second enthalten die gleichen Elemente, unabhängig von deren
#    Reihenfolge.
#
# Die Methoden assertRaises, assertRaisesRegex, assertWarns und
# assertWarnsRegex können auch ohne die Parameter callable, *args
# und **kwds aufgerufen werden. In diesem Fall geben sie ein
# Kontextobjekt zurück, das mit einer with-Anweisung verwendet
# werden kann:
#
# with self.assertRaises (TypeError):
#   <Code>
#
# der Vorteil dieser Schreibweise ist, daß der zu testende Code
# nicht extra in eine Funktion gekapselt werden muß.

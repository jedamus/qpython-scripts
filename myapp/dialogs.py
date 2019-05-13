#-*-coding:utf-8;-*-
#qpy:3
#qpy:console
# erzeugt Mittwoch, 22. Juli 2015 17:05 von Leander Jedamus
# modifiziert Montag, 13. Mai 2019 18:29 von Leander Jedamus
# modifiziert Montag, 27. Juli 2015 13:04 von Leander Jedamus
# modifiziert Samstag, 25. Juli 2015 20:43 von Leander Jedamus
# modifiziert Freitag, 24. Juli 2015 20:24 von Leander Jedamus
# modifiziert Mittwoch, 22. Juli 2015 18:45 von Leander Jedamus

import time
import logging
import log

logger = logging.getLogger(__name__)
log.addFilter(logger)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.NullHandler())

def addHandler(handler):
  logger.removeHandler(logging.NullHandler())
  logger.addHandler(handler)

email = ""

def getEmailBody():
    return email

def t(droid,speak,send,*seq):
  if logger.isEnabledFor(logging.DEBUG):
    logger.debug("t")

  global email
  s = ' '.join(seq)
  s2 = ' '.join(seq).encode('utf-8')
  if speak:
    droid.ttsSpeak(s)
    if logger.isEnabledFor(logging.DEBUG):
      logger.debug("speaking: " + s)
  if send:
    email = email + s2 + "\n"
  return s
  
def Speaking(droid,speak,*seq):
  if logger.isEnabledFor(logging.DEBUG):
    logger.debug("In dialogs.Speaking")

  if speak:
    t = 0
    for s in seq:
      time.sleep(t)
      droid.ttsSpeak(s)
      if logger.isEnabledFor(logging.DEBUG):
        logger.debug("speaking: " + s)
      t = 1

def ListDialog(droid,title,list,cancel="Cancel"):
  if logger.isEnabledFor(logging.DEBUG):
    logger.debug("In dialogs.ListDialog")

  droid.dialogCreateAlert(title, '')
  droid.dialogSetItems(list)
  droid.dialogSetNegativeButtonText(cancel)
  droid.dialogShow()
  resp = droid.dialogGetResponse()
  droid.dialogDismiss()
  if resp.result.has_key('item'):
    return resp.result['item']
  else:
    return None
    
def YesNoDialog(droid,speak,title,question,yes,no):
  if logger.isEnabledFor(logging.DEBUG):
    logger.debug("In dialogs.YesNoDialog")

  droid.dialogCreateAlert(title,question)
  droid.dialogSetPositiveButtonText(yes)
  droid.dialogSetNegativeButtonText(no)
  Speaking(droid,speak,title,question)
  droid.dialogShow()
  response = droid.dialogGetResponse().result
  droid.dialogDismiss()
  return ('which' in response) and (response['which'] == 'positive')


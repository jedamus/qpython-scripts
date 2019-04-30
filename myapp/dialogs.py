#-*-coding:utf-8;-*-
#qpy:3
#qpy:console
# erzeugt Mittwoch, 22. Juli 2015 17:05 von Leander Jedamus
# modifiziert Montag, 27. Juli 2015 13:04 von Leander Jedamus
# modifiziert Samstag, 25. Juli 2015 20:43 von Leander Jedamus
# modifiziert Freitag, 24. Juli 2015 20:24 von Leander Jedamus
# modifiziert Mittwoch, 22. Juli 2015 18:45 von Leander Jedamus

import time

email = ""

def getEmailBody():
    return email

def t(droid,speak,send,*seq):
  global email
  s = ' '.join(seq).encode('utf-8')
  if speak: droid.ttsSpeak(s)
  if send: email = email + s + "\n"
  return s
  
def Speaking(droid,speak,*seq):
    if speak:
        t = 0
        for s in seq:
            time.sleep(t)
            droid.ttsSpeak(s)
            t = 1

def ListDialog(droid,title,list,cancel="Cancel"):
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
    droid.dialogCreateAlert(title,question)
    droid.dialogSetPositiveButtonText(yes)
    droid.dialogSetNegativeButtonText(no)
    Speaking(droid,speak,title,question)
    droid.dialogShow()
    response = droid.dialogGetResponse().result
    droid.dialogDismiss()
    return ('which' in response) and (response['which'] == 'positive')

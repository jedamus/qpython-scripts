#-*-coding:utf8;-*-
#qpy:2
#qpy:console

import time

try:
    import androidhelper as android
except ImportError:
    import android
    
hallo = "Hallo"
whd   = "Wie heißt du?"

droid = android.Android()
droid.ttsSpeak(hallo)
time.sleep(1)
droid.ttsSpeak(whd)
response = droid.dialogGetInput(hallo,whd)
name = response.result
if name:
    message = "Hallo, %s!" % name
else:
    message = "Du bist sehr unhöflich, Benutzer!"
droid.ttsSpeak(message)
droid.makeToast(message)
time.sleep(2)
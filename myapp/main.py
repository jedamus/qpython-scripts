#-*-coding:utf-8;-*-
#qpy:3
#qpy:console
# erzeugt Mittwoch, 22. Juli 2015 17:05 von Leander Jedamus
# modifiziert Montag, 13. Mai 2019 10:06 von Leander Jedamus
# modifiziert Mittwoch, 01. Mai 2019 01:51 von Leander Jedamus
# modifiziert Montag, 27. Juli 2015 13:04 von Leander Jedamus
# modifiziert Samstag, 25. Juli 2015 20:43 von Leander Jedamus
# modifiziert Freitag, 24. Juli 2015 20:24 von Leander Jedamus
# modifiziert Mittwoch, 22. Juli 2015 18:45 von Leander Jedamus

from __future__ import print_function
import atexit
import logging
import sys
import os
import gettext
import time
from dialogs import ListDialog, YesNoDialog, t, Speaking, getEmailBody
import dialogs
from xmls import xml
import log

try:
    import androidhelper as android
except ImportError:
    import android

os.chdir("/storage/emulated/0/com.hipipal.qpyplus/projects/myapp")
    
logger = ""
atexit.register(logging.shutdown)

languages = ["English","Deutsch"]
short_languages = ["en","de"]
        
# create the droid
droid = android.Android()
 
handler1 = logging.StreamHandler(sys.stdout)
handler2 = logging.FileHandler("myapp.log","w","utf-8",True)

logging.Formatter.converter=time.gmtime
frm = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s",
                        "%d.%m.%Y %H:%M:%S %Z")

handler1.setFormatter(frm)
handler2.setFormatter(frm)

logger = logging.getLogger(__name__)
#logger.addHandler(handler1)
logger.addHandler(handler2)
logger.setLevel(logging.DEBUG)

#dialogs.addHandler(handler1)
dialogs.addHandler(handler2)
log.addFilter(logger)

# user has to select language
lang_index = ListDialog(droid,"Select language",languages,"Cancel")
if lang_index == None:
    sys.exit(0)
else:
    # write selected language into environment, so gettext knows,
    # what language to choose
    os.environ["LANG"] = short_languages[lang_index]
    logger.debug("main: language = " + short_languages[lang_index]
                 + " (" + languages[lang_index] + ")")
    
scriptpath = os.path.abspath(os.path.dirname(sys.argv[0]))  
try:
    trans = gettext.translation("myapp", \
    	        os.path.join(scriptpath, "translate"))
    trans.install(unicode=True)
except IOError:
    def _ (s):
        return s
        
#sys.exit(0)

# """

speak = YesNoDialog(droid,False,_("Text-to-speech?"),
  _("Do you want speech output?"),_("Yes"),_("No"))

response = YesNoDialog(droid,speak,_("Install Packages?"),
	 _("You may want to use WiFi for this."),
	 _("Yes"),_("No"))
if not response: sys.exit()
 
# Now the checks are done, create and render the new progress bar dialog,
# setting a title, message and a maximum progress of 10
s1 = _("Installing Packages...")
s2 = _("This should just take a moment.")
droid.dialogCreateHorizontalProgress(s1,s2,10)
 
# Render the dialog
Speaking(droid,speak,s1,s2)
droid.dialogShow()
 
# Now do the installation, updating the progress bar along the way...
 
# Install each of the packages, incrementing the progress bar on each
progress = 0
for i in range(10):
    time.sleep(1)
    progress += 1
    droid.dialogSetCurrentProgress(progress)
    
time.sleep(2)

# Tidy up and exit
droid.dialogDismiss()

# """

# sys.exit(0)

entries = [_("19 percent"), _("16 percent"), _("7 percent")]
entryValues = [ 19, 16, 7]


droid.fullShow(xml)
droid.fullSetList("spinner1", entries)
droid.fullSetProperty("textView1","text",_("Please input data here:"))
droid.fullSetProperty("button1","text",_("Send data"))
droid.fullSetProperty("textView2","text",_("First name"))
droid.fullSetProperty("textView3","text",_("Last name"))
droid.fullSetProperty("textView4","text",_("street"))
droid.fullSetProperty("textView5","text",_("nr."))
droid.fullSetProperty("textView6","text",_("postcode"))
droid.fullSetProperty("textView7","text",_("town"))
droid.fullSetProperty("textView8","text",_("telephone"))
droid.fullSetProperty("editText1","text",_("testing 123"))

# addOptionsMenuItem takes two to four arguments:
# item_label, event_name, [event_data], [icon_name]
       
# The following calls add three items to the options menu...
droid.addOptionsMenuItem(_("Do A"), "a_event", _("Some event data."))
droid.addOptionsMenuItem(_("Do B"), "b_event", _("Some other data."))
droid.addOptionsMenuItem(_("Quit"), "kill", None, "ic_menu_revert")

while True:
    # Block until an event happens, then grab the result
    res = droid.eventWait().result
    
    #print(res)
    
    # If it's a kill event, exit the event loop
    if res['name'] == 'kill':
        resp = droid.fullQuery().result
        droid.fullDismiss()
        send = YesNoDialog(droid,speak,_("Send as email?"),
          _("Do you want to send data as email?"),
          _("Yes"),_("No"))
        editText1 = resp['editText1']
        vorname = resp['vorname']
        nachname = resp['nachname']
        strasse = resp['strasse']
        nr = resp['nr']
        plz = resp['plz']
        ort = resp['ort']
        telefon = resp['telefon']
        spinner1 = resp['spinner1']
        print("\n-----------------\n")
        print(t(droid,speak,send,_("firstname:"),vorname['text']))
        print(t(droid,speak,send,_("lastname:"),nachname['text']))
        print(t(droid,speak,send,_("street:"),strasse['text']))
        print(t(droid,speak,send,_("nr.:"),nr['text']))
        print(t(droid,speak,send,_("postcode:"),plz['text']))
        print(t(droid,speak,send,_("town:"),ort['text']))
        print(t(droid,speak,send,_("telephone:"),telefon['text']))
        #print(spinner1)
        print("\n-----------------\n")
        print(t(droid,speak,send,_("data:"),editText1['text']))
        index = int(spinner1['selectedItemPosition'])
        print(t(droid,speak,send,entries[index] + " = " +
        	  str(entryValues[index]) + " %"))
        print("\n-----------------\n")
        if send:
            recipients = ["ljedamus@web.de",
                "ljedamus@googlemail.com",
                _("other")]
            subject = _("send data from qpython")
        
            recipient_index = ListDialog(droid,
            	    _("Select recipient"),recipients,_("Cancel"))
            if recipient_index != None:
                to = recipients[recipient_index]
                if to == _("other"):
                    result = droid.dialogGetInput(
                    	_("Email address"),
                    	_("Input email adress")).result
                    if result == None:
                        break
                    else:
                  	      to = result
                droid.sendEmail(to,subject,getEmailBody())
        #print(resp)
        break
 
    # Otherwise, print the event data
    if (res['name'] == 'a_event') or (res ['name'] == 'b_event'):
        print(res['data'])
	if res['name'] == 'a_event':
	    droid.fullSetProperty("vorname","text","Leander")
	    droid.fullSetProperty("nachname","text","Jedamus")
	    droid.fullSetProperty("strasse","text","Lainsteiner Str.")
	    droid.fullSetProperty("nr","text","12")
	    droid.fullSetProperty("plz","text","56736")
	    droid.fullSetProperty("ort","text","Kottenheim")
	    droid.fullSetProperty("telefon","text","+49 2651 41563")
    elif res['data'].has_key('id'):
	if res['data']['id'] == "button1":
          droid.fullSetProperty("button1","textColor","#ffffff")
          droid.fullSetProperty("button1","background","#000000")
	    
 

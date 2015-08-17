#-*-coding:utf-8;-*-
#qpy:3
#qpy:console
# erzeugt Mittwoch, 22. Juli 2015 17:05 von Leander Jedamus
# modifiziert Freitag, 24. Juli 2015 20:24 von Leander Jedamus
# modifiziert Mittwoch, 22. Juli 2015 18:45 von Leander Jedamus

import sys
import os
import gettext

try:
    import androidhelper as android
except ImportError:
    import android
    
xml = """<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
android:layout_width="match_parent"
android:layout_height="match_parent"
android:orientation="vertical" >

<TextView
    android:id="@+id/textView1"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:layout_alignParentTop="true"
    android:layout_centerHorizontal="true"
    android:layout_marginTop="60dp"
    android:textSize="18sp"
    android:textColor="#4169E1"
    android:text="Static Switch" />

<Switch
    android:id="@+id/switch1"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:layout_centerInParent="true"
    android:text="Switch" />

</LinearLayout>

"""
    
def dialog(droid,title, list):
    '''display dialog with list of files/folders title
    allowing user to select any item or click Cancel 
    get user input and return selected index or None
    '''

    droid.dialogCreateAlert(title, '')
    droid.dialogSetItems(list)
    droid.dialogSetNegativeButtonText('Cancel')
    droid.dialogShow()
    resp = droid.dialogGetResponse()
    droid.dialogDismiss()
    if resp.result.has_key('item'):
        return resp.result['item']
    else:
        return None
        
# create the droid
droid = android.Android()
 
# user has to select language
language = dialog(droid,'Select language',["English","Deutsch"])
if language == None:
    sys.exit(0)
elif language == 0:
    lang = "en"
else:
    lang = "de"
    
# write selected language into environment, so gettext knows,
# what language to choose 
os.environ["LANG"] = lang

scriptpath = os.path.abspath(os.path.dirname(sys.argv[0]))  
try:
    trans = gettext.translation("installer.py", \
    	        os.path.join(scriptpath, "translate"))
    trans.install(unicode=True)
except IOError:
    def _ (s):
        return s

# Create an alert, setting a title and message
droid.dialogCreateAlert(
    _('Install Packages?'),
    _('You may want to use WiFi for this.')
)
 
# Set up a couple of buttons
droid.dialogSetPositiveButtonText(_('Yes'))
droid.dialogSetNegativeButtonText(_('No'))
 
# Now render the dialog to the user
droid.dialogShow()
 
# Get the result and dismiss the dialog
response = droid.dialogGetResponse().result
droid.dialogDismiss()
 
# Check to see if the user has pressed a button, as users can dismiss
# dialogs, and check if it was the positive one, otherwise we're done
if not 'which' in response or response['which'] != 'positive': sys.exit()
 
# Now the checks are done, create and render the new progress bar dialog,
# setting a title, message and a maximum progress of 10
droid.dialogCreateHorizontalProgress(
    _('Installing Packages...'),
    _('This should just take a moment.'),
    10
)
 
# Render the dialog
droid.dialogShow()
 
# Now do the installation, updating the progress bar along the way...
 
# Import a couple of parsimonyms
#import some_package_installing_function as install
#import some_list_of_packages as packages
import time

# Install each of the packages, incrementing the progress bar on each
progress = 0
for i in range(10):
    time.sleep(1)
    progress += 1
    droid.dialogSetCurrentProgress(progress)
    
time.sleep(3)

# Tidy up and exit
droid.dialogDismiss()

# sys.exit(0)

droid.fullShow(xml,"Beispiel XML zum testen der Funktionen")

# addOptionsMenuItem takes two to four arguments:
# item_label, event_name, [event_data], [icon_name]
       
# The following calls add three items to the options menu...
droid.addOptionsMenuItem('Do A', 'a_event', _('Some event data.'))
droid.addOptionsMenuItem('Do B', 'b_event', _('Some other data.'))
droid.addOptionsMenuItem('Quit', 'kill', None, 'ic_menu_revert')

while True:
    # Block until an event happens, then grab the result
    res = droid.eventWait().result
    
    # If it's a kill event, exit the event loop
    if res['name'] == 'kill':
        droid.fullDismiss()
        break
 
    # Otherwise, print the event data
    print(res['data'])
 

#-*-coding:utf-8;-*-
#qpy:3
#qpy:console
# erzeugt Mittwoch, 22. Juli 2015 17:05 von Leander Jedamus
# modifiziert Montag, 27. Juli 2015 13:04 von Leander Jedamus
# modifiziert Samstag, 25. Juli 2015 20:43 von Leander Jedamus
# modifiziert Freitag, 24. Juli 2015 20:24 von Leander Jedamus
# modifiziert Mittwoch, 22. Juli 2015 18:45 von Leander Jedamus

xml = '''<?xml version="1.0" encoding="utf-8"?>

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
    android:text="" />

  <EditText
    android:id="@+id/editText1"
    android:layout_alignParentTop="true"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:text="@id/testtext" />
    
  <Button
    android:id="@+id/button1"
    android:layout_alignParentTop="true"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:textColor="#121212"
    android:text="" />

  <Spinner android:id="@+id/spinner1"
    android:layout_alignParentTop="true"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:drawSelectorOnTop="true"
    android:entries=""
    android:entryValues="" />

  <LinearLayout
    android:layout_width="fill_parent"
    android:layout_height="wrap_content"
    android:weightSum="10"
    android:layout_alignParentTop="true"
    android:orientation="horizontal" >
    
    <TextView
      android:id="@+id/textView2"
      android:layout_width="wrap_content"
      android:layout_height="wrap_content"
      android:text="" />

    <EditText
        android:id="@+id/vorname"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="" />
  </LinearLayout>

  <LinearLayout
    android:layout_alignParentTop="true"
    android:layout_height="wrap_content"
    android:weightSum="10"
    android:layout_width="fill_parent"
    android:orientation="horizontal" >
    
    <TextView
      android:id="@+id/textView3"
      android:layout_width="wrap_content"
      android:layout_height="wrap_content"
      android:text="" />

    <EditText
        android:id="@+id/nachname"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="" />
  </LinearLayout>

  <LinearLayout
    android:layout_alignParentTop="true"
    android:layout_height="wrap_content"
    android:weightSum="10"
    android:layout_width="fill_parent"
    android:orientation="horizontal" >
    
    <TextView
      android:id="@+id/textView4"
      android:layout_width="wrap_content"
      android:layout_height="wrap_content"
      android:text="" />

    <EditText
        android:id="@+id/strasse"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="" />
  </LinearLayout>
    android:layout_alignParentTop="true"

  <LinearLayout
    android:layout_alignParentTop="true"
    android:layout_height="wrap_content"
    android:weightSum="10"
    android:layout_width="fill_parent"
    android:orientation="horizontal" >
    
    <TextView
      android:id="@+id/textView5"
      android:layout_width="wrap_content"
      android:layout_height="wrap_content"
      android:text="" />

    <EditText
        android:id="@+id/nr"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="" />
  </LinearLayout>

  <LinearLayout
    android:layout_alignParentTop="true"
    android:layout_height="wrap_content"
    android:weightSum="10"
    android:layout_width="fill_parent"
    android:orientation="horizontal" >
    
    <TextView
      android:id="@+id/textView6"
      android:layout_width="wrap_content"
      android:layout_height="wrap_content"
      android:text="" />

    <EditText
        android:id="@+id/plz"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="" />
  </LinearLayout>

  <LinearLayout
    android:layout_width="fill_parent"
    android:layout_height="wrap_content"
    android:weightSum="10"
    android:layout_alignParentTop="true"
    android:orientation="horizontal" >
    
    <TextView
      android:id="@+id/textView7"
      android:layout_width="wrap_content"
      android:layout_height="wrap_content"
      android:text="" />

    <EditText
        android:id="@+id/ort"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="" />
  </LinearLayout>

  <LinearLayout
    android:layout_width="fill_parent"
    android:layout_height="wrap_content"
    android:weightSum="10"
    android:layout_alignParentTop="true"
    android:orientation="horizontal" >
    
    <TextView
      android:id="@+id/textView8"
      android:layout_width="wrap_content"
      android:layout_height="wrap_content"
      android:text="" />

    <EditText
        android:id="@+id/telefon"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="" />
  </LinearLayout>

</LinearLayout>

'''


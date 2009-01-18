# -*- coding: utf-8 -*-
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html

# Based on changekeys.pl by Damien Elmes <anki@ichi2.net>
# Modified by Samson Melamed

# this plugin:
#  * allows you to show the answer for a card with the 'space' key even
#    when the 'show answer' button isn't focused
#  * binds 't' to change focus to the Q/A window, so you can use the
#    arrow keys to scroll around without needing the mouse.

# version 1: initial release

from PyQt4.QtCore import *
from ankiqt import mw

def newEventHandler(evt):
    if mw.state == "showQuestion":
        if evt.key() == Qt.Key_Space:
            evt.accept()
            return mw.moveToState("showAnswer")
    if mw.state == "showAnswer":
        key = unicode(evt.text())
        if key == "t":
            evt.accept()
            return mw.mainWin.mainText.setFocus()
    return oldEventHandler(evt)

oldEventHandler = mw.keyPressEvent
mw.keyPressEvent = newEventHandler

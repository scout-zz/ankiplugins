# -*- coding: utf-8 -*-
# Copyright: Samson Melamed
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
# Repository: http://github.com/scout/ankiplugins/tree/master

# This plugin adds Ctrl-g as a binding to regenerate the Japanese reading 
# field

# Many thanks to Damien Elmes for his assistance.

# version 1: initial release
# version 1.1: added plugin registration (3/21/09)
# version 2: now uses MeCab from the Japanese Support plugin (6/12/09)
#     requires Anki >= 0.9.9.8.2
# version 2.1: sets fact and deck as modified, to avoid data loss on sync
#     thanks to Qwertyu for the patch and ceba for the original report

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from japanese import reading as r
from anki.hooks import wrap
from ankiqt.ui import facteditor as fe
from ankiqt import mw

mw.registerPlugin("Regenerate Reading Field", 12)

def genReading(self):
    self.fact[r.dstField] = r.mecab.reading(self.fact[r.srcField])
    self.fact.setModified(textChanged=True)
    self.deck.setModified() 
    self.loadFields()

def newSetupFields(self):
    s = QShortcut(QKeySequence(_("Ctrl+g")), self.parent)
    s.connect(s, SIGNAL("activated()"), lambda self=self: genReading(self))

fe.FactEditor.setupFields = wrap(fe.FactEditor.setupFields, newSetupFields, 
        "after")
s = QShortcut(QKeySequence(_("Ctrl+g")), mw.editor.parent)
s.connect(s, SIGNAL("activated()"), lambda self=mw.editor: genReading(self))

# -*- coding: utf-8 -*-
# Copyright: Samson Melamed
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html

# this plugin adds Ctrl-g as a binding to regenerate the Japanese reading field

# version 1: initial release
# version 1.1: added plugin registration (3/21/09)

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from anki.features import japanese as j
from anki.hooks import wrap
from ankiqt.ui import facteditor as fe
from ankiqt import mw

mw.registerPlugin("Regenerate Reading Field", 12)

def genReading(self):
    self.fact[j.dstField] = j.kakasi.toFurigana(self.fact[j.srcField])
    self.loadFields()

def newSetupFields(self):
    s = QShortcut(QKeySequence(_("Ctrl+g")), self.parent)
    s.connect(s, SIGNAL("activated()"), lambda self=self: genReading(self))

fe.FactEditor.setupFields = wrap(fe.FactEditor.setupFields, newSetupFields, 
        "after")
s = QShortcut(QKeySequence(_("Ctrl+g")), mw.editor.parent)
s.connect(s, SIGNAL("activated()"), lambda self=mw.editor: genReading(self))

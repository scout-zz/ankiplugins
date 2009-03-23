# -*- coding: utf-8 -*-
# Copyright: Damien Elmes <anki@ichi2.net>
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html

# this plugin allows you to redefine the keys used to answer cards. it defines
# 'x' as a failed answer and 'y' as a correct answer.

# version 1: initial release
# version 1.1: added plugin registration (3/21/09)

from ankiqt.ui import view as v
from anki.hooks import wrap

from ankiqt import mw
mw.registerPlugin("Resize Images", 10)

def newClearWindow(self):
        self.write('''
<script type="text/javascript">
//<![CDATA[
var maxWidth = window.innerWidth-40;
window.onload = function(){
  var elements = document.getElementsByTagName("img");
    for(i=0;i<elements.length;i++){
        if(elements[i].width > maxWidth){
           elements[i].style.width = "100%";
        }
    }
}
//]]>
</script>''')

v.View.clearWindow = wrap(v.View.clearWindow, newClearWindow,
        "after")

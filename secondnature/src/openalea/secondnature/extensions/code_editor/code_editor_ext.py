# -*- python -*-
#
#       OpenAlea.Secondnature
#
#       Copyright 2006-2011 INRIA - CIRAD - INRA
#
#       File author(s): Daniel Barbeau <daniel.barbeau@sophia.inria.fr>
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
###############################################################################

__license__ = "CeCILL v2"
__revision__ = " $Id$ "

from openalea.secondnature.api import *

from openalea.core.node import NodeFactory
from openalea.core.compositenode import CompositeNodeFactory
from openalea.core.pkgmanager import PackageManager
from openalea.secondnature.urltools import file_url_to_path

import urllib2
import urlparse
import os.path as path
import inspect


class DT_Text(DataType):
    __name__        = "Text"
    __mimetypes__ = ["text/plain",
                     "application/x-qt-windows-mime;value=\"FileName\"",
                     NodeFactory.mimetype,
                     CompositeNodeFactory.mimetype]

    def __init__(self):
        DataType.__init__(self)
        self.pm = PackageManager()

    def new(self):
        text = ""
        name = self.__name__
        return Data(name, text, mimetype = "text/plain")

    def open_url(self, parsedUrl):
        url = parsedUrl.geturl()

        if parsedUrl.scheme == "oa":
            fac = self.pm.get_factory_from_url(parsedUrl)
            if isinstance(fac, CompositeNodeFactory):
                pkg  = self.pm.get_package_from_url(parsedUrl)[0]
                name = pkg.get_wralea_path()
            else:
                mod_name = fac.get_node_module()
                name =  inspect.getsourcefile(mod_name)
            f = open(name)
        elif parsedUrl.scheme == "file":
            name = file_url_to_path(url)
            #name = parsedUrl.path#.strip("/")
            f = open(name)
        else:
            f = urllib2.urlopen(url)
            name = parsedUrl.path
        text = f.read()
        f.close()

        return Data(name, text, mimetype="text/plain")




class CodeEditorFactory(AppletBase):
    __name__        = "CodeEditor.CodeEditor"

    def __init__(self):
        AppletBase.__init__(self)
        self.add_data_type(DT_Text())

    def get_applet_space(self, data):
        from openalea.visualea.scintilla_editor import ScintillaCodeEditor
        widget = ScintillaCodeEditor()
        widget.setText(data.obj)
        return LayoutSpace(widget)


# -- instantiate widget factories --
editor_f = CodeEditorFactory()

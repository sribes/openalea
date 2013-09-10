# -*- python -*-
#
#       OpenAlea.OALab: Multi-Paradigm GUI
#
#       Copyright 2013 INRIA - CIRAD - INRA
#
#       File author(s): Julien Coste <julien.coste@inria.fr>
#
#       File contributor(s):
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
###############################################################################
__revision__ = ""

from openalea.vpltk.qt import QtGui, QtCore
import webbrowser

class Help(QtGui.QWidget):
    """
    Widget which permit to display informations/help.
    Usefull in visualea.
    """
    def __init__(self):
        super(QtGui.QWidget, self).__init__() 
        
        actionHelpOpenAlea = QtGui.QAction(QtGui.QIcon(":/images/resources/openalealogo.png"),"OpenAlea", self)
        actionHelpGForge = QtGui.QAction(QtGui.QIcon(":/images/resources/gforge.png"),"Submit Bug", self)
        actionHelpTasks = QtGui.QAction(QtGui.QIcon(":/images/resources/gforge.png"),"See Tasks", self)
        actionHelpIntranet = QtGui.QAction(QtGui.QIcon(":/lpy_images/resources/lpy/logo.png"),"Intranet", self)
        
        QtCore.QObject.connect(actionHelpOpenAlea, QtCore.SIGNAL('triggered(bool)'),self.openWebsiteOpenalea)
        QtCore.QObject.connect(actionHelpGForge, QtCore.SIGNAL('triggered(bool)'),self.openOALabBugs)
        QtCore.QObject.connect(actionHelpTasks, QtCore.SIGNAL('triggered(bool)'),self.openOALabTasks)
        QtCore.QObject.connect(actionHelpIntranet, QtCore.SIGNAL('triggered(bool)'),self.openWebsiteIntranet)
        
        self._actions = ["Help",[["Website",actionHelpOpenAlea,0],
                                    ["Website",actionHelpGForge,0],
                                    ["Website",actionHelpTasks,0],
                                    ["Website",actionHelpIntranet,0]]]

    def actions(self):
        return self._actions
    
    def openWebsiteOpenalea(self):
        webbrowser.open('http://openalea.gforge.inria.fr/dokuwiki/doku.php')
        
    def openWebsiteIntranet(self):
        webbrowser.open('http://www-sop.inria.fr/virtualplants/wiki/doku.php?id=intranet:oalab')
        
    def openOALabBugs(self):
        webbrowser.open('https://gforge.inria.fr/tracker/?func=add&group_id=79&atid=13823')    
        
    def openOALabTasks(self):
        webbrowser.open('https://gforge.inria.fr/pm/task.php?group_project_id=6971&group_id=79&func=browse')
        

    def mainMenu(self):
        """
        :return: Name of menu tab to automatically set current when current widget
        begin current.
        """
        return "Help"  

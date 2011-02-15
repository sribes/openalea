#!/usr/bin/python

# -*- python -*-
#
#       OpenAlea.Visualea: OpenAlea graphical user interface
#
#       Copyright 2006-2009 INRIA - CIRAD - INRA
#
#       File author(s): Samuel Dufour-Kowalski <samuel.dufour@sophia.inria.fr>
#                       Christophe Pradal <christophe.prada@cirad.fr>
#
#       Distributed under the CeCILL v2 License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL_V2-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
################################################################################
"""Wrapper to start Visualea with correct environment variables"""

__license__ = "CeCILL v2"
__revision__ = " $Id$"

import os, sys



def level_one():
    envdict = os.environ
    os.execle(sys.executable, sys.executable, "-c",
              "import sys; from openalea.secondnature import main;sys.argv+="+str(sys.argv)+";main.level_two(sys.argv)",
              envdict)


def level_two(args):
    # Restore default signal handler for CTRL+C
    import signal


    from PyQt4 import QtGui
    from PyQt4 import QtCore

    from openalea.core import logger
    from openalea.core.session import Session
    from openalea.visualea.visualeagui import threadit
    from openalea.secondnature import mainwindow

    class SecondNature(QtGui.QApplication):
        """Materialisation of the Openalea application.
        Does the basic inits. The session is initialised
        in a thread. It is safe to use once the sessionStarted
        signal has been emitted."""


        def __init__(self, args):
            QtGui.QApplication.__init__(self, args)
            # -- reconfigure LoggerOffice to use Qt log handler and a file handler --
            logger.default_init(level=logger.ERROR, handlers=["qt"]) #TODO get level from settings
            logger.connect_loggers_to_handlers(logger.get_logger_names(), logger.get_handler_names())

            if __debug__:
                logger.set_global_logger_level(logger.DEBUG)
            else:
                logger.set_global_logger_level(logger.WARNING)

            # -- main window --
            self.win = mainwindow.MainWindow(None)
            self.win.statusBar().showMessage("Starting up! Please wait")
            self.win.setEnabled(False)
            self.win.show()

            # -- start session in a thread --
            self.sessionth = threadit(Session, self, self.__cb_session_thread_end)

        def __cb_session_thread_end(self):
            self.win.statusBar().clearMessage()
            self.win.setEnabled(True)

    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = SecondNature(args)
    return app.exec_()


if( __name__ == "__main__"):
    level_one()





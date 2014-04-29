
class PluginApplet(object):

    def __init__(self):
        self._applet = None

    def __call__(self, mainwindow):
        pass

    def _fill_menu(self, mainwindow, widget):
        # add actions to menu
        if widget.actions():
            for action in widget.actions():
                # Add actions in PanedMenu
                mainwindow.menu.addBtnByAction(*action)

        # Show/Hide in menu
        ## TODO
        """
        name = widget.windowTitle()
        btn = QtGui.QCheckBox(name, self)
        btn.setChecked(widget.isVisibleTo(self))
        btn.toggled.connect(widget.setVisible)
        # child.visibilityChanged.connect(btn.setChecked)
        action = [["View", "Show", btn, "smallwidget"], ]
        mainwindow.menu.addBtnByAction(action)"""

    def instance(self):
        return self._applet


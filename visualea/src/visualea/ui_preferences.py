# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/preferences.ui'
#
# Created: Fri Nov 19 16:49:21 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from openalea.vpltk.qt import qt

class Ui_Preferences(object):
    def setupUi(self, Preferences):
        Preferences.setObjectName("Preferences")
        Preferences.resize(596, 369)
        self.gridlayout = qt.QtGui.QGridLayout(Preferences)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")
        self.buttonBox = qt.QtGui.QDialogButtonBox(Preferences)
        self.buttonBox.setOrientation(qt.QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(qt.QtGui.QDialogButtonBox.Cancel|qt.QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridlayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.tabWidget = qt.QtGui.QTabWidget(Preferences)
        sizePolicy = qt.QtGui.QSizePolicy(qt.QtGui.QSizePolicy.Expanding, qt.QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = qt.QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.gridlayout1 = qt.QtGui.QGridLayout(self.tab)
        self.gridlayout1.setMargin(9)
        self.gridlayout1.setSpacing(6)
        self.gridlayout1.setObjectName("gridlayout1")
        self.label_2 = qt.QtGui.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridlayout1.addWidget(self.label_2, 0, 0, 1, 1)
        self.pathList = qt.QtGui.QListWidget(self.tab)
        self.pathList.setObjectName("pathList")
        self.gridlayout1.addWidget(self.pathList, 0, 1, 3, 1)
        self.addButton = qt.QtGui.QPushButton(self.tab)
        self.addButton.setObjectName("addButton")
        self.gridlayout1.addWidget(self.addButton, 1, 0, 1, 1)
        self.removeButton = qt.QtGui.QPushButton(self.tab)
        self.removeButton.setObjectName("removeButton")
        self.gridlayout1.addWidget(self.removeButton, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = qt.QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.vboxlayout = qt.QtGui.QVBoxLayout(self.tab_2)
        self.vboxlayout.setObjectName("vboxlayout")
        self.externalBool = qt.QtGui.QCheckBox(self.tab_2)
        self.externalBool.setObjectName("externalBool")
        self.vboxlayout.addWidget(self.externalBool)
        self.hboxlayout = qt.QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.label_4 = qt.QtGui.QLabel(self.tab_2)
        self.label_4.setObjectName("label_4")
        self.hboxlayout.addWidget(self.label_4)
        self.commandStr = qt.QtGui.QLineEdit(self.tab_2)
        self.commandStr.setObjectName("commandStr")
        self.hboxlayout.addWidget(self.commandStr)
        self.commandPath = qt.QtGui.QPushButton(self.tab_2)
        self.commandPath.setObjectName("commandPath")
        self.hboxlayout.addWidget(self.commandPath)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = qt.QtGui.QWidget()
        sizePolicy = qt.QtGui.QSizePolicy(qt.QtGui.QSizePolicy.Preferred, qt.QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_3.sizePolicy().hasHeightForWidth())
        self.tab_3.setSizePolicy(sizePolicy)
        self.tab_3.setObjectName("tab_3")
        self.gridlayout2 = qt.QtGui.QGridLayout(self.tab_3)
        self.gridlayout2.setSizeConstraint(qt.QtGui.QLayout.SetDefaultConstraint)
        self.gridlayout2.setMargin(9)
        self.gridlayout2.setSpacing(6)
        self.gridlayout2.setObjectName("gridlayout2")
        self.label = qt.QtGui.QLabel(self.tab_3)
        self.label.setObjectName("label")
        self.gridlayout2.addWidget(self.label, 0, 0, 1, 1)
        self.dbclickBox = qt.QtGui.QComboBox(self.tab_3)
        self.dbclickBox.setObjectName("dbclickBox")
        self.dbclickBox.addItem("")
        self.dbclickBox.addItem("")
        self.dbclickBox.addItem("")
        self.gridlayout2.addWidget(self.dbclickBox, 0, 1, 1, 1)
        self.comboBox = qt.QtGui.QComboBox(self.tab_3)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridlayout2.addWidget(self.comboBox, 1, 1, 1, 1)
        self.label_edge_style = qt.QtGui.QLabel(self.tab_3)
        self.label_edge_style.setObjectName("label_edge_style")
        self.gridlayout2.addWidget(self.label_edge_style, 1, 0, 1, 1)
        self.evalCue = qt.QtGui.QCheckBox(self.tab_3)
        self.evalCue.setObjectName("evalCue")
        self.gridlayout2.addWidget(self.evalCue, 2, 0, 1, 2)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridlayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Preferences)
        self.tabWidget.setCurrentIndex(2)
        qt.QtCore.QObject.connect(self.buttonBox, qt.QtCore.SIGNAL("accepted()"), Preferences.accept)
        qt.QtCore.QObject.connect(self.buttonBox, qt.QtCore.SIGNAL("rejected()"), Preferences.reject)
        qt.QtCore.QMetaObject.connectSlotsByName(Preferences)

    def retranslateUi(self, Preferences):
        Preferences.setWindowTitle(qt.QtGui.QApplication.translate("Preferences", "Preferences", None, qt.QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(qt.QtGui.QApplication.translate("Preferences", "Search Path", None, qt.QtGui.QApplication.UnicodeUTF8))
        self.addButton.setText(qt.QtGui.QApplication.translate("Preferences", "Add", None, qt.QtGui.QApplication.UnicodeUTF8))
        self.removeButton.setText(qt.QtGui.QApplication.translate("Preferences", "Remove", None, qt.QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), qt.QtGui.QApplication.translate("Preferences", "Package Manager", None, qt.QtGui.QApplication.UnicodeUTF8))
        self.externalBool.setText(qt.QtGui.QApplication.translate("Preferences", "Use External editor", None, qt.QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(qt.QtGui.QApplication.translate("Preferences", "Command", None, qt.QtGui.QApplication.UnicodeUTF8))
        self.commandPath.setText(qt.QtGui.QApplication.translate("Preferences", "...", None, qt.QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), qt.QtGui.QApplication.translate("Preferences", "Editor", None, qt.QtGui.QApplication.UnicodeUTF8))
        self.label.setText(qt.QtGui.QApplication.translate("Preferences", "Double click on item", None, qt.QtGui.QApplication.UnicodeUTF8))
        self.dbclickBox.setItemText(0, qt.QtGui.QApplication.translate("Preferences", "Run + Open (Default)", None, qt.QtGui.QApplication.UnicodeUTF8))
        self.dbclickBox.setItemText(1, qt.QtGui.QApplication.translate("Preferences", "Run", None, qt.QtGui.QApplication.UnicodeUTF8))
        self.dbclickBox.setItemText(2, qt.QtGui.QApplication.translate("Preferences", "Open", None, qt.QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, qt.QtGui.QApplication.translate("Preferences", "Spline (Default)", None, qt.QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, qt.QtGui.QApplication.translate("Preferences", "Polyline", None, qt.QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, qt.QtGui.QApplication.translate("Preferences", "Line", None, qt.QtGui.QApplication.UnicodeUTF8))
        self.label_edge_style.setText(qt.QtGui.QApplication.translate("Preferences", "Edge Style", None, qt.QtGui.QApplication.UnicodeUTF8))
        self.evalCue.setText(qt.QtGui.QApplication.translate("Preferences", "Show evaluation cue (side effect: slows down evaluation)", None, qt.QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), qt.QtGui.QApplication.translate("Preferences", "UI", None, qt.QtGui.QApplication.UnicodeUTF8))


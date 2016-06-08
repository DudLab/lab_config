#!/usr/bin/env python


from __future__ import print_function

import collections as col
import json
import os
import sys

try:
    from PySide import QtCore, QtGui, QtUiTools
except ImportError:
    from PyQt4 import QtCore, QtGui, uic

# Python 3 compatibility
try:
    xrange
except NameError:
    xrange = range

script_dir = os.path.dirname(os.path.abspath(__file__))

class Config(QtGui.QDialog):
    """
        Parses the configuration the user applies
    """

    def __init__(self, *args, **kwargs):
        super(Config, self).__init__(*args, **kwargs)
        self.modal = True

        self.config = col.OrderedDict()

        config_ui = os.path.join(
            script_dir,
            "config.ui"
        )
        try:
            self.ui = QtUiTools.QUiLoader().load(config_ui)
        except NameError:
            self.ui = uic.loadUi(config_ui)

        btn_box = self.ui.buttonBox
        ok_btn = btn_box.button(
                QtGui.QDialogButtonBox.Ok
        )
        ok_btn.clicked.connect(self.accept)

    def show(self):
        self.ui.show()
        self.ui.activateWindow()
        self.ui.raise_()

    def accept(self):
        table = self.ui.tableWidget
        for i in xrange(table.rowCount()):
            header_i = str(table.verticalHeaderItem(i).text())
            self.config[header_i] = ""
            item_i = table.item(0, i)
            if item_i:
                self.config[header_i] = str(item_i.text())

        filename = QtGui.QFileDialog.getSaveFileName(
                self,
                "Save file",
                "",
                "*.json"
        )
        # PySide gives us a tuple.
        # The actual filename is first
        if isinstance(filename, tuple):
            filename = filename[0]
        with open(filename, "w") as f:
            json.dump(self.config, f, indent=True)

def main(*argv):
    app = QtGui.QApplication(sys.argv)
    window = Config()
    window.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main(*sys.argv))

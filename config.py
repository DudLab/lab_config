#!/usr/bin/env python


from __future__ import print_function

from collections import OrderedDict
import json
import sys

from PyQt4 import QtCore, QtGui, uic


# Python 3 compatibility
try:
    xrange
except NameError:
    xrange = range


class Config(QtGui.QDialog):
    """
        Parses the configuration the user applies
    """

    def __init__(self):
        super(Config, self).__init__()

        self.config = OrderedDict()

        self.ui = uic.loadUi("config.ui")
        self.ui.show()

        btn = self.ui.buttonBox.button(
                QtGui.QDialogButtonBox.Ok
        )
        btn.clicked.connect(self.accept)

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
        with open(filename, "w") as f:
            json.dump(self.config, f, indent=True)

def main(*argv):
    app = QtGui.QApplication(sys.argv)
    window = Config()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main(*sys.argv))

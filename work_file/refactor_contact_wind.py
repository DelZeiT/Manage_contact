from PyQt5 import uic
from PyQt5.QtWidgets import *



def refactor_contact():
    Form5, Window5 = uic.loadUiType("refactor_window_ui.ui")
    window5 = Window5()
    form5 = Form5()
    form5.setupUi(window5)


    def test():
        print('f')

    form5.pushButton.clicked.connect(test)

    window5.exec_()


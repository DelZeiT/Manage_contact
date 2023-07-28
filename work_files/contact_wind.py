from PyQt5 import uic
from PyQt5.QtWidgets import *


# открывает окно контакт
def open_contact_window():
    Form4, Window4 = uic.loadUiType("disign_UI_UI/contact_window_ui.ui")
    window4 = Window4()
    form4 = Form4()
    form4.setupUi(window4)

    # редактор контакта
    def open_window_in_contact():
        Form5, Window5 = uic.loadUiType("disign_UI_UI/refactor_window_ui.ui")
        window5 = Window5()
        form5 = Form5()
        form5.setupUi(window5)
        window5.exec_()
    form4.pushButton.clicked.connect(open_window_in_contact)


    window4.exec_()


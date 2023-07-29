from PyQt5 import uic
from PyQt5.QtWidgets import *
from refactor_contact_wind import refactor_contact



# открывает окно контакт
def open_contact_window():
    Form4, Window4 = uic.loadUiType("contact_window_ui.ui")
    window4 = Window4()
    form4 = Form4()
    form4.setupUi(window4)

    # переменные с инфой о пользователе
    # form4.lineEdit_2.setText(lname)
    # form4.lineEdit.setText(fname)
    # form4.lineEdit_3.setText(number)
    # form4.lineEdit_4.setText(email)


    # редактор контакта
    def open_window_in_contact():
       refactor_contact()
    form4.pushButton.clicked.connect(open_window_in_contact)


    window4.exec_()


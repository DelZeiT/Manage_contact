from PyQt5 import uic
from PyQt5.QtWidgets import *
from backend_sql import Info_Contact

def open_add_window():
    Form2, Window2 = uic.loadUiType("add_window_ui.ui")
    window2 = Window2()
    form2 = Form2()
    form2.setupUi(window2)

    #кнопка добавление контакта
    def press_add_contact():
        info_contact = Info_Contact('3', 'Вася', '8999000', 'vasya@gmail.com')
        info_contact.sql_query()


    #кнопка отмены
    def press_cancel():
        window2.close()

    form2.pushButton.clicked.connect(press_add_contact)
    form2.pushButton_2.clicked.connect(press_cancel)

    window2.show()
    window2.exec_()















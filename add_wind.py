from PyQt5 import uic
from PyQt5.QtWidgets import *
from backend_sql import Info_Contact

# функция обработки всех кнопок в окне добавления контакта
def open_add_window():
    Form2, Window2 = uic.loadUiType("add_window_ui.ui")
    window2 = Window2()
    form2 = Form2()
    form2.setupUi(window2)


    #кнопка добавление контакта
    def press_add_contact():
        text_LName = form2.lineEdit.text()
        text_FName = form2.lineEdit_2.text()
        text_Number = form2.lineEdit_3.text()
        text_Email = form2.lineEdit_4.text()
        info_contact = Info_Contact(text_LName, text_FName, text_Number, text_Email)
        info_contact.sql_query()

    #кнопка отмены
    def press_cancel():
        window2.close()

    form2.pushButton.clicked.connect(press_add_contact)
    form2.pushButton_2.clicked.connect(press_cancel)

    window2.show()
    window2.exec_()















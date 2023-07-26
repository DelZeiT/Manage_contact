from PyQt5 import uic
from PyQt5.QtWidgets import *

Form, Window = uic.loadUiType("main_window_ui.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()


# функция открывания окна для добавления контакта
def open_add_window():
    Form2, Window2 = uic.loadUiType("add_window_ui.ui")
    app2 = QApplication([])
    window2 = Window2()
    form2 = Form2()
    form2.setupUi(window2)
    window2.show()
    window2.exec_()


form.pushButton.clicked.connect(open_add_window)


# функция открывания окна для удаления контакта
def open_delete_window():
    pass


form.pushButton_2.clicked.connect(open_add_window)


app.exec()

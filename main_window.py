from PyQt5 import uic
from PyQt5.QtWidgets import *

# from add_window_py import AddWindow

Form, Window = uic.loadUiType("main_window_ui.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()


# функция открывания окна для добавления контакта
def open_add_window():
    pass


form.pushButton.clicked.connect(open_add_window)


# функция открывания окна для удаления контакта
def open_delete_window():
    pass


form.pushButton_2.clicked.connect(open_add_window)


app.exec()

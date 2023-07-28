from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from add_wind import open_add_window

Form, Window = uic.loadUiType("main_window_ui2.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()


# функция открывания окна для добавления контакта.
def start_add_window():
    open_add_window()


form.pushButton.clicked.connect(open_add_window)


def add_new_button():
    list_widget = form.listWidget
    new_button = QPushButton("Новая кнопка")
    new_button.setFixedSize(120, 40)

    new_button.setStyleSheet("text-align: left; padding-left: 10px;")

    list_widget_item = QListWidgetItem()
    list_widget_item.setSizeHint(new_button.sizeHint())
    list_widget.addItem(list_widget_item)
    list_widget.setItemWidget(list_widget_item, new_button)


form.pushButton_3.clicked.connect(add_new_button)

# функция открывания окна для удаления контакта
def open_delete_window():
    pass


form.pushButton_2.clicked.connect(open_delete_window)


app.exec()

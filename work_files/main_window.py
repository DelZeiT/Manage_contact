from PyQt5 import uic
from PyQt5.QtWidgets import *
from work_files.add_wind import open_add_window
from work_files.contact_wind import open_contact_window



Form, Window = uic.loadUiType("disign_UI_UI/main_window_ui3.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)


# функция открывания окна для добавления контакта.
def start_add_window():
    open_add_window()


# окно контакты
def contact_window():
    open_contact_window()


# функция добавления контакта
def add_new_button():
    list_widget = form.listWidget
    new_button = QPushButton("Новая кнопка")
    new_button.setStyleSheet("background-color: #778899; color: white;")
    list_widget_item = QListWidgetItem()
    list_widget_item.setSizeHint(new_button.sizeHint())
    list_widget.addItem(list_widget_item)
    list_widget.setItemWidget(list_widget_item, new_button)
    new_button.clicked.connect(open_contact_window)


# функция открывания окна для удаления контакта
def open_delete_window():
    Form3, Window3 = uic.loadUiType("disign_UI_UI/delete_window_ui.ui")
    window3 = Window3()
    form3 = Form3()
    form3.setupUi(window3)
    window3.exec_()


# КЛИКИ КНОПОК
form.pushButton.clicked.connect(open_add_window)
form.pushButton_3.clicked.connect(add_new_button)
form.pushButton_2.clicked.connect(open_delete_window)


window.show()
app.exec()


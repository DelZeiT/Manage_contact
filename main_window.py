from PyQt5 import uic
from PyQt5.QtWidgets import *
from add_wind import open_add_window

Form, Window = uic.loadUiType("main_window_ui3.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)


# функция открывания окна для добавления контакта.
def start_add_window():
    open_add_window()


form.pushButton.clicked.connect(open_add_window)


def add_new_button():
    list_widget = form.listWidget
    new_button = QPushButton("Новая кнопка")
    list_widget_item = QListWidgetItem()
    list_widget_item.setSizeHint(new_button.sizeHint())
    list_widget.addItem(list_widget_item)
    list_widget.setItemWidget(list_widget_item, new_button)


form.pushButton_3.clicked.connect(add_new_button)

# функция открывания окна для удаления контакта
def open_delete_window():
    pass


form.pushButton_2.clicked.connect(open_delete_window)

window.show()
app.exec()


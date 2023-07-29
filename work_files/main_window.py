from PyQt5 import uic
from PyQt5.QtWidgets import *
# from work_files.add_wind import open_add_window
from work_files.contact_wind import open_contact_window
from backend_sql import Info_Contact


Form, Window = uic.loadUiType("disign_UI_UI/main_window_ui3.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)



# функция обработки всех кнопок в окне добавления контакта
def open_add_window():
    Form2, Window2 = uic.loadUiType("disign_UI_UI/add_window_ui.ui")
    window2 = Window2()
    form2 = Form2()
    form2.setupUi(window2)


    #кнопка добавление контакта
    def press_add_contact():
        text_LName = form2.lineEdit.text() # имя
        text_FName = form2.lineEdit_2.text() # фамилия
        text_Number = form2.lineEdit_3.text() # номер
        text_Email = form2.lineEdit_4.text() # почта

        if not text_LName or not text_FName or not text_Number or not text_Email:
            QMessageBox.warning(window2, 'Ошибка!', 'Заполните все поля.', QMessageBox.Ok)
            return

        info_contact = Info_Contact(text_LName, text_FName, text_Number, text_Email) # отправка в класс SQL
        info_contact.sql_query()

        add_new_button(text_LName, text_FName)
        window2.close()

    #кнопка отмены
    def press_cancel():
        window2.close()


    form2.pushButton.clicked.connect(press_add_contact) # кнопка добавить
    form2.pushButton_2.clicked.connect(press_cancel) # кнопка отмены

    window2.show()
    window2.exec_()



# функция добавления контакта в лист
def add_new_button(LName, FName):
    list_widget = form.listWidget
    new_button = QPushButton(f"{LName} {FName}")
    new_button.setStyleSheet("background-color: #778899; color: white;")
    list_widget_item = QListWidgetItem()
    list_widget_item.setSizeHint(new_button.sizeHint())
    list_widget.addItem(list_widget_item)
    list_widget.setItemWidget(list_widget_item, new_button)
    new_button.clicked.connect(open_contact_window)


# функция открывания окна для добавления контакта.
def start_add_window():
    open_add_window()


# окно контакты
def contact_window():
    open_contact_window()


# функция открывания окна для удаления контакта
def open_delete_window():
    Form3, Window3 = uic.loadUiType("disign_UI_UI/delete_window_ui.ui")
    window3 = Window3()
    form3 = Form3()
    form3.setupUi(window3)
    window3.exec_()


# КЛИКИ КНОПОК
form.pushButton.clicked.connect(open_add_window)
# form.pushButton_3.clicked.connect(add_new_button)
form.pushButton_2.clicked.connect(open_delete_window)


window.show()
app.exec()


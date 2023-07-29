from backend_sql import *
from contact_wind import *
from PyQt5 import uic
from PyQt5.QtWidgets import *
from refactor_contact_wind import refactor_contact

Form, Window = uic.loadUiType("main_window_ui3.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)

# global_LName = None
# global_FName = None
# global_Number = ''
# global_Email = None


# функция обработки всех кнопок в окне добавления контакта
def open_add_window():
    Form2, Window2 = uic.loadUiType("add_window_ui.ui")
    window2 = Window2()
    form2 = Form2()
    form2.setupUi(window2)

    # кнопка добавление контакта
    def press_add_contact():
        text_LName = form2.lineEdit.text()  # имя
        text_FName = form2.lineEdit_2.text()  # фамилия
        text_Number = form2.lineEdit_4.text()  # номер
        text_Email = form2.lineEdit_3.text()  # почта

        # ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ
        # global global_LName
        # global_LName = text_LName
        # global global_FName
        # global_FName = text_FName
        # global global_Number
        # global_Number = text_Number
        # global global_Email
        # global_Email = text_Email

        if not text_LName or not text_FName or not text_Number or not text_Email:
            QMessageBox.warning(window2, 'Ошибка!', 'Заполните все поля.', QMessageBox.Ok)
            return

        info_contact = InfoContact(text_LName, text_FName, text_Number, text_Email)  # отправка в класс SQL
        info_contact.sql_query()

        lname_cl = GetDataContact('LName', text_Number)
        fname_cl = GetDataContact('FName', text_Number)
        number_cl = GetDataContact('Number', text_Number)
        email_cl = GetDataContact('Email', text_Number)
        add_new_button(*lname_cl.get_another_name(), *fname_cl.get_another_name(), *number_cl.get_another_name())

        return info_cont(text_Number, text_LName, text_FName, text_Email)

    # кнопка отмены
    def press_cancel():
        window2.close()

    form2.pushButton.clicked.connect(press_add_contact)  # кнопка добавить
    form2.pushButton_2.clicked.connect(press_cancel)  # кнопка отмены

    window2.show()
    window2.exec_()


# открывает окно контакт
def open_contact_window():
    Form4, Window4 = uic.loadUiType("contact_window_ui.ui")
    window4 = Window4()
    form4 = Form4()
    form4.setupUi(window4)



    # редактор контакта
    def open_window_in_contact():
        refactor_contact()

    form4.pushButton.clicked.connect(open_window_in_contact)

    window4.exec_()

def info_cont(text_Number, text_LName, text_FName, text_Email):
    Form4, Window4 = uic.loadUiType("contact_window_ui.ui")
    window4 = Window4()
    form4 = Form4()
    form4.setupUi(window4)

    # переменные с инфой о пользователе
    form4.lineEdit_surname.insert(*GetDataContact(text_LName, text_Number).get_Lname())
    form4.lineEdit_name.insert(*GetDataContact(text_FName, text_Number).get_Fname())
    form4.lineEdit_number.insert(*GetDataContact(text_Number, text_Number).get_Number())
    form4.lineEdit_mail.insert(*GetDataContact(text_Email, text_Number).get_Email())


# функция добавления контакта в лист
def add_new_button(lname_cl, fname_cl, number_cl):
    list_widget = form.listWidget
    new_button = QPushButton(f"{lname_cl} {fname_cl}         {number_cl}")
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
    Form3, Window3 = uic.loadUiType("delete_window_ui.ui")
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

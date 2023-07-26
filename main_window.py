from PyQt5 import uic
from PyQt5.QtWidgets import *
#from add_window_py import AddWindow

Form, Window = uic.loadUiType("main_window_ui.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()


app.exec()
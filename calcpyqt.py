import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from operations import addNumbers

class CalculatorWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.button = QtWidgets.QPushButton("Add!")
        self.text = QtWidgets.QLabel("Add two numbers",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout_n1 = QtWidgets.QHBoxLayout()
        self.line_edit_n1 = QtWidgets.QLineEdit("")
        self.line_edit_n1.setFixedSize(100, 30)
        self.text_n1 = QtWidgets.QLabel("First number: ",
                                     alignment=QtCore.Qt.AlignCenter)
        self.layout_n1.addWidget(self.text_n1)
        self.layout_n1.addWidget(self.line_edit_n1)

        self.layout_n2 = QtWidgets.QHBoxLayout()
        self.line_edit_n2 = QtWidgets.QLineEdit("")
        self.line_edit_n2.setFixedSize(100, 30)
        self.text_n2 = QtWidgets.QLabel("Second number: ",
                                     alignment=QtCore.Qt.AlignCenter)
        self.layout_n2.addWidget(self.text_n2)
        self.layout_n2.addWidget(self.line_edit_n2)

        self.layout_result = QtWidgets.QHBoxLayout()
        self.line_edit_result = QtWidgets.QLineEdit("")
        self.line_edit_result.setFixedSize(100, 30)
        self.line_edit_result.setDisabled(True)
        self.text_result = QtWidgets.QLabel("Result: ",
                                     alignment=QtCore.Qt.AlignCenter)
        self.layout_result.addWidget(self.text_result)
        self.layout_result.addWidget(self.line_edit_result)

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.addWidget(self.text)
        self.main_layout.addLayout(self.layout_n1)
        self.main_layout.addLayout(self.layout_n2)
        self.main_layout.addLayout(self.layout_result)
        self.main_layout.addWidget(self.button)
        self.main_layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        try:
            self.line_edit_result.setText(str(round(addNumbers(float(self.line_edit_n1.text()), float(self.line_edit_n2.text())), 6)))
        except:
            self.line_edit_result.setText("Invalid")

        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = CalculatorWidget()
    widget.resize(200, 150)
    widget.show()

    sys.exit(app.exec())
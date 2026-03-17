from PySide6 import QtCore, QtWidgets, QtGui
from Logic.logic_controller import LogicController

class RevisionPage(QtWidgets.QWidget):

    def __init__(self, p_logic_controller):
        super().__init__()
        self.resize(900,900)
        self.logic_controller = p_logic_controller
        self.heading = QtWidgets.QLabel("Revise",
                                alignment=QtCore.Qt.AlignmentFlag.AlignTop)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.heading)
        self.setLayout(self.layout)


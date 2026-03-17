from PySide6 import QtCore, QtWidgets, QtGui
from Logic.logic_controller import LogicController

class AddSentencePairsPage(QtWidgets.QWidget):

    def __init__(self, p_logic_controller = None):
        super().__init__()
        self.resize(900,900)
        if p_logic_controller == None:
            self.logic_controller = LogicController()
        else:
            self.logic_controller = p_logic_controller
            
        self.heading = QtWidgets.QLabel("Add A Sentence Pair",
                                alignment=QtCore.Qt.AlignmentFlag.AlignTop)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.heading)
        self.setLayout(self.layout)



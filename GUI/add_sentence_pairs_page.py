from PySide6 import QtCore, QtWidgets, QtGui
from Logic.logic_controller import LogicController

class AddSentencePairsPage(QtWidgets.QWidget):

    def __init__(self, p_logic_controller = None):
        super().__init__()
        self.setFixedSize(1200,900)
        if p_logic_controller == None:
            self.logic_controller = LogicController()
        else:
            self.logic_controller = p_logic_controller


        self.heading = QtWidgets.QLabel("Add A Sentence Pair",
                                     alignment=QtCore.Qt.AlignmentFlag.AlignTop)
        self.previous_page_button = QtWidgets.QPushButton("Back")
        self.home_button = QtWidgets.QPushButton("Home")
        self.add_sentence_pair_button = QtWidgets.QPushButton("Add")
        self.options_button = QtWidgets.QPushButton("Options")
        

        self.drop_down = QtWidgets.QMenu(self)
        self.drop_down.addAction("Home", lambda: self.home_button.click())
        self.drop_down.addAction("Sound",lambda: print("Sound has been toggled"))
        self.options_button.setMenu(self.drop_down)


        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.heading)
        self.layout.addWidget(self.previous_page_button)
        self.layout.addWidget(self.options_button)
        self.layout.addWidget(self.add_sentence_pair_button)

    @QtCore.Slot()
    def add_sentence_pair(self, p_sentence_pair):
        self.logic_controller.add_sentence_pair(p_sentence_pair)


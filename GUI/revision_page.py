from PySide6 import QtCore, QtWidgets, QtGui
from Logic.logic_controller import LogicController

class RevisionPage(QtWidgets.QWidget):

    def __init__(self, p_logic_controller = None):
        super().__init__()
        self.setFixedSize(1200,900)

        if p_logic_controller == None:
            self.logic_controller = LogicController()
        else:
            self.logic_controller = p_logic_controller
            
        self.heading = QtWidgets.QLabel("Revise",
                                alignment=QtCore.Qt.AlignmentFlag.AlignTop)
        self.previous_page_button = QtWidgets.QPushButton("Back")
        self.option_button = QtWidgets.QPushButton("Options")
        self.next_sentence_pair_button = QtWidgets.QPushButton("Next SP")
        self.previous_sentence_pair_button = QtWidgets.QPushButton("Previous SP")
        self.toggle_show_sentence_pair_button = QtWidgets.QPushButton("Show/Hide Sentence")
        self.home_button = QtWidgets.QPushButton("Home")

        self.drop_down = QtWidgets.QMenu(self)
        self.drop_down.addAction("Home", lambda: self.home_button.click())
        self.drop_down.addAction("Sound",lambda: print("Sound has been toggled"))
        self.option_button.setMenu(self.drop_down)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.heading)
        self.layout.addWidget(self.option_button)
        self.layout.addStretch()
        self.layout.addWidget(self.next_sentence_pair_button)
        self.layout.addWidget(self.previous_sentence_pair_button)     
        self.layout.addWidget(self.toggle_show_sentence_pair_button)
        self.layout.addWidget(self.previous_page_button)   


       
    @QtCore.Slot()
    def next_sentence_pair():
        return False
    
    @QtCore.Slot()
    def previous_sentence_pair():
        return False
    
    @QtCore.Slot()
    def toggle_show_sentence_pair():
        return False


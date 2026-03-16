from PySide6 import QtCore, QtWidgets, QtGui
from Logic.logic_controller import LogicController

class ModifySentencePairsPage(QtWidgets.QWidget):

    def __init__(self, p_logic_controller):
        super().__init__()
        self.logic_controller = p_logic_controller


    def previous_page(self):
        return False


    def home_page(self):
        return False

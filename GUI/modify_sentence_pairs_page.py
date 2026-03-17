from PySide6 import QtCore, QtWidgets, QtGui
from Logic.logic_controller import LogicController

class ModifySentencePairsPage(QtWidgets.QWidget):

    def __init__(self, p_logic_controller = None):
        super().__init__()
        if p_logic_controller == None :
            self.logic_controller = LogicController
        else:  
            self.logic_controller = p_logic_controller


    def previous_page(self):
        return False


    def home_page(self):
        return False

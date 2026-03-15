from abc import ABC, abstractmethod
from PySide6 import QtCore, QtWidgets, QtGui
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Logic import logic_controller

class CITPage(ABC,QtWidgets.QWidget):

    @abstractmethod
    def previous_page(self):
        pass

    @abstractmethod
    def home_page(self):
        pass

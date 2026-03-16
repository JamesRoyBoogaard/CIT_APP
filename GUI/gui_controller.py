import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PySide6.QtWidgets import QStackedWidget, QApplication
from GUI.home_page import HomePage
from GUI.modify_sentence_pairs_page import ModifySentencePairsPage
from GUI.revision_page import RevisionPage
from GUI.add_sentence_pairs_page import AddSentencePairsPage
from Logic.logic_controller import LogicController

class GUIController():

    def __init__(self):
        self.app = QApplication([])
        self.stack = QStackedWidget()
        logic_controller = LogicController()
        home_page = HomePage()
        home_page.resize(900,900)
        #self.stack.addWidget(RevisionPage(logic_controller))
        self.stack.addWidget(home_page)
        # self.stack.addWidget(ModifySentencePairsPage(logic_controller))
        # self.stack.addWidget(AddSentencePairsPage(logic_controller))
        self.current_page = home_page
        self.stack.show()

    def run(self):
        sys.exit(self.app.exec())
        # self.app.exec()
    
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
        self.home_page = HomePage()
        self.revision_page = RevisionPage(logic_controller)
        self.modify_sentence_pairs_page = ModifySentencePairsPage(logic_controller)
        self.add_sentence_pairs_page = AddSentencePairsPage(logic_controller)

        # home_page.resize(900,900)
        self.stack.addWidget(self.home_page)
        self.stack.addWidget(self.revision_page)
        self.stack.addWidget(self.modify_sentence_pairs_page)
        self.stack.addWidget(self.add_sentence_pairs_page)

        self.navigation()

        self.current_page = self.home_page
        self.stack.show()

    def run(self):
        sys.exit(self.app.exec())
        # self.app.exec()
    
    def navigation(self):
        self.home_page.revision_button.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        self.home_page.modify_sentences_button.clicked.connect(lambda: self.stack.setCurrentIndex(2))
        self.home_page.add_sentences_button.clicked.connect(lambda: self.stack.setCurrentIndex(3))

        # Then do the same for all navigation for each of the pages
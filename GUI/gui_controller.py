import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PySide6.QtWidgets import QStackedWidget, QApplication
from GUI.home_page import HomePage
from GUI.modify_sentence_pairs_page import ModifySentencePairsPage
from GUI.revision_page import RevisionPage
from GUI.add_sentence_pairs_page import AddSentencePairsPage

class GUIController():

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.stack = QStackedWidget()
        self.stack.addWidget(RevisionPage())
        self.stack.addWidget(HomePage())
        self.stack.addWidget(ModifySentencePairsPage())
        self.stack.addWidget(AddSentencePairsPage())
    
    def run(self):
        self.window = HomePage()
        self.window.show()
        self.app.exec()
    
from PySide6.QtWidgets import QStackedWidget, QApplication
from home_page import HomePage
from modify_sentence_pairs_page import ModifySentencePairsPage
from revision_page import RevisionPage
from add_sentence_pairs_page import AddSentencePairsPage

class GUIController():

    def __init__(self):
        self.stack = QStackedWidget()
        self.stack.addWidget(RevisionPage())
        self.stack.addWidget(HomePage())
        self.stack.addWidget(ModifySentencePairsPage())
        self.stack.addWidget(AddSentencePairsPage())
    
    def run(self):
        self.app = QApplication()
        self.window = HomePage()
        self.window.show()
        self.app.exec()
    
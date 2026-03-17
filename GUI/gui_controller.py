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

    def __init__(self, p_app = None):
        if p_app == None:
            self.app = QApplication([])
        else:
            self.app = p_app
            
        self.stack = QStackedWidget()
        logic_controller = LogicController()
        self.list_of_widgets = []

        self.home_page = HomePage()
        self.revision_page = RevisionPage(logic_controller)
        self.modify_sentence_pairs_page = ModifySentencePairsPage(logic_controller)
        self.add_sentence_pairs_page = AddSentencePairsPage(logic_controller)

        # home_page.resize(900,900)
        self.stack.addWidget(self.home_page)
        self.stack.addWidget(self.revision_page)
        self.stack.addWidget(self.modify_sentence_pairs_page)
        self.stack.addWidget(self.add_sentence_pairs_page)
        
        # self.setPage(1)
        self.current_page = self.home_page
        self.navigation()
        self.stack.show()

    def run(self):
        sys.exit(self.app.exec())
        # self.app.exec()
    
    def navigation(self):
        # self.home_page.revision_button.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        self.home_page.revision_button.clicked.connect(lambda: self.setPage(1))
        self.home_page.modify_sentences_button.clicked.connect(lambda: self.setPage(2))
        self.home_page.add_sentences_button.clicked.connect(lambda: self.setPage(3))
        self.home_page.previous_page_button.clicked.connect(lambda: self.setPrevious())

        # Then do the same for all navigation for each of the pages
        

    def setPage(self, p_page_index):
        # add the p_page_index to the list and set it to that page index and then use this method as a lambda
        self.list_of_widgets.append(self.stack.currentIndex())
        self.stack.setCurrentIndex(p_page_index)
        self.current_page = self.stack.currentWidget()
      
    def setHome(self):
        self.setPage(0)

    def setPrevious(self):
        self.setPage(self.list_of_widgets.pop())

    def destroySingleton(self):
        self.app.quit()
        self.stack.destroy()
        del self.stack
        del self.app
from PySide6 import QtCore, QtWidgets, QtGui
from Logic.logic_controller import LogicController
from SentencePair import SentencePair

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
        self.english_sentence_input = QtWidgets.QTextEdit(placeholderText= "Enter english sentence")
        self.dutch_sentence_input = QtWidgets.QTextEdit(placeholderText= "Enter the dutch equivalent")
        self.options_button = QtWidgets.QPushButton("Options")
        

        self.drop_down = QtWidgets.QMenu(self)
        self.drop_down.addAction("Home", lambda: self.home_button.click())
        self.drop_down.addAction("Sound",lambda: print("Sound has been toggled"))
        self.options_button.setMenu(self.drop_down)


        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.heading)
        self.layout.addWidget(self.previous_page_button)
        self.layout.addWidget(self.options_button)
        self.layout.addWidget(self.english_sentence_input)
        self.layout.addWidget(self.dutch_sentence_input)
        self.layout.addWidget(self.add_sentence_pair_button)

        self.add_sentence_pair_button.clicked.connect(self.gui_add_sentence_pair)

    @QtCore.Slot()
    def gui_add_sentence_pair(self):
        # self.english_sentence_input.selectAll()
        # self.english_sentence_input.copy()
        english_sentence = self.english_sentence_input.toPlainText()
        # print(english_sentence)
        # self.dutch_sentence_input.selectAll()
        # self.dutch_sentence_input.copy()
        dutch_sentence = self.dutch_sentence_input.toPlainText()
        # print(dutch_sentence)

        if(english_sentence == None or dutch_sentence == None):
            print("please enter a valid input in both input fields")
        else:  
            sentence_pair = SentencePair(english_sentence,dutch_sentence)
            # print(str(len(self.logic_controller.get_all_sentence_pairs())))
            self.logic_controller.add_sentence_pair(sentence_pair)
            # print(str(len(self.logic_controller.get_all_sentence_pairs())))
            self.english_sentence_input.clear()
            self.dutch_sentence_input.clear()
            

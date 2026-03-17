from PySide6 import QtCore, QtWidgets

class HomePage(QtWidgets.QWidget):
    navigate_revision_page = QtCore.Signal()
    navigate_add_sentence_pairs_page = QtCore.Signal()
    navigate_modify_sentence_pairs_page = QtCore.Signal()

    def __init__(self):
        super().__init__()
        self.setFixedSize(1200,900)

        self.stack_list = []
        self.heading = QtWidgets.QLabel("Welcome",
                                     alignment=QtCore.Qt.AlignmentFlag.AlignTop)
        self.previous_page_button = QtWidgets.QPushButton("Back")
        self.modify_sentences_button = QtWidgets.QPushButton("Modify Sentence Pairs")
        self.add_sentences_button = QtWidgets.QPushButton("Add Sentence Pairs")
        self.revision_button = QtWidgets.QPushButton("Revise")
        self.options_button = QtWidgets.QPushButton("Options")
        

        self.drop_down = QtWidgets.QMenu(self)
        self.drop_down.addAction("Home", lambda: print("You are already at home"))
        self.drop_down.addAction("Sound",lambda: print("Sound has been toggled"))
        self.options_button.setMenu(self.drop_down)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.heading)
        self.layout.addWidget(self.options_button)
        self.layout.addStretch()
        self.layout.addWidget(self.revision_button)
        self.layout.addWidget(self.modify_sentences_button)
        self.layout.addWidget(self.add_sentences_button)
        self.layout.addWidget(self.previous_page_button)
   

        self.revision_button.pressed.connect(self.navigate_revision_page.emit)
        self.modify_sentences_button.pressed.connect(self.navigate_modify_sentence_pairs_page.emit)
        self.add_sentences_button.pressed.connect(self.navigate_add_sentence_pairs_page.emit)

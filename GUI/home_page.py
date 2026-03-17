from PySide6 import QtCore, QtWidgets

class HomePage(QtWidgets.QWidget):
    navigate_revision_page = QtCore.Signal()
    navigate_add_sentence_pairs_page = QtCore.Signal()
    navigate_modify_sentence_pairs_page = QtCore.Signal()

    def __init__(self):
        super().__init__()
        self.resize(900,900)
        # self.logic_controller = p_logic_controller
        # now we can set up the three buttons and there tests as well as the menu and the heading
        self.stack_list = []
        self.heading = QtWidgets.QLabel("Welcome",
                                     alignment=QtCore.Qt.AlignmentFlag.AlignTop)
        self.revision_button = QtWidgets.QPushButton("Revise")
        self.modify_sentences_button = QtWidgets.QPushButton("Modify Sentence Pairs")
        self.add_sentences_button = QtWidgets.QPushButton("Add Sentence Pairs")
        self.options_button = QtWidgets.QPushButton("Options")
        self.previous_page_button = QtWidgets.QPushButton("Back")

        self.layout = QtWidgets.QVBoxLayout(self)

        self.layout.addWidget(self.heading)
        self.layout.addStretch()
        self.layout.addWidget(self.previous_page_button)
        self.layout.addWidget(self.options_button)

        self.layout.addWidget(self.revision_button)
        self.layout.addWidget(self.modify_sentences_button)
        self.layout.addWidget(self.add_sentences_button)

        self.setLayout(self.layout)

        self.revision_button.pressed.connect(self.navigate_revision_page.emit)
        self.revision_button.pressed.connect(self.navigate_modify_sentence_pairs_page.emit)
        self.revision_button.pressed.connect(self.navigate_add_sentence_pairs_page.emit)
        self.revision_button.pressed.connect(self.options)

    @QtCore.Slot()
    def previous_page(self):
        # Go to the previously documented Widget and if that doesnt exist stay on home_page
        return False
    
    # @QtCore.Slot()
    # def navigate_revision_page(self):
    #     return self.navigate_revision_page


    # @QtCore.Slot()
    # def navigate_modify_sentence_pairs_page(self):
    #     return self.navigate_modify_sentence_pairs_page
    
    # @QtCore.Slot()
    # def navigate_add_sentence_pairs_page(self):
    #     return self.navigate_add_sentence_pairs_page

    @QtCore.Slot()
    def options(self):
        # handle the drop down menu
        # Can create a button grouping for inside the options drop down for the home and sound toggle
        return False
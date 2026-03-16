from PySide6 import QtCore, QtWidgets

class HomePage(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        # self.logic_controller = p_logic_controller
        # now we can set up the three buttons and there tests as well as the menu and the heading
        self.heading = QtWidgets.QLabel("Welcome",
                                     alignment=QtCore.Qt.AlignmentFlag.AlignTop)
        self.revision_button = QtWidgets.QPushButton("Revise")
        self.modify_sentences_button = QtWidgets.QPushButton("Modify Sentence Pairs")
        self.add_sentences_button = QtWidgets.QPushButton("Add Sentence Pairs")
        self.options_button = QtWidgets.QPushButton("Options")

        self.layout = QtWidgets.QVBoxLayout(self)

        # self.top_assets = QtWidgets.QHBoxLayout(self)
        # self.top_assets.addWidget(self.heading,alignment = QtCore.Qt.center)
        # self.top_assets.addStretch()
        # self.top_assets.addWidget(self.options_button)

        # self.middle_assets = QtWidgets.QVBoxLayout(self)
        # self.middle_assets.addWidget(self.revision_button, alignment=QtCore.Qt.center)
        # self.middle_assets.addWidget(self.modify_sentences_button, alignment=QtCore.Qt.center)
        # self.middle_assets.addWidget(self.add_sentences_button, alignment=QtCore.Qt.center)

        # self.layout.addLayout(self.top_assets)
        # self.layout.addLayout(self.middle_assets)
        self.layout.addWidget(self.heading)
        self.layout.addStretch()
        self.layout.addWidget(self.options_button)

        self.layout.addWidget(self.revision_button)
        self.layout.addWidget(self.modify_sentences_button)
        self.layout.addWidget(self.add_sentences_button)

        self.setLayout(self.layout)

        self.revision_button.pressed.connect(self.navigate_revision_page)
        self.revision_button.pressed.connect(self.navigate_modify_sentence_pairs_page)
        self.revision_button.pressed.connect(self.navigate_add_sentence_pairs_page)
        self.revision_button.pressed.connect(self.options)

    @QtCore.Slot()
    def previous_page(self):
        # Go to the previously documented Widget and if that doesnt exist stay on home_page
        return False
    
    @QtCore.Slot()
    def navigate_revision_page(self):
        return False

    @QtCore.Slot()
    def navigate_modify_sentence_pairs_page():
        return False
    
    @QtCore.Slot()
    def navigate_add_sentence_pairs_page():
        return False

    @QtCore.Slot()
    def options():
        # handle the drop down menu
        # Can create a button grouping for inside the options drop down for the home and sound toggle
        return False
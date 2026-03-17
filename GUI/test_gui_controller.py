import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PySide6 import QtWidgets
from Logic.logic_controller import LogicController
from Persistence.database_handler import DatabaseHandler
from SentencePair import SentencePair
from GUI.gui_controller import GUIController
from GUI.home_page import HomePage
from GUI.modify_sentence_pairs_page import ModifySentencePairsPage
from GUI.revision_page import RevisionPage
from GUI.add_sentence_pairs_page import AddSentencePairsPage

class TestGUIController():
    # setup for the tests

    # gui_controller testing section
    def test_run(self, gui_controller):
        # assert that the home page is the initial starting point
        # home_page = HomePage()
        # hp_type = type(home_page)
        # assert type(gui_controller.stack.currentWidget()) == hp_type
        assert type(gui_controller.stack.currentWidget()) == type(HomePage())
        
    # home_page testing section

    def test_modify_sentence_page(self, gui_controller):
        # WE NEED TO DESTROY THE APPLICATION BEFORE EACH TEST CAUSE THE CONTEXT IS CARRYING OVER
        assert type(gui_controller.stack.currentWidget()) == type(HomePage())
        gui_controller.setPage(2)
        assert type(gui_controller.stack.currentWidget()) == type(ModifySentencePairsPage())
        # assert gui_controller.stack.currentWidget == ModifySentencePairsPage()

    def test_revision_page(self, gui_controller):
        # assert that the window/scene/page has changed to the revision_page
        assert type(gui_controller.stack.currentWidget()) == type(HomePage())
        gui_controller.setPage(1)
        assert type(gui_controller.stack.currentWidget()) == type(RevisionPage())

    def test_add_sentence_pairs_page(self, gui_controller):
        # assert that the window/scene/page has changed to the add_sentence_pairs_page
        assert type(gui_controller.stack.currentWidget()) == type(HomePage())
        gui_controller.setPage(3)
        assert gui_controller.stack.currentWidget == AddSentencePairsPage()

    def test_return_to_home_page(self, gui_controller):
        assert type(gui_controller.stack.currentWidget()) == type(HomePage())
        gui_controller.setPage(2)
        assert type(gui_controller.stack.currentWidget()) == type(ModifySentencePairsPage())
        gui_controller.setHome()
        assert type(gui_controller.stack.currentWidget()) == type(HomePage())
        
    def test_return_to_previous_page(self, gui_controller):
        assert type(gui_controller.stack.currentWidget()) == type(HomePage())
        gui_controller.setPage(2)
        assert type(gui_controller.stack.currentWidget()) == type(ModifySentencePairsPage())
        gui_controller.setHome()
        assert type(gui_controller.stack.currentWidget()) == type(HomePage())
        gui_controller.setPrevious()
        assert type(gui_controller.stack.currentWidget()) == type(ModifySentencePairsPage())



    # # add_sentences_pairs_page testing section

    # def test_add_sentence_pairs():
    #     # assert that from the gui level 
    #     return False

    # # modify_sentence_pairs_page testing section

    # def test_search_next():
    #     return False

    # def test_search_previous():
    #     return False

    # def test_modify_sentence_pairs():
    #     return False

    # # revision_page testing section

    # def test_revision():
    #     return False
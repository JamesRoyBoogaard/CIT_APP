import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from Logic.logic_controller import LogicController
from Persistence.database_handler import DatabaseHandler
from SentencePair import SentencePair
from GUI.gui_controller import GUIController
from home_page import HomePage
from modify_sentence_pairs_page import ModifySentencePairsPage
from revision_page import RevisionPage
from add_sentence_pairs_page import AddSentencePairsPage

# setup for the tests

# gui_controller testing section
def test_run(self, gui_controller):
    # assert that the home page is the initial starting point
    assert gui_controller.stack.currentWidget == HomePage()
  

# home_page testing section

def test_modify_sentence_page(self, gui_controller):
    # assert that the window/scene/page has changed to the modify_sentence_page 
    assert gui_controller.stack.currentWidget == HomePage()
    HomePage().navigate_modify_sentence_pairs_page()
    assert gui_controller.stack.currentWidget == ModifySentencePairsPage()

def test_revision_page(self, gui_controller):
    # assert that the window/scene/page has changed to the revision_page
    assert gui_controller.stack.currentWidget == HomePage()
    HomePage().navigate_revision_page()
    assert gui_controller.stack.currentWidget == RevisionPage()

def test_add_sentence_pairs_page(self, gui_controller):
    # assert that the window/scene/page has changed to the add_sentence_pairs_page
    assert gui_controller.stack.currentWidget == HomePage()
    HomePage().navigate_add_sentence_pairs_page()
    assert gui_controller.stack.currentWidget == AddSentencePairsPage()


def test_return_to_previous_page(self, gui_controller):
    assert gui_controller.stack.currentWidget == HomePage()
    HomePage().navigate_modify_sentence_pairs_page()
    assert gui_controller.stack.currentWidget == ModifySentencePairsPage()
    ModifySentencePairsPage.previous_page()
    assert gui_controller.stack.currentWidget == HomePage()

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
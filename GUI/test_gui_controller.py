import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from Logic.logic_controller import LogicController
from Persistence.database_handler import DatabaseHandler
from SentencePair import SentencePair
from GUI.gui_controller import GUIController


# setup for the tests


# gui_controller testing section

def test_run():

    return False

# home_page testing section

def test_modify_sentence_page():
    # assert that the window/scene/page has changed to the modify_sentence_page 
    return False

def test_revision_page():
    # assert that the window/scene/page has changed to the revision_page
    return False

def test_add_sentence_pairs_page():
    # assert that the window/scene/page has changed to the add_sentence_pairs_page
    return False

# add_sentences_pairs_page testing section

def test_add_sentence_pairs():
    return False

# modify_sentence_pairs_page testing section

def test_search_next():
    return False

def test_search_previous():
    return False

def test_modify_sentence_pairs():
    return False

# revision_page testing section

def test_revision():
    return False
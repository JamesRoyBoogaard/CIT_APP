# import sys
# import os
import pytest
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Logic.logic_controller import LogicController
from Persistence.database_handler import DatabaseHandler
from SentencePair import SentencePair
from GUI.gui_controller import GUIController
from PySide6.QtWidgets import QApplication


# setup for all the tests in CITApp
@pytest.fixture
def db():
    mem_db = DatabaseHandler(":memory:")
    yield mem_db
    mem_db.close()

@pytest.fixture
def logic_controller(db):
    logic_controller = LogicController(db)
    yield logic_controller

@pytest.fixture(scope="session")
def qapp():
    app = QApplication.instance() or QApplication([])
    yield app

@pytest.fixture()
def gui_controller(qapp):
    gui_controller = GUIController(qapp)
    yield gui_controller
    gui_controller.destroySingleton()

@pytest.fixture
def populated_db(db):
    sentence_pairs = [SentencePair("Ik ga thuis", "I'm going home", '2026-03-05 12:30:40'),
    SentencePair("Ik wil wat pasta", "I want some pasta", '2026-01-05 10:30:40'),
    SentencePair("er zit eimand aan die kant", "There is someone sitting in that corner", '2026-04-05 12:30:40'),
    SentencePair("Hoe heet je", "What is your name", '2026-01-05 11:20:40'),
    SentencePair("Toen ik 96 werd", "When I turned 96", '2026-03-05 12:30:30'),
    SentencePair("Je waarschijnlijk geen sluetal toch", "You probably dont have a key right?", '2026-01-05 12:30:40'),
    SentencePair("Er zijn hier zo veel mensen", "There are so many people here", '2026-03-05 12:30:10'),
    SentencePair("Ik hoe van oilifanten", "I love elephants", '2026-03-05 06:30:40')]

    for sentence in sentence_pairs:
        db.add_sentence_pair(sentence)
        
    return db

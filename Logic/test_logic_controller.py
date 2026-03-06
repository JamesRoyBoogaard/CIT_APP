import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logic_controller import LogicController
from Persistence.test_database_handler import TestDatabaseHandler
from Persistence.database_handler import DatabaseHandler
from SentencePair import SentencePair


class TestLogicController():

    # @pytest.fixture
    # def proxy_db(self):
    #     test_database_handler = TestDatabaseHandler()
    #     db = test_database_handler.populated_db
    #     yield db

    #Setup
    @pytest.fixture
    def db(self):
        mem_db = DatabaseHandler(":memory:")
        yield mem_db
        mem_db.close()

    @pytest.fixture
    def populated_db(self, db):
        sentence_pairs = [SentencePair("Ik ga thuis", "I'm going home", '2026-03-05 12:30:40'),
        SentencePair("Ik wil wat pasta", "I want some pasta", '2026-01-05 10:30:40'),
        SentencePair("er zit eimand aan die kant", "There is someone sitting in that corner", '2026-04-05 12:30:40'),
        SentencePair("Hoe heet je", "What is your name", '2026-01-05 11:20:40'),
        SentencePair("Toen ik 96 werd", "When I turned 96", '2026-03-05 12:30:30'),
        SentencePair("Je waarschijnlijk geen sluetal toch", "You probably dont have a key right?", '2026-01-05 12:30:40'),
        SentencePair("Er zijn hier zo veel mensen", "There are so many people here", '2026-03-05 12:30:10'),
        SentencePair("Ik hoevan oilifanten", "I love elephants", '2026-03-05 06:30:40')]

        for sentence in sentence_pairs:
            db.add_sentence_pair(sentence)
            
        return db
    
    # @pytest.fixture
    # def logic_controller_supplier(self):
    #     logic_controller = LogicController()
    #     return logic_controller

    def test_memory_db(self, populated_db):
        populated_db.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='sentence_pairs'")
        result = populated_db.cursor.fetchall()
        assert result is not None

    # def test_update_sentence_pairs(self):

    #     assert False
    
    # def test_delete_sentence_pairs(self):
    #     assert False

    def test_add_sentence_pair(self, db):
        logic_controller = LogicController()

        db.cursor.execute("SELECT COUNT(ID) FROM sentence_pairs")
        initial_result = db.cursor.fetchone()
        assert initial_result == (0,)

        sp = SentencePair("eish", "eish", '2026-03-05 12:30:40')
        logic_controller.add_sentence_pair(sp)

        db.cursor.execute("SELECT COUNT(ID) FROM sentence_pairs")
        new_result = db.cursor.fetchone()
        assert new_result == (1,)
       

    # def test_revise(self):
    #     assert False
    
    # def test_get_all_sentence_pairs(self):
import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logic_controller import LogicController
from Persistence.test_database_handler import TestDatabaseHandler
from Persistence.database_handler import DatabaseHandler
from SentencePair import SentencePair
import datetime
import sqlite3


class TestLogicController():

    #Setup
    @pytest.fixture
    def db(self):
        mem_db = DatabaseHandler(":memory:")
        yield mem_db
        mem_db.close()

    @pytest.fixture
    def logic_controller(self,db):
        logic_controller = LogicController(db)
        yield logic_controller

    @pytest.fixture
    def populated_db(self, db):
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

    def test_memory_db(self, populated_db):
        populated_db.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='sentence_pairs'")
        result = populated_db.cursor.fetchall()
        assert result is not None
        populated_db.close()

    def test_close(self, db, logic_controller):
        db.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='sentence_pairs'")
        result = db.cursor.fetchall()
        assert result is not None
        logic_controller.close()
        with pytest.raises(sqlite3.ProgrammingError):
            db.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='sentence_pairs'")
            result = db.cursor.fetchall()

    def test_update_sentence_pairs(self, populated_db, logic_controller):
        populated_db.cursor.execute("SELECT DutchSentence FROM sentence_pairs WHERE ID = 1")
        result = populated_db.cursor.fetchone()
        assert result == ("Ik ga thuis",)

        sp = SentencePair("testen", "testing")
        logic_controller.update_sentence_pairs(1, sp)

        populated_db.cursor.execute("SELECT DutchSentence FROM sentence_pairs WHERE ID IN (2,9)")
        result = populated_db.cursor.fetchall()
        assert result == [("Ik wil wat pasta",),("testen",)]
        logic_controller.close()
       
    
    def test_delete_sentence_pairs(self,populated_db, logic_controller):
        populated_db.cursor.execute("SELECT DutchSentence FROM sentence_pairs WHERE ID = 1")
        result = populated_db.cursor.fetchone()
        assert result == ("Ik ga thuis",)
        logic_controller.delete_sentence_pair(1)

        populated_db.cursor.execute("SELECT DutchSentence FROM sentence_pairs WHERE ID = 1")
        result = populated_db.cursor.fetchone()
        assert result == ("Ik wil wat pasta",)
        logic_controller.close()

    def test_add_sentence_pair(self, db, logic_controller):

        db.cursor.execute("SELECT COUNT(ID) FROM sentence_pairs")
        initial_result = db.cursor.fetchone()
        assert initial_result == (0,)

        sp = SentencePair("testen", "testing")
        logic_controller.add_sentence_pair(sp)

        db.cursor.execute("SELECT COUNT(ID) FROM sentence_pairs")
        new_result = db.cursor.fetchone()
        assert new_result == (1,)
        logic_controller.close()

    def test_revise(self, populated_db, logic_controller):
        test_list = populated_db.get_sentence_pairs(3)
        logic_list = logic_controller.revise(3)
        time_now = datetime.datetime.now()
        assert len(test_list) == 3 and len(logic_list) == 3

        # Check that the ids are 2,4,6 in that order
        expected_id_order = [2,4,6]
        for i in range(len(logic_list)):
            print(str(logic_list[i].LastReviewed))
            print(str(logic_list[i].DutchSentence))
            assert logic_list[i].ID == expected_id_order[i]
        
        placeholder = ",".join(["?"]*len(expected_id_order))

        populated_db.cursor.execute("SELECT LastReviewed FROM sentence_pairs WHERE ID IN ("+placeholder+")",expected_id_order)
        updated_dates = populated_db.cursor.fetchall()
        
        for rows_date in updated_dates:
            assert str(rows_date)[2:-3] == str(time_now)[:-7]
        logic_controller.close()
        
    
    def test_get_all_sentence_pairs(self, populated_db, logic_controller):
        all_sentences = logic_controller.get_all_sentence_pairs()
        all_sentence_pairs_comparison = populated_db.cursor.execute("SELECT DutchSentence FROM sentence_pairs")

        i = 0
        for dutch_sentence in all_sentence_pairs_comparison: 
            assert dutch_sentence == all_sentences[i].DutchSentence
            i = i + 1

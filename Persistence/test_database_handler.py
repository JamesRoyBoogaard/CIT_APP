import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
import sqlite3
from Persistence.database_handler import DatabaseHandler
from SentencePair import SentencePair
import datetime

class TestDatabaseHandler():

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
    
    #Tests
    def test_persistence_handler_instantiate(self,db):
        db.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='sentence_pairs'")
        result = db.cursor.fetchall()
        assert result is not None

    def test_add_sentence_pair(self, db):
        db.cursor.execute("SELECT COUNT(ID) FROM sentence_pairs")
        num_sentence_pairs_in_db = db.cursor.fetchone()
        assert num_sentence_pairs_in_db == (0,)

        sentence = SentencePair("Hoe heet je", "What is your name", '2026-03-05 12:20:40')
        db.add_sentence_pair(sentence)
        db.cursor.execute("SELECT COUNT(ID) FROM sentence_pairs")
        num_sentence_pairs_in_db = db.cursor.fetchone()
        assert num_sentence_pairs_in_db == (1,)

    def test_remove_sentence_pair(self, populated_db):
        populated_db.cursor.execute("SELECT COUNT(ID) FROM sentence_pairs")
        num_sentence_pairs_in_db = populated_db.cursor.fetchone()
        assert num_sentence_pairs_in_db == (8,)

        populated_db.remove_sentence_pair(1)
        populated_db.cursor.execute("SELECT COUNT(ID) FROM sentence_pairs")
        num_sentence_pairs_in_db = populated_db.cursor.fetchone()
        assert num_sentence_pairs_in_db == (7,)

        populated_db.remove_sentence_pair(2)
        populated_db.cursor.execute("SELECT COUNT(ID) FROM sentence_pairs")
        num_sentence_pairs_in_db = populated_db.cursor.fetchone()
        assert num_sentence_pairs_in_db == (6,)
    
    def test_get_sentence_pair(self, populated_db):
        review_list = populated_db.get_sentence_pairs(3)
        time_now = datetime.datetime.now()
        assert len(review_list) == 3

        # Check that the ids are 2,4,6 in that order
        expected_id_order = [2,4,6]
        for i in range(len(review_list)):
            assert review_list[i].ID == expected_id_order[i]
        
        placeholder = ",".join(["?"]*len(expected_id_order))

        populated_db.cursor.execute("SELECT LastReviewed FROM sentence_pairs WHERE ID IN ("+placeholder+")",expected_id_order)
        updated_dates = populated_db.cursor.fetchall()
        
        for rows_date in updated_dates:
            assert str(rows_date)[2:-3] == str(time_now)[:-7]

        
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
import sqlite3
from Persistence.database_handler import DatabaseHandler
from SentencePair import SentencePair
import datetime

class TestDatabaseHandler():

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
            print(str(review_list[i].LastReviewed))
            print(str(review_list[i].DutchSentence))
            assert review_list[i].ID == expected_id_order[i]
        
        placeholder = ",".join(["?"]*len(expected_id_order))

        populated_db.cursor.execute("SELECT LastReviewed FROM sentence_pairs WHERE ID IN ("+placeholder+")",expected_id_order)
        updated_dates = populated_db.cursor.fetchall()
        
        for rows_date in updated_dates:
            assert str(rows_date)[2:-3] == str(time_now)[:-7]

        
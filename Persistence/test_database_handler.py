import pytest
#import database_handlerDa
import sqlite3
from database_handler import DatabaseHandler
from SentencePair import SentencePair
import datetime

class TestDatabaseHandler():

    @pytest.fixture
    def db(self):
        mem_db = DatabaseHandler(":memory:")
        yield mem_db
        mem_db.close()

    @pytest.fixture
    def populated_db(self, db):
        sentence_pairs = [SentencePair("Ik ga thuis", "I'm going home", '2026-03-05 12:30:40'),
        SentencePair("Ik wil wat pasta", "I want some pasta", '2026-03-05 10:30:40'),
        SentencePair("er zit eimand aan die kant", "There is someone sitting in that corner", '2026-04-05 12:30:40'),
        SentencePair("Hoe heet je", "What is your name", '2026-03-05 12:20:40'),
        SentencePair("Toen ik 96 werd", "When I turned 96", '2026-03-05 12:30:30'),
        SentencePair("Je waarschijnlijk geen sluetal toch", "You probably dont have a key right?", '2026-03-02 12:30:40'),
        SentencePair("Er zijn hier zo veel mensen", "There are so many people here", '2026-03-05 12:30:10'),
        SentencePair("Ik hoevan oilifanten", "I love elephants", '2026-03-05 06:30:40')]

        for sentence in sentence_pairs:
            db.add_sentence_pair(sentence)
            
        return db
    
    def test_persistence_handler_instantiate(self,db):
        db.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='sentence_pairs'")
        result = db.cursor.fetchall()
        assert result is not None

    def test_add_sentence_pair(self, db):
        db.cursor.execute("SELECT COUNT(ID) FROM sentence_pairs")
        num_sentences_in_db = db.cursor.fetchone()
        #print(num_sentences_in_db)
        assert num_sentences_in_db == (0,)

        sentence = SentencePair("Hoe heet je", "What is your name", '2026-03-05 12:20:40')
        db.add_sentence_pair(sentence)
        db.cursor.execute("SELECT COUNT(ID) FROM sentence_pairs")
        num_sentences_in_db = db.cursor.fetchone()
        assert num_sentences_in_db == (1,)
        
import sqlite3
import SentencePair

def __init__(self):
    self.connection = sqlite3.connect("SentencePairs.db")
    self.cursor = self.connection.cursor()
    self.cursor.execute("Create Table If Not Exists sentence_pairs(ID INTEGER PRIMARY KEY AUTOINCREMENT, DutchSentence TEXT, EnglishSentence TEXT, LastReviewed DATETIME)")
    

def add_sentence_pair(self, sentence_pair):
    # Add sentence_pair to the db
    DutchSentence = sentence_pair.DutchSentence
    EnglishSentence = sentence_pair.EnglishSentence
    LastReviewed = sentence_pair.LastReviewed

    new_tuple = (DutchSentence,EnglishSentence,LastReviewed)
    self.cursor.execute("INSERT INTO sentence_pairs VALUES (?,?,?)", new_tuple)
    self.connection.commit()
    

def remove_sentence_pair(self, sentence_pair_id):
    #remove the sentence pair from the database that has sentence_pair_id as its primary key
    self.cursor.execute("DELETE FROM sentence_pairs WHERE ID = ?", sentence_pair_id)
    self.connection.commit()

def get_sentence_pairs(self, p_number_of_sentence_pairs):
    # return p_number_of_sentence_pairs of the least revised sentence pairs as a List<SentencePairs>
    return p_number_of_sentence_pairs

def close(self):
    self.connection.close()
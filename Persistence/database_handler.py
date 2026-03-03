import sqlite3


def database_handler():
    connection = sqlite3.connect("SentencePairs.db")
    cursor = connection.cursor()
    cursor.execute("Create Table If Not Exists sentence_pairs(ID INTEGER PRIMARY KEY, DutchSentence TEXT, EnglishSentence TEXT, LastReviewed DATETIME)")
    connection.close()


def add_sentence_pair(sentence_pair):
    # Add sentence_pair to the db
    return 0

def remove_sentence_pair(sentence_pair_id):
    #remove the sentence pair from the database that has sentence_pair_id as its primary key
    return 0

def get_sentence_pairs(p_number_of_sentence_pairs):
    # return p_number_of_sentence_pairs of the least revised sentence pairs as a List<SentencePairs>
    return p_number_of_sentence_pairs
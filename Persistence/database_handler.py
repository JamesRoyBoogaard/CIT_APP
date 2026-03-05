import sqlite3
from SentencePair import SentencePair

class DatabaseHandler():

    def __init__(self, db_pth = "SentencePairs.db"):
        self.connection = sqlite3.connect(db_pth)
        self.cursor = self.connection.cursor()
        self.cursor.execute("Create Table If Not Exists sentence_pairs(ID INTEGER PRIMARY KEY AUTOINCREMENT, DutchSentence TEXT, EnglishSentence TEXT, LastReviewed DATETIME)")
        

    def add_sentence_pair(self, sentence_pair):
        # Add sentence_pair to the db
        DutchSentence = sentence_pair.DutchSentence
        EnglishSentence = sentence_pair.EnglishSentence
        LastReviewed = sentence_pair.LastReviewed

        new_tuple = (DutchSentence,EnglishSentence,LastReviewed)
        self.cursor.execute("INSERT INTO sentence_pairs (DutchSentence, EnglishSentence, LastReviewed) VALUES (?,?,?)", new_tuple)
        self.connection.commit()
        

    def remove_sentence_pair(self, sentence_pair_id):
        #remove the sentence pair from the database that has sentence_pair_id as its primary key
        self.cursor.execute("DELETE FROM sentence_pairs WHERE ID = ?", str(sentence_pair_id))
        self.connection.commit()

    def get_sentence_pairs(self, p_number_of_sentence_pairs):
        # return p_number_of_sentence_pairs of the least revised sentence pairs as a List<SentencePairs>
        review_list = []
        self.cursor.execute("""SELECT ID,DutchSentence,EnglishSentence,LastReviewed
                    FROM sentence_pairs 
                    ORDER BY date(LastReviewed) ASC 
                    LIMIT ?"""
                , str(p_number_of_sentence_pairs))
        sentence_pairs = self.cursor.fetchall()
        print(sentence_pairs)

        rows_to_update = [row[0] for row in sentence_pairs]
        placeholder = ",".join(["?"] * len(rows_to_update))
        self.cursor.execute("""UPDATE sentence_pairs
                    SET LastReviewed = CURRENT_TIMESTAMP
                    WHERE ID IN (""" + placeholder +")", rows_to_update)
        self.connection.commit()

        for ID, DutchSentence, EnglishSentence, LastReviewed in sentence_pairs:
            sentence_pair = SentencePair(DutchSentence,EnglishSentence,LastReviewed,ID)
            review_list.append(sentence_pair)

        return review_list

    def close(self):
        self.connection.close()
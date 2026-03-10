import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from SentencePair import SentencePair
from Persistence.database_handler import DatabaseHandler


class LogicController():

    def __init__(self, p_db_handler = None):
        if p_db_handler == None:
            self.db_handler = DatabaseHandler()
        else:
            self.db_handler = p_db_handler
   
    def update_sentence_pairs(self, ID, new_sentence_pair):
        self.db_handler.remove_sentence_pair(ID)
        self.db_handler.add_sentence_pair(new_sentence_pair)
        # self.db_handler.close()
    
    def delete_sentence_pairs(self, ID):
        self.db_handler.remove_sentence_pair(ID)
        # self.db_handler.close()

    def add_sentence_pair(self, new_sentence_pair):
        self.db_handler.add_sentence_pair(new_sentence_pair)
        #self.db_handler.close()

    def revise(self, number_sentences):
        revision_list = self.db_handler.get_sentence_pairs(number_sentences)
        # self.db_handler.close()
        return revision_list
    
    def close(self):
        self.db_handler.close()
import sys
import os
from SentencePair import SentencePair
from Persistence.database_handler import DatabaseHandler
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class LogicController():

    def __init__(self):
        self.db_handler = DatabaseHandler()
        
    def update_sentence_pairs(self, ID, new_sentence_pair):
        return 0
    
    def delete_sentence_pairs(self, ID):
        return 0
    
    def add_sentence_pair(new_sentence_pair):
        return 0
    
    def revise(number_sentences):
        return 0
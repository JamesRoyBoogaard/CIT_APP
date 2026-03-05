import pytest
#import database_handlerDa
import sqlite3
from database_handler import DatabaseHandler

class TestDatabaseHandler():

    @pytest.fixture
    def db(self):
        mem_db = DatabaseHandler(":memory:")
        yield mem_db
        mem_db.close()

    
    def test_persistence_handler_instantiate(self,db):
        assert 0==0
import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logic_controller import LogicController


class TestLogicController():

    @pytest.fixture
    def setup():
        logic_controller = LogicController("test")
        yield logic_controller
        
        
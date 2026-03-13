from Logic.logic_controller import LogicController

class GUIController():

    def __init__(self, p_logic_controller = None):
        if(p_logic_controller == None):
            self.logic_controller = LogicController()
        else:
            self.logic_controller = p_logic_controller
     
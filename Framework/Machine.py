import json
class Machine():
    def __init__(self,name,initial_state = None):
        self.name = name
        self.initial_state = initial_state
        self.current_state = self.initial_state
         
    #Simulates the run of the machine on inputs    
    def simulate(self,inputs):
        if(self.initial_state == None):
            raise  Exception('Initial state is: None')
        self.current_state = self.initial_state    
        self.initial_state.logic()    
        for i in inputs:
            self.current_state = self.current_state.get_next(i)
            self.current_state.logic() 
            

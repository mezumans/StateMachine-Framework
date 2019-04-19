
from Framework.State import *
from Framework.Event import *
from Framework.Machine import *

class StateImpl(State):
    def __init__(self,name,is_acceptor=False):
        self.name = name
        self.is_acceptor = is_acceptor
        #Dictionary<event_id,state>, key:event_id(Event), value:state(State)
        self.transition_map = {}
        
    @classmethod
    def build_acceptor(cls, name):
        return cls(name, True)
    
    def get_next(self,event):
        return self.transition_map[event]

    def logic(self):
        print("State:{}".format(type(self).__name__))
        if(self.is_acceptor):
            print('Warning: Three consecutive events')

  
class Initial(StateImpl):
    def get_next(self,event):  
        if (event == event_one):
            self.transition_map[event] = first_one_state
        else:
            self.transition_map[event] = first_two_state    
        return StateImpl.get_next(self,event)
   
class One(StateImpl):
    def get_next(self,event):
        if (event == event_one):
            self.transition_map[event] = second_one_state
        else:
            self.transition_map[event] = first_two_state    
        return StateImpl.get_next(self,event)

        
class Ones(StateImpl):
    def get_next(self,event):
        if (event == event_one):
            self.transition_map[event] = final_one_state
        else:
            self.transition_map[event] = first_two_state   
        return StateImpl.get_next(self,event)

class Two(StateImpl):
    def get_next(self,event):
        if (event == event_one):
            self.transition_map[event] = first_one_state
        else:
            self.transition_map[event] = second_two_state  
        return StateImpl.get_next(self,event)

class Twos(StateImpl):
    def get_next(self,event):
        if (event == event_one):
            self.transition_map[event] = first_one_state
        else:
            self.transition_map[event] = final_two_state  
        return StateImpl.get_next(self,event)

class Finish(StateImpl):       
    def get_next(self,event):
        if (event == event_one):
            self.transition_map[event] = final_one_state
        else:
            self.transition_map[event] = first_two_state
        return StateImpl.get_next(self,event)

class FinishTwo(StateImpl):       
    def get_next(self,event):
        if (event == event_one):
            self.transition_map[event] = first_one_state
        else:
            self.transition_map[event] = final_two_state    
        return StateImpl.get_next(self,event)

initial_state = Initial("initial_state")
first_one_state = One("first_one_state")
second_one_state = Ones('second_one_state')
final_one_state = Finish.build_acceptor("final_one_state")
first_two_state = Two("first_two_state")
second_two_state = Twos("second_two_state")
final_two_state = FinishTwo.build_acceptor("final_two_state")
event_one = Event(1)
event_two = Event(2)
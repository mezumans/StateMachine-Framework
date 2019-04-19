import json
from Framework.Machine import *
class PresistentMachine(Machine):
    def __init__(self,name,initial_state = None,events = [],states = []):
        self.name = name
        self.initial_state = initial_state
        self.transition_table = {}        
        self.events = events
        self.states = states
        #current_state holds the state class name
        self.current_state = self.get_first()
        if(self.states!=[]):
            for state in self.states:
                self.add_state(state)   
                
    #Get the first key in the hash table 
    def get_first(self):
        if(self.initial_state == None):
            try:
                return (next(iter(self.transition_table)))
            except StopIteration as identifier:
                print("Transition table is empty")
        else:
            return self.get_class_name(self.initial_state)

    #Gets event and returns state
    def get_next(self,event): 
        self.current_state = self.transition_table[self.current_state][str(event.event_id)]
        return self.current_state
        
    def subscribe_event(self,event):
        self.events.append(event)

    #Maintain transition table
    def add_state(self,state):
        transition = {}
        if(self.events!=[]):
            for event in self.events:
                next_state = state.get_next(event)
                transition[event.event_id] = self.get_class_name(next_state)
            self.transition_table[self.get_class_name(state)]  = transition
            self.save_to_file()
        else:
            raise Exception("Subscribe events before adding states")

    #Can be multithreaded presistency vs preformance
    def save_to_file(self):
        json_string = self.serialize_json(self.transition_table)
        file = open("machine_state.json", "w")
        file.write(json_string)
    #Can be multithreaded , presistency vs preformance
    def load_file(self):
        file = open("machine_state.json", "r")
        self.transition_table = self.deserialize_json(file)
        #init first state
        self.initial_state = self.current_state = self.get_first()

    def serialize_json(self,map):
        return json.dumps(map) 

    def deserialize_json(self,file):
        return json.loads(file.read())

    def get_class_name(self,class_instance):
        return  class_instance.__name__           
from abc import ABC, abstractmethod
class State(ABC):
    #is_acceptor is True if State is accepting state
    def __init__(self):
       pass
        
    #Get event and returns the next state object
    @abstractmethod
    def get_next(self,event): 
        pass
    
    #Implment logic here
    @abstractmethod
    def logic(self):
        pass

        

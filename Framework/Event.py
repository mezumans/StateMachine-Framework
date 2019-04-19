
class Event():
    def __init__(self,event_id):
        self.event_id = event_id

    def __eq__(self,other):
        return self.event_id == other.event_id

    def __lt__ (self, other):
        return self.event_id < other.event_id

    def __gt__ (self, other):
        return self.event_id > other.event_id

    def __ne__ (self, other):
        return not self.__eq__(other)

    def __hash__(self) :
        return hash((self.event_id))
    
        
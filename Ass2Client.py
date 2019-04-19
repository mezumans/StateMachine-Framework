
from Framework.State import *
from Framework.Event import *
from Framework.PresistentMachine import *

class Initial(State):
    def get_next(event):  
        if (event.event_id == 1):
            return One
        else:
            return Two
    @staticmethod
    def logic():
        print("State:Initial")
    
class One(State):
    @staticmethod
    def get_next(event):
        if (event.event_id == 1):
            return Ones
        else:
            return Two
    @staticmethod
    def logic():
         print("State:One")    

class Two(State):
    @staticmethod
    def get_next(event):
        if (event.event_id == 1):
            return Ones
        else:
            return Twos
    @staticmethod
    def logic():
         print("State:Two")    


class Ones(State):
    @staticmethod
    def get_next(event):
        if (event.event_id == 1):
           return FinishOne
        else:
            return Two
    @staticmethod
    def logic():
         print('state:Ones')        

class Twos(State):
    @staticmethod
    def get_next(event):
        if (event.event_id == 1):
           return One
        else:
            return FinishTwo
    @staticmethod
    def logic():
         print('State:Twos')        

class FinishOne(State):       
    @staticmethod
    def get_next(event):
        if (event.event_id == 1):
            return FinishOne
        else:
            return Two
    @staticmethod
    def logic():
         print('State:FinishOne, Warning: Three consecutive events')

class FinishTwo(State):       
    @staticmethod
    def get_next(event):
        if (event.event_id == 2):
            return FinishTwo
        else:
            return One
    @staticmethod
    def logic():
         print('State:FinishTwo, Warning: Three consecutive events')    

event_one = Event(1)
event_two = Event(2)
states = [Initial,One,Ones,Two,Twos,FinishOne,FinishTwo]
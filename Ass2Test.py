
from Ass2Client  import *

machine = PresistentMachine('First Machine',initial_state = Initial,
            events = [event_one,event_two],states=states )
machine.states = []
machine.load_file()

#**********Restore state case*************
#******************************PresistentMachine.get_next(event) reads from transition_table**************      

events = [event_one,event_one,event_one,event_two,event_two,event_one
                    ,event_two,event_two,event_two,event_two]
state_class = eval(machine.current_state)
logic_func = getattr(state_class, 'logic')
logic_func()
for event in events:
    state_name = machine.get_next(event)
    state_class = eval(machine.current_state)
    logic_func = getattr(state_class, 'logic')
    logic_func()
    

from Ass1Client import *


states = [initial_state,first_one_state,second_one_state,final_one_state
        ,first_two_state,second_two_state,final_two_state]
machine = Machine('First Machine',initial_state = initial_state )
#machine = PresistentMachine('First Machine',initial_state = initial_state,events = [one,two],states=states )
print('first simulation:')
machine.simulate([event_two,event_two,event_two])   

print('\nSecond simulation:')
machine.simulate([event_one,event_one,event_one])

print('\nThird simulation:')
machine.simulate([event_two,event_two,event_one]) 

print('\nFourth simulation:')   
machine.simulate([event_one,event_one,event_one,event_two,event_two,event_one
                    ,event_two,event_two,event_two,event_two])

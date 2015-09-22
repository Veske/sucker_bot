__author__ = 'kaspar'

import Room
from Agent import Agent
from Agent2 import Agent2


class Simulator:
    def __init__(self):
        self.rooms = [Room.Room("A", "CLEAN"), Room.Room("B", "DIRTY")]

    def get_room1(self):
        return self.rooms[0]

    def get_room2(self):
        return self.rooms[1]



manual_world = input("Do you want to create the world manually?  Y/n")

if(manual_world.capitalize() == "Y"):
    a_state = input("Room A state...    CLEAN/DIRTY")
    b_state = input("Room B state...    CLEAN/DIRTY")
    steps = input("How many steps to run for...  n")
    sim = Simulator()
    sim.rooms[0].state = a_state.upper()
    sim.rooms[1].state = b_state.upper()

    a = Agent(sim.rooms)
    b = Agent2(sim.rooms)
    a.run(int(steps))
    b.run(int(steps))

else:
    c = Simulator()
    a = Agent(c.rooms)
    b = Agent2(c.rooms)
    a.run()
    b.run()



__author__ = 'kaspar'

import msvcrt
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


c = Simulator()

#a = Agent(c.rooms)
a = Agent2(c.rooms)

a.run()









#print(a.left())
#print(c.get_room1().getName())
#a.suck(c.get_room2())
#print(c.get_room1().getName(), c.get_room1().getState())
#print(c.get_room2().getName(), c.get_room2().getState())

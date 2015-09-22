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

c = Simulator()

#a = Agent(c.rooms)
a = Agent(c.rooms)

a.run()
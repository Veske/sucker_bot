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

simulator1 = Simulator()
simulator2 = Simulator()

a = Agent(simulator1.rooms)
b = Agent2(simulator2.rooms)

a.run()
b.run()
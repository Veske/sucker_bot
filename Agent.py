__author__ = 'kaspar'

from random import randint

class Agent:
    room = ""

    def __init__(self, rooms):
        self.rooms = rooms
        self.room = rooms[randint(0, 1)]

    def suck(self, room):
        room.cleanRoom()

    def no_op(self):
        return

    def left(self):
        if(self.room.getName() != "A"):
            self.room = self.rooms[0]
            print("Cleaning: ", self.room.getName(), "State after work: ", self.room.getState())
        else:
            print("Cleaning: ", self.room.getName(), "State after work: ", self.room.getState())
            return

    def right(self):
        if(self.room.getName() != "B"):
            self.room = self.rooms[1]
            print("Cleaning: ", self.room.getName(), "State after work: ", self.room.getState())
        else:
            print("Cleaning: ", self.room.getName(), "State after work: ", self.room.getState())
            return


    def run(self, steps = 10):
        for i in range(steps):
            if(self.room.getState() == "DIRTY"):
                self.room.cleanRoom()
                self.choose_room(randint(0, 1) )
            else:
                self.choose_room(randint(0, 1) )

    def choose_room(self, choice):
        if(choice == 0):
            self.right()
        else:
            self.left()

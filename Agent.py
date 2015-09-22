__author__ = 'kaspar'

from random import randint
from Colors import bcolors

class Agent:
    room = ""

    def __init__(self, rooms):
        self.rooms = rooms
        self.room = rooms[randint(0, 1)]
        self.score = 1

    def suck(self, room):
        self.score -= 1
        print(bcolors.OKGREEN + "Cleaning room: ", self.room.getName())
        room.cleanRoom()

    def no_op(self):
        return

    def left(self):
        self.score -= 1
        if(self.room.getName() != "A"):
            self.room = self.rooms[0]
            print("Moving to room: ", self.room.getName(), "Room state: ", self.room.getState())
        else:
            self.no_op()

    def right(self):
        self.score -= 1
        if(self.room.getName() != "B"):
            self.room = self.rooms[1]
            print("Moving to room: ", self.room.getName(), "Room state: ", self.room.getState())
        else:
            self.no_op()


    def run(self, steps = 10):
        for i in range(steps):
            self.score += 1
            print(bcolors.BOLD + "Step: ", i)
            print(bcolors.FAIL + "Current room states:\nROOM A: ", self.rooms[0].getState(), "\tROOM B: ", self.rooms[1].getState() + bcolors.ENDC)
            if(self.room.getState() == "DIRTY"):
                self.suck(self.room)
            else:
                self.choose_room(randint(0, 1) )

        print(bcolors.OKBLUE + "\nScore after operation: ", self.score, bcolors.ENDC, "\n")

    def choose_room(self, choice):
        if(choice == 0):
            self.right()
        else:
            self.left()

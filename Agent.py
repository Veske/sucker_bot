__author__ = 'kaspar'

from random import randint

class Agent:
    room = ""

    def __init__(self, rooms):
        self.rooms = rooms
        self.room = rooms[randint(0, 1)]
        self.score = 0;

    def suck(self, room):
        print("State: Sucking Room:[",self.room.getName(),",",self.room.getState(),"]")
        self.room.cleanRoom()

    def no_op(self):
        return

    def left(self):
        self.score-=1;
        if(self.room.getName() != "A"):
            self.room = self.rooms[0]
            print("Cleaning: ", self.room.getName(), "State after work: ", self.room.getState())
        else:
            print("Cleaning: ", self.room.getName(), "State after work: ", self.room.getState())
            return

    def right(self):
        self.score-=1;
        if(self.room.getName() != "B"):
            self.room = self.rooms[1]
            print("Cleaning: ", self.room.getName(), "State after work: ", self.room.getState())
        else:
            print("Cleaning: ", self.room.getName(), "State after work: ", self.room.getState())
            return


    def run(self, steps = 10):

        for i in range(steps):
            self.score+=1;
            if(self.room.getState() == "DIRTY"):
                self.suck(self)
                self.choose_room(randint(0, 1) )
            else:
                self.choose_room(randint(0, 1) )
                self.score +=1

        print("Efektiivsus Skoor: ", self.score)

    def choose_room(self, choice):
        if(choice == 0):
            self.right()
        else:
            self.left()








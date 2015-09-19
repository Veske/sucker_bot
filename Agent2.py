__author__ = 'Martin'

from random import randint

class Agent2:
    room = ""

    def __init__(self, rooms):
        self.rooms = rooms
        self.room = rooms[randint(0, 1)]
        self.score = 1
        self.cleaned_rooms = []

    def suck(self, room):
        print("State: Sucking Room:[",self.room.getName(),",",self.room.getState(),"]")
        self.room.cleanRoom()
        self.cleaned_rooms.append(self.room)

    def no_op(self):
        self.score += 1
        print("State: All rooms clean, In room:", self.room.getName())
        return "self.room"

    def left(self):
        self.score -= 1
        if(self.room.getName() != "A"):
            self.room = self.rooms[0]

        print("State: Moved to room ", self.room.getName(), "State after work: ", self.room.getState())
        return

    def right(self):
        self.score -= 1
        if(self.room.getName() != "B"):
            self.room = self.rooms[1]

        print("State: Moved to room ", self.room.getName(), "State after work: ", self.room.getState())
        return

    def run(self, steps = 10):
        for i in range(steps):
            self.score+=1
            if(self.room.getState() == "DIRTY"):
                self.suck(self.room)
            else:
                self.choose_room()

        print("Efektiivsus Skoor: ", self.score)

    def choose_room(self):
        if(self.rooms not in self.cleaned_rooms):
            for room in list(set(self.rooms)-set(self.cleaned_rooms)):
                if room.getState() == "DIRTY":
                    if(self.room != room):
                        self.change_room(room)
                        return
                    else:
                        self.suck(self.room)
                        return

            self.no_op()
        else:
            self.no_op()



    def change_room(self, room):
        if(room.getName()=="A"):
            self.left()
        else:
            self.right()
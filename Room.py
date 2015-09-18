__author__ = 'kaspar'

class Room:
    def __init__(self, name, state):
        self.name = name
        self.state = state

    def getName(self):
        return self.name

    def getState(self):
        return self.state

    def cleanRoom(self):
        self.state = "CLEAN"

    def dirtyRoom(self):
        self.state = "DIRTY"
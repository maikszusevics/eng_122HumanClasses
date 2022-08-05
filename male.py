# Creates class for male to inherit from Human
from human import Human


class Male(Human):
    # need to initialise class
    def __init__(self): # attributes here
        super().__init__() # used to inherit from parent
        self.__XY = True # this is a private attribute, cannot be called
        self.facial_hair = True
        self._employed = True # this is a protected attribute, it will not be listed
        self.name = input("name unassigned, assign: ")


    #behaviours:
    def sends_emails(self):
        return "He sending email!"

    def paternity_leave(self):
        return "he take care of dem kids"

    def earns_money(self):
        return "I sure hope he do"





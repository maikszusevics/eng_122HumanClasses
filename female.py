# Creates class for male to inherit from Human
from human import Human


class Female(Human):
    # need to initialise class
    def __init__(self): # attributes here
        super().__init__() # used to inherit from parent
        self.__XX = True
        self.facial_hair = False
        self._employed = True
        self.name = ("unassigned name")
        self.fertile = True

    #behaviours:
    def sends_emails(self):
        return "she sending email!"

    def maternity_leave(self):
        return "she take care of dem kids"

    def earns_money(self):
        return "At an equal rate to Male class"


h2 = Female()

print(h2.sends_emails())












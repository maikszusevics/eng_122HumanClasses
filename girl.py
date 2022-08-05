# Creates class for girl and imports female
from female import Female


class Girl(Female):
    # need to initialise class
    def __init__(self): # attributes here
        super().__init__() # used to inherit from parent
        self.fav_colour = "unassigned"
        self.parent_reliant = True
        self.schoolyear = 6
        self.fertile = False

    #behaviours:
    def plays(self):
        return "she playing with friends!"

    def studies(self):
        return "she works hard at school"

    def cartoon(self):
        return "she like adventure time the most"


youngXX = Girl()

print(youngXX.fav_colour)
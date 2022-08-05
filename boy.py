# Creates class for male to inherit from Human
from male import Male


class Boy(Male): # establishes Male class as parent
    # need to initialise class
    def __init__(self): # attributes here
        super().__init__() # used to inherit from Male class
        self.fav_colour = "unassigned"
        self.parent_reliant = True
        self.schoolyear = 6
        self.facial_hair = False # polymorphic reassign

    #behaviours:
    def plays(self):
        return "he playing with friends!"

    def studies(self):
        return "he works hard at school"

    def cartoon(self):
        return "He like spongebob the most"


youngXY = Boy()

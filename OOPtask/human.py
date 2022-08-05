# Creates class for human
class Human:
    # need to initialise class
    def __init__(self): # attributes here
        self.alive = True
        self.spine = True
        self.heart = True

    #behaviours:
    def sleep(self):
        return "people be sleepin"

    def breathe(self):
        return "people definitely be breathing"

    def eats(self):
        return "you need to eat to live"


person = Human()

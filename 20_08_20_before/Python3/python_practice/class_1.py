class Terran(object):
    def __init__(self, mineral):
        self.scv=4
        self.marine = 0
        self.medic = 0
        self.mineral = mineral
    def command(self, SCV=False):
        self.mineral += 8*self.scv
        if SCV:
            self.scv += 1
            self.mineral -= 10
    def barrack(self, Marine=False, Medic=False):
        self.mineral += 8*self.scv
        if Marine:
            self.marine += 1
            self.mineral -= 15
        if Medic:
            self.medic += 1
            self.mineral -= 25
    def check_source(self):
        print("Mineral:"+str(self.mineral))



User = Terran(50)
#print(User)
User.command(True)
#print(User.command(True))
User.barrack(True,True)
#print(User.barrack(True,True))
User.check_source()

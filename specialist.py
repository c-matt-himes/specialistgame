from IntroSpecialistMechanic import *
ran_num=5

#Diplomacy, Insurrection, Espionage, Martial, Leadership

class Specialist():
    def __init__(self,rank):
        self.diplo = ISV(1)
        self.insurrection = ISV(1)
        self.espionage = ISV(1)
        self.martial = ISV(1)
        self.leadership = ISV(1)

    def get_name(self):
        return self.name

    def TestCommand(self):
        print(f"{self} has {self.diplo} diplomacy, {self.insurrection} insurrection, {self.espionage} espionage, {self.martial} martial, {self.leadership} leadership")

class Diplomat(Specialist):
    def __init__(self,rank):
        super().__init__(rank)
        self.diplo = ISV(20)

class Guerilla(Specialist):
    def __init__(self,rank):
        super().__init__(rank)
        self.insurrection = ISV(20)

class Spy(Specialist):
    def __init__(self,rank):
        super().__init__(rank)
        self.espionage = ISV(20)

class Assassin(Specialist):
    def __init__(self,rank):
        super().__init__(rank)
        self.martial = ISV(20)

class Commander(Specialist):
    def __init__(self,rank):
        super().__init__(rank)
        self.leadership = ISV(20)

TestDiplo = Diplomat(1)
TestGuerilla = Guerilla(1)
TestSpy = Spy(1)
TestAssassin = Assassin(1)
TestCommander = Commander(1)


TestDiplo.TestCommand()
TestGuerilla.TestCommand()
TestSpy.TestCommand()
TestAssassin.TestCommand()
TestCommander.TestCommand()

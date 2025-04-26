from IntroSpecialistMechanic import *

#Diplomacy, Insurrection, Espionage, Martial, Leadership

class Specialist():
    def __init__(self,rank):
        self.diplo = ISV(1)
        self.insurrection = ISV(1)
        self.espionage = ISV(1)
        self.martial = ISV(1)
        self.leadership = ISV(1)

Test_Spec = Specialist(1)

print(Test_Spec.diplo, Test_Spec.insurrection, Test_Spec.espionage, Test_Spec.martial, Test_Spec.leadership)

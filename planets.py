from IntroSpecialistMechanic import *
ran_num=3
avg_raw_min = 5
avg_build = 8

class Planet():
    def __init__(self,avg_raw_min,avg_build):
        self.Raw_min = ISV(avg_raw_min)
        self.Build = ISV(avg_build)
        if self.Build < self.Raw_min:
            self.Build = self.Raw_min

    def Min_Display(self):
        print ("-" * self.Build)
        print ("-" * self.Raw_min)


TestPlanet1 = Planet(avg_raw_min,avg_build)
TestPlanet2 = Planet(avg_raw_min,avg_build)

TestPlanet1.Min_Display()
TestPlanet2.Min_Display()


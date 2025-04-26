import random
ran_num = 5

#Diplomacy, Insurrection, Espionage, Martial, Leadership

def Averaging(x):
    y = (x*2)//ran_num
    if y == 0:
        y = 1
    return y

def IntroSpecValue(y):
    x = y
    z = 0
    while x > 0:
        z += random.randint(0,ran_num)
        x -= 1
    return z

def ISV(x):
    return IntroSpecValue(Averaging(x))
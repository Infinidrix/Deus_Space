from math import pi
import numpy as np


class Orbit:

    g = 6.67408 * pow(10, -11)
    m1 = 50


    def __init__(self, semiaxis, eccent, m2):
        self.m2 = m2
        self.semiaxis = semiaxis
        self.eccent = eccent
        self.minoraxis= pow(((1 - pow(self.eccent, 2)) * pow(self.semiaxis, 2)), 0.5)

    def aphelion(self):
        aph = self.semiaxis * (1 + self.eccent)
        return aph

    def perhelion(self):
        per = self.semiaxis * (1 - self.eccent)
        return per

    def gravity(self):
       f = ((self.g * self.m1 *self. m2) / pow(r, 2))
       return f

    def velocity(self, r):
       v =  pow(self.g * self.m2 * ((2 / r) - (1 / self.semiaxis)), 0.5)
       return v

    def period(self): #distance of the star from the center of the orbit is a third of the majoraxis
        p = pow(((8*pi/(self.g*(self.m1+self.m2)))*pow((self.semiaxis/3), 3)), 0.5)
        return p

    def planetpose(self, r):
        h = 0
        k = 0
        y = 0
        x = r + (self.semiaxis/3)
        p =((pow((x - h), 2) // pow(self.semiaxis, 2)) + pow((y - k), 2) // pow(self.minoraxis, 2))
        if p==1:
            return x,y
        else:
            x =(self.semiaxis/3) - r
            return x,y
        #the center of the orbit is arbitrarily (0,0)


def checkpoint(x, y, a, b):

            # checking the equation of
            # ellipse with the given point
     p = (pow((x ), 2) // pow(a, 2)) + (pow((y ), 2) // pow(b, 2))

     return p






def main():

    planet_1 = Orbit(10,0.5, 1)
    planet_2 = Orbit(5, 0.3, 2)
    planet_list= [planet_1, planet_2]




    aph = planet_1.aphelion()
    per = planet_1.perhelion()
    print(planet_1.aphelion())
    print(planet_1.velocity(aph))

    print(planet_1.planetpose(aph))
    print(planet_2.planetpose(aph))

    print(planet_1.perhelion())
    print(planet_1.velocity(per))

    print(planet_1.period())
    print(planet_1.planetpose(per))

    for i in planet_list:
        a = i.semiaxis
        b = i.minoraxis
        for j in planet_list:
            if i != j:
                x, y = j.planetpose(aph)

                if (checkpoint(x, y, a, b) == 1):
                    print("collision immeninet")
                else:
                    pass



main()
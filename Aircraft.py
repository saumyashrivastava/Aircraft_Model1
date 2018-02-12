import matplotlib.pyplot as plt
import random


class Aircraft:
    def __init__(self, aircraft_model, x=0, y=0, acceleration=1,range=6100, speed=610):
        self.x = x
        self.y = y
        self.aircraft_model = aircraft_model
        self.acceleration = acceleration
        self.range = range
        self.speed = speed

    def return_all(self):
        return self


    def moving(self, xcord=0, ycord=0):
        self.x += xcord
        self.y += ycord

    def flightpathcalculation(self, x1, y1, x2, y2):
        m = (y2 - y1) / (x2 - x1)

        b = y1 - (m * x1)

        xtemp = x1
        flightpath = []
        while xtemp <= x2:
            ytemp = (m * xtemp) + b
            flightpath.append(tuple((xtemp, ytemp)))
            xtemp += 1
        self.flightpath = flightpath

        # plt.figure(figsize=(8,8))
        #plt.plot([x1, y1], [x2, y2])
        #plt.show()


class Boeing747(Aircraft):
    def __init__(self, aircraft_model, x2=0, y2=0, range=6100, speed=610, acceleration=1):
        self.aircraft_model = aircraft_model
        self.x2 = x2
        self.y2 = y2
        self.acceleration = acceleration
        self.range = range
        self.speed = speed

    def return_all(self):
        return self


class PrivateJet(Aircraft):
    def __init__(self, aircraft_model, x2=0,y2=0,range=7100, speed=710, acceleration=1):
        self.aircraft_model = aircraft_model
        self.x2 = x2
        self.y2 = y2
        self.acceleration = acceleration
        self.range = range
        self.speed = speed

    def return_all(self):
        return self

flights = []


b1 = Boeing747("Boeing-741")
b1_1= 12
b1_2= 10
b1_3= 13
b1_4= 24
b1.flightpathcalculation(b1_1,b1_2,b1_3,b1_4)
flights.append(b1)
plt.plot([b1_1, b1_2], [b1_3, b1_4])


b1 = Boeing747("Boeing-742")
b1_1= 11
b1_2= 50
b1_3= 32
b1_4= 78
b1.flightpathcalculation(b1_1,b1_2,b1_3,b1_4)
flights.append(b1)
plt.plot([b1_1, b1_2], [b1_3, b1_4])


b1 = Boeing747("Boeing-743")
b1_1= 25
b1_2= 80
b1_3= 29
b1_4= 83
b1.flightpathcalculation(b1_1,b1_2,b1_3,b1_4)
flights.append(b1)
plt.plot([b1_1, b1_2], [b1_3, b1_4])


b1 = Boeing747("Boeing-744")
b1_1= 61
b1_2= 83
b1_3= 65
b1_4= 83
b1.flightpathcalculation(b1_1,b1_2,b1_3,b1_4)
flights.append(b1)
plt.plot([b1_1, b1_2], [b1_3, b1_4])


b1 = Boeing747("Boeing-745")
b1_1= 4
b1_2= 16
b1_3= 6
b1_4= 40
b1.flightpathcalculation(b1_1,b1_2,b1_3,b1_4)
flights.append(b1)
plt.plot([b1_1, b1_2], [b1_3, b1_4])


b1 = Boeing747("Boeing-746")
b1_1= 56
b1_2= 43
b1_3= 64
b1_4= 52
b1.flightpathcalculation(b1_1,b1_2,b1_3,b1_4)
flights.append(b1)
plt.plot([b1_1, b1_2], [b1_3, b1_4])


b1 = Boeing747("Boeing-747")
b1_1= 10
b1_2= 86
b1_3= 30
b1_4= 90
b1.flightpathcalculation(b1_1,b1_2,b1_3,b1_4)
flights.append(b1)
plt.plot([b1_1, b1_2], [b1_3, b1_4])


b1 = PrivateJet("PrivateJet1")
b1_1= 4
b1_2= 9
b1_3= 19
b1_4= 92
b1.flightpathcalculation(b1_1,b1_2,b1_3,b1_4)
flights.append(b1)
plt.plot([b1_1, b1_2], [b1_3, b1_4])


b1 = PrivateJet("PrivateJet2")
b1_1= 17
b1_2= 5
b1_3= 19
b1_4= 58
b1.flightpathcalculation(b1_1,b1_2,b1_3,b1_4)
flights.append(b1)
plt.plot([b1_1, b1_2], [b1_3, b1_4])


b1 = PrivateJet("PrivateJet3")
b1_1= 13
b1_2= 9
b1_3= 56
b1_4= 46
b1.flightpathcalculation(b1_1,b1_2,b1_3,b1_4)
flights.append(b1)
plt.plot([b1_1, b1_2], [b1_3, b1_4])



for f in flights:
    obj = f.return_all()
    path = obj.flightpath
    length_of_path = len(path)
    print "Object Model :",obj.aircraft_model
    print "Range :",obj.range
    print "Max_Speed :",obj.speed
    print "Acceleration :', '1"
    print "Aircraft Start Position :" ,path[0]
    print "Aircraft End Position :",path[length_of_path-1]
    print "Flight Path :", path

plt.show()


class vehicle:
    nooftyres = 4

class vehicle2:
    noofheadlights = 2


class car(vehicle,vehicle2):
    def showcar(self):
        print(f"the no of tyres in the car is {vehicle.nooftyres}\n the no of headlights are {vehicle2.noofheadlights}")


c = car()
c.showcar()

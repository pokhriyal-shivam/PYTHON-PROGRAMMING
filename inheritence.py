class vehicle:
    nooftyres = 4


class car(vehicle):
    def showcar(self):
        print(f"the no of tyres in the car is {vehicle.nooftyres}")


c = car()
c.showcar()

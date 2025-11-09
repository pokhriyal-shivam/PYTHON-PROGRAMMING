class Vehicle:
    no_of_tyres = 4
    vehicle_type = "Four Wheeler"


class Car(Vehicle):   # inherits from Vehicle
    def show_car(self):
        print("Car is a", self.vehicle_type)
        print("It has", self.no_of_tyres, "tyres.")


class SportsCar(Car):  # inherits from Car
    def show_sportscar(self):
        print("Sports car details:")
        print("Type:", self.vehicle_type)
        print("Tyres:", self.no_of_tyres)
        print("Speed: 320 km/h")


# Object of SportsCar
s = SportsCar()

print("--- Car Details ---")
s.show_car()

print("\n--- Sports Car Details ---")
s.show_sportscar()

from vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, name, year, color, plate, estimatedPrice, condition, fuelLevel):
        super().__init__(name, year, color, plate, estimatedPrice, condition)
        self.fuelLevel = fuelLevel  # percentage

def details(self):
        return f"{self.name} ({self.year}) - {self.color} - {self.license_plate} - R$ {self.price} - {self.condition}"
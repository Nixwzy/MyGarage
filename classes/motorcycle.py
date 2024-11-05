from vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, name, year, color, plate, estimatedPrice, condition, cylinderCapacity, fuelLevel):
        super().__init__(name, year, color, plate, estimatedPrice, condition)
        self.cylinderCapacity = cylinderCapacity  # Cilindrada
        self.fuelLevel = fuelLevel  # percentage

def details(self):
        return f"{self.name} ({self.year}) - {self.color} - {self.license_plate} - R$ {self.price} - {self.condition}"
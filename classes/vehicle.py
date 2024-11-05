class Vehicle:
    def __init__(self, name, year, color, plate, estimatedPrice, condition):
        self.name = name # brand + model
        self.year = year
        self.color = color 
        self.plate = plate  
        self.estimatedPrice = estimatedPrice 
        self.condition = condition

def details(self):
        return f"{self.name} ({self.year}) - {self.color} - {self.license_plate} - R$ {self.price} - {self.condition}"
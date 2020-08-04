class vehicles :
    def __init__(self,ID,brand,model,year,color,vehicle_type,base_cost):
        self.ID = ID
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.vehicle_type = vehicle_type
        self.base_cost = base_cost
    
class Sedan(vehicles) :
    def __init__(self,ID,brand,model,year,color,vehicle_type,base_cost):
        super().__init__(ID,brand,model,year,color,vehicle_type,base_cost)
        self.base_cost = base_cost + 50
        self.vehicle_type = "sedan"
        self.is_rented = bool(False)

    def create_vehicle(self):
        return {"ID": self.ID, "brand": self.brand, "model":self.model,"year":self.year,"color":self.color,"type":self.vehicle_type,"cost":self.base_cost,"is_rented":self.is_rented}

class SUV(vehicles) :
    def __init__(self,ID,brand,model,year,color,vehicle_type,base_cost):
        super().__init__(ID,brand,model,year,color,vehicle_type,base_cost)
        self.base_cost = base_cost + 100
        self.vehicle_type = "SUV"
        self.is_rented = bool(False)

    def create_vehicle(self):
        return {"ID": self.ID, "brand": self.brand, "model":self.model,"year":self.year,"color":self.color,"type":self.vehicle_type,"cost":self.base_cost,"is_rented":self.is_rented}

class Coupe(vehicles) :
    def __init__(self,ID,brand,model,year,color,vehicle_type,base_cost):
        super().__init__(ID,brand,model,year,color,vehicle_type,base_cost)
        self.base_cost = base_cost + 75
        self.vehicle_type = "coupe"
        self.is_rented = bool(False)

    def create_vehicle(self):
        return {"ID": self.ID, "brand": self.brand, "model":self.model,"year":self.year,"color":self.color,"type":self.vehicle_type,"cost":self.base_cost,"is_rented":self.is_rented}

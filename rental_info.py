class rental_info:
    def __init__(self,vehicle_id,vehicle_name,customer_id,rental_date,rental_price,is_active):
        self.vehicle_id = vehicle_id
        self.vehicle_name = vehicle_name
        self.customer_id = customer_id
        self.rental_date = rental_date
        self.rental_price = rental_price
        self.is_active = is_active

    def add_rental_info(self):
        return{"vehicle_id":self.vehicle_id,"vehicle_name":self.vehicle_name,"customer_id":self.customer_id,"rental_date":self.rental_date,"rental_price":self.rental_price,"is_active":self.is_active}


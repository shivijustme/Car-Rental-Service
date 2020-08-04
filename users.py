class Users :
    def __init__(self, ID, username, password):
        self.ID = ID
        self.username = username
        self.password = password
    
class Admin_users(Users) :
    def __init__(self,ID, username, password):
        super().__init__(ID, username, password)
        self.user_type = "admin"
        
    def sign_up(self):
        return {"ID": self.ID,"username":self.username,"password":self.password,"user_type":self.user_type}

class Customer_users(Users) :
    def __init__(self,ID, username, password, name, address, phone):
        super().__init__(ID, username, password)
        self.name = name
        self.address = address
        self.phone = int(phone)
        self.user_type = "customer"
        self.has_rented = bool(False)

    def sign_up(self):
        return{"ID": self.ID, "username":self.username,"password":self.password,"user_type": self.user_type,"name": self.name, "address":self.address,"phone":self.phone, "has_rented":self.has_rented}
        




# Car-Rental-Service
Python-MongoDB Project

Overview:
In this project, i will be writing a Python Application for a Car Rental Company. There will be two types of Users in your database - Customer Users and Admin Users. Customers will be able to rent cars and Admins will be able to add new cars to the inventory and manage Customers Users and Rentals.

Customer Users will be able to browse through a selection of vehicles that they can rent. The system will give them an option to choose the car type - Sedan, SUV, Coupe. The users will be able to choose the correct car based on car data such as Base Cost, Mileage, Brand, Model, Year and Color. Once a user chooses to rent a car, the car should no longer appear in the inventory of available cars. Customer Users will also be able to see what cars they have rented (in the past or at present) through the main menu.

Admin Users will be able to add new vehicles to the inventory by specifying properties such as Car Type, Base Cost, Mileage, Brand, Model, Year and Color. They will also be able to Delete/Edit vehicles. Admin Users will also be able to see all the Customer Users that exist in the database. Admin Users will be able to see a list of all the vehicles that are currently rented by any Customer User.

Requirements:
Users:
●	The application will have two types of users - Admin Users and Customer Users.
●	Both these user types will be child classes of User class and inherit properties such as Id, UserName, Password, UserType. The difference between the two users will be that Customers Users will also have additional properties - Name, Address, Phone, hasRented. hasRented will be False when the account is created and it will be set to True once a customer user rents a vehicle.  
●	Customer Users will only be able to View Data but Admin Users will be able to Add/Edit/Delete/View all data. 
Vehicles:
●	The parent Vehicle Class will have properties such as -  Id, Brand, Model, Year, Color, Type, Base Cost, Mileage and isRented
●	isRented property will be set to False by default and will only switch to True if that specific vehicle is currently Rented by a user.
●	Mileage is not a required property. Admin may or may not provide a value for this. All other properties are required. The Admin should not be able to Add a vehicle if any of the required properties are not specified.
●	The Child Classes will be - Sedan, SUV, Coupe. These will inherit all properties of Vehicle Class but the Base Cost will be different. Base cost will be in addition to the base cost entered by the Admin when creating the object. Additional base cost for Sedan = 50, Coupe = 75, SUV = 100.
Rental/RentalAgreement:
●	This object/class will store the information about which vehicle was rented to which user, at what date/time and for how much.
●	Properties will include - RentalId, RentalDateTime, RentalPrice, VehicleId, UserId, isActive. isActive will be set to True when a vehicle is rented and set to False when the rental is returned (will work on this part later, if time permits)

Workflow:
Application begins and prompts the User to use as Admin Version or Customer Version.
Admin Version:
●	Prompts the user to Create Account/Sign Up or Login.
●	User can create a new Admin account or simply login with an existing account.
●	User will be taken to the Main Menu. Main Menu options will be - Administer Vehicles, View Users, View Rentals.
●	Administer Vehicles SubMenu:
○	View All Vehicles - Display all Vehicles (isRented = True and isRented=False)
○	Add new Vehicle
○	Edit Vehicle using Id
○	Delete Vehicle using Id
●	View Users will display a list of all Customer Users
●	View Rentals will display all Rentals (isActive= True and isActive=False) sorted by latest rental first.

Customer Version:
●	Prompts the user to Create Account/Sign Up or Login.
●	User can create a new Customer account or simply login with an existing account.
●	User will be taken to the Main Menu. Main Menu options will be - View Vehicles, View My Rentals.
●	View Vehicles Sub-Menu:
○	View All Vehicles - Available vehicles only (isRented=False)
○	View Vehicles by VehicleType
○	User will be able to view select the vehicle they want to Rent.
○	The system will prompt confirmation of Rental Vehicle Selection.
○	After a user confirm Rental, the Rental/RentalAgreement Object will be created and isRented (in vehicle object) and hasRented (in user object) will be switched to True.
●	View My Rentals - All previous and current RentalAgreements for the given user will be displayed.

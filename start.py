from tkinter import *
import tkinter.messagebox
from random import randint

from users import *
from Vehicles import *
from rental_info import *

import tkinter 
from tkcalendar import *

import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://amogh:amogh@shivi-usyoc.mongodb.net/test?retryWrites=true&w=majority")

db = cluster["tkinter_1"]
collection = db["users"]

db_2 = cluster["tkinter_1"]
collection_2 = db_2["Vehicles"]

db_3 = cluster["tkinter_1"]
collection_3 = db_3["rental_info"]

def login_page():
    
    frame_login = Frame(start)
    frame_login.pack(side= TOP)
    frame_back = Frame(start)
    frame_back.pack(side = BOTTOM , anchor = SW)
    Button(frame_back, text="Back", width=4, height=1, activebackground = "grey", command = lambda:[frame_login.destroy(), frame_back.destroy(), begin()]).pack(side = BOTTOM)

    def message_box():
        user_object = collection.find({"username":username_login_entry.get(),'password': password_login_entry.get(),'user_type' : 'admin'})

        if user_object.count() == 0 :
            tkinter.messagebox.showerror('incorrect details','incorrect username or password')
            
        else :
            tkinter.messagebox.showinfo('Login status','you have been logged in')
            frame_login.destroy()
            frame_back.destroy()
            main_menu()
              

    Label(frame_login, text="Please enter login details").pack(side = TOP)

    Label(frame_login, text="").pack()
    Label(frame_login, text="Username").pack()
    username_login_entry = Entry(frame_login)
    username_login_entry.pack()
    
    Label(frame_login, text="").pack()
    Label(frame_login, text="Password").pack()
    password_login_entry = Entry(frame_login, show= '*')
    password_login_entry.pack()

    Label(frame_login, text="").pack()

    Button(frame_login, text="Submit", width=10, height=1, activebackground = "grey", command = lambda : [message_box()]).pack(pady = 5)
    Button(frame_login, text="Sign Up", width=10, height=1, activebackground = "grey", command = lambda : [frame_login.destroy() ,frame_back.destroy(), sign_up()]).pack()

def login_page_customer():
    
    frame_login = Frame(start)
    frame_login.pack(side= TOP)
    frame_back = Frame(start)
    frame_back.pack(side = BOTTOM , anchor = SW)
    Button(frame_back, text="Back", width=4, height=1, activebackground = "grey", command = lambda:[frame_login.destroy(), frame_back.destroy(), begin()]).pack(side = BOTTOM)
        
    def message_box():
        
        user_object = collection.find({"username":username_login_entry.get(),'password': password_login_entry.get(),'user_type' : 'customer'})
        global current_user_ID
        current_user_ID = collection.find_one({"username":username_login_entry.get(),'password': password_login_entry.get(),'user_type' : 'customer'})["ID"]
    
        if user_object.count() == 0 :
            tkinter.messagebox.showerror('incorrect details','incorrect username or password')
            
        else :
            tkinter.messagebox.showinfo('Login status','you have been logged in')
            frame_login.destroy()
            frame_back.destroy()
            main_menu_customer()
              

    Label(frame_login, text="Please enter login details").pack(side = TOP)

    Label(frame_login, text="").pack()
    Label(frame_login, text="Username").pack()
    username_login_entry = Entry(frame_login)
    username_login_entry.pack()
    
    Label(frame_login, text="").pack()
    Label(frame_login, text="Password").pack()
    password_login_entry = Entry(frame_login, show= '*')
    password_login_entry.pack()

    Label(frame_login, text="").pack()

    Button(frame_login, text="Submit", width=10, height=1, activebackground = "grey", command = lambda : [message_box()]).pack(pady = 5)
    Button(frame_login, text="Sign Up", width=10, height=1, activebackground = "grey", command = lambda : [frame_login.destroy() ,frame_back.destroy() ,sign_up_customer()]).pack()


def sign_up():

    frame_sign_up = Frame(start)
    frame_sign_up.pack(side= TOP)

    frame_back = Frame(start)
    frame_back.pack(side = BOTTOM , anchor = SW)
    Button(frame_back, text="Back", width=4, height=1, activebackground = "grey", command = lambda:[frame_sign_up.destroy(), frame_back.destroy(), login_page()]).pack(side = BOTTOM)

   
    def getvalues_2():
        
        add_user = Admin_users(randint(100000,999999), username_signup_entry.get(), password_signup_entry.get())
        collection.insert_one(add_user.sign_up())
    
        tkinter.messagebox.showinfo('Sign up status','your account has been created')

    Label(frame_sign_up, text="create your new account.").pack(side = TOP)

    Label(frame_sign_up, text="").pack()
    Label(frame_sign_up, text="Username").pack()
    username_signup_entry = Entry(frame_sign_up)
    username_signup_entry.pack()
    
    Label(frame_sign_up, text="").pack()
    Label(frame_sign_up, text="Password").pack()
    password_signup_entry = Entry(frame_sign_up, show= '*')
    password_signup_entry.pack()

    Label(frame_sign_up, text="").pack()

    Button(frame_sign_up, text="create account", width=13, height=1, activebackground = "grey", command = lambda : [getvalues_2()]).pack()

def sign_up_customer():

    frame_sign_up = Frame(start)
    frame_sign_up.pack(side= TOP)
    frame_back = Frame(start)
    frame_back.pack(side = BOTTOM , anchor = SW)
    Button(frame_back, text="Back", width=4, height=1, activebackground = "grey", command = lambda:[frame_sign_up.destroy(), frame_back.destroy(), login_page_customer()]).pack(side = BOTTOM)

    
   
    def getvalues_2():
        
        add_user = Customer_users(randint(100000,999999), username_signup_entry.get(), password_signup_entry.get(),name_signup_entry.get(),address_signup_entry.get(),phone_signup_entry.get())
        collection.insert_one(add_user.sign_up())

        tkinter.messagebox.showinfo('Sign up status','your account has been created')

    Label(frame_sign_up, text="create your new account.").pack(side = TOP)

    Label(frame_sign_up, text="").pack()
    Label(frame_sign_up, text="Username").pack()
    username_signup_entry = Entry(frame_sign_up)
    username_signup_entry.pack()
    
    Label(frame_sign_up, text="").pack()
    Label(frame_sign_up, text="Password").pack()
    password_signup_entry = Entry(frame_sign_up, show= '*')
    password_signup_entry.pack()

    Label(frame_sign_up, text="").pack()
    Label(frame_sign_up, text="Name").pack()
    name_signup_entry = Entry(frame_sign_up)
    name_signup_entry.pack()
    
    Label(frame_sign_up, text="").pack()
    Label(frame_sign_up, text="Address").pack()
    address_signup_entry = Entry(frame_sign_up)
    address_signup_entry.pack()

    Label(frame_sign_up, text="").pack()
    Label(frame_sign_up, text="Phone Number").pack()
    phone_signup_entry = Entry(frame_sign_up)
    phone_signup_entry.pack()

    Label(frame_sign_up, text="").pack()

    Button(frame_sign_up, text="create account", width=13, height=1, activebackground = "grey", command = lambda : [getvalues_2()]).pack()


def main_menu():
    
    frame_mainmenu = Frame(start)
    frame_mainmenu.pack(side= TOP)

    frame_back = Frame(start)
    frame_back.pack(side = BOTTOM , anchor = SW)
    Button(frame_back, text="Back", width=4, height=1, activebackground = "grey", command = lambda:[frame_mainmenu.destroy(), frame_back.destroy(), login_page()]).pack(side = BOTTOM)


    Label(frame_mainmenu, text="").pack()
    Label(frame_mainmenu, text="MAIN MENU", fg = "purple").pack()
    Label(frame_mainmenu, text="").pack()

    def administer_vehicles():
        frame_admin_vehicle = Frame(start)
        frame_admin_vehicle.pack(side = TOP)

        frame_back = Frame(start)
        frame_back.pack(side = BOTTOM , anchor = SW)
        Button(frame_back, text="Back", width=4, height=1, activebackground = "grey", command = lambda:[frame_admin_vehicle.destroy(), frame_back.destroy(), main_menu()]).pack(side = BOTTOM)


        Label(frame_admin_vehicle, text="").pack()
        Label(frame_admin_vehicle, text="ADMINISTER VEHICLES", fg = "purple").pack()
        Label(frame_admin_vehicle, text="").pack()

        Button(frame_admin_vehicle, text = "View all vehicles", width = 15, activebackground = "grey", command = lambda :[frame_admin_vehicle.destroy(),frame_back.destroy(), view_vehicles()]).pack(pady = 5)
        Button(frame_admin_vehicle, text = "Add new vehicle", width = 15, activebackground = "grey", command = lambda:[frame_admin_vehicle.destroy(),frame_back.destroy(), add_vehicles()]).pack(pady = 5)
        Button(frame_admin_vehicle, text = "Edit Vehicle", width = 15, activebackground = "grey", command = lambda :[frame_admin_vehicle.destroy(),frame_back.destroy(), edit_vehicles_1()]).pack(pady = 5)
        Button(frame_admin_vehicle, text = "Delete Vehicle", width = 15, activebackground = "grey", command = lambda :[frame_admin_vehicle.destroy(),frame_back.destroy(), delete_vehicles()]).pack(pady = 5)
        
            
        def view_vehicles():
            frame_view_vehicle = Frame(start)
            frame_d = Frame(start)
            frame_d.pack(side = TOP)
            frame_view_vehicle.pack(side = TOP, anchor = NW)

            frame_back = Frame(start)
            frame_back.pack(side = BOTTOM , anchor = SW)
            Button(frame_back, text="Back", width=4, height=1, activebackground = "grey", command = lambda:[frame_view_vehicle.destroy(),frame_d.destroy(), frame_back.destroy(), administer_vehicles()]).pack(side = BOTTOM)


            Label(frame_d, text="").pack()
            Label(frame_d, text="LIST OF VEHICLES", fg = "purple").pack()
            Label(frame_d, text="").pack()
            c = collection_2.find({},{"_id":0})
            i=1
            for d in c:
                Message(frame_view_vehicle, text =str(i) + ". \nBrand     \t : " + d["brand"] + "\nModel    \t : " +d["model"] + "\nIs rented  : " + str(d["is_rented"]), width = 170,  ).pack(side = TOP,anchor = W)
                i=i+1

        def add_vehicles():
            frame_add_vehicle = Frame(start)
            frame_add_vehicle.pack(side = TOP)

            frame_back = Frame(start)
            frame_back.pack(side = BOTTOM , anchor = SW)
            Button(frame_back, text="Back", width=4, height=1, activebackground = "grey", command = lambda:[frame_add_vehicle.destroy(), frame_back.destroy(), administer_vehicles()]).pack(side = BOTTOM)


            Label(frame_add_vehicle, text="").pack()
            Label(frame_add_vehicle, text="ENTER VEHICLE DETAILS", fg = "purple").pack()
            Label(frame_add_vehicle, text="").pack()

            def getvalues_3():
                
                vehicle_type.get()

                if(vehicle_type.get() == "sedan"):
                    add_vehicle = Sedan(int(ID.get()),brand.get(),model.get(),int(year.get()),color.get(),vehicle_type.get(),int(cost.get()))
                    collection_2.insert_one(add_vehicle.create_vehicle())
                    tkinter.messagebox.showinfo('Vehicle status','Vehicle has been added.')


                if(vehicle_type.get() == "SUV"):
                    add_vehicle = SUV(int(ID.get()),brand.get(),model.get(),int(year.get()),color.get(),vehicle_type.get(),int(cost.get()))
                    collection_2.insert_one(add_vehicle.create_vehicle())
                    tkinter.messagebox.showinfo('Vehicle status','Vehicle has been added.')

                if(vehicle_type.get() == "coupe"):
                    add_vehicle = Coupe(int(ID.get()),brand.get(),model.get(),int(year.get()),color.get(),vehicle_type.get(),int(cost.get()))
                    collection_2.insert_one(add_vehicle.create_vehicle())
                    tkinter.messagebox.showinfo('Vehicle status','Vehicle has been added.')                
                
            
            Label(frame_add_vehicle, text="").pack()
            Label(frame_add_vehicle, text="ID :").pack()
            ID = Entry(frame_add_vehicle)
            ID.pack()

            Label(frame_add_vehicle, text="").pack()
            Label(frame_add_vehicle, text="Brand :").pack()
            brand = Entry(frame_add_vehicle)
            brand.pack()

            Label(frame_add_vehicle, text="").pack()
            Label(frame_add_vehicle, text="Model :").pack()
            model = Entry(frame_add_vehicle)
            model.pack()

            Label(frame_add_vehicle, text="").pack()
            Label(frame_add_vehicle, text="Year :").pack()
            year = Entry(frame_add_vehicle)
            year.pack()

            Label(frame_add_vehicle, text="").pack()
            Label(frame_add_vehicle, text="Colour :").pack()
            color = Entry(frame_add_vehicle)
            color.pack()

            Label(frame_add_vehicle, text="").pack()
            Label(frame_add_vehicle, text="Type :").pack()
            vehicle_type = Entry(frame_add_vehicle)
            vehicle_type.pack()

            Label(frame_add_vehicle, text="").pack()
            Label(frame_add_vehicle, text="Cost :").pack()
            cost = Entry(frame_add_vehicle)
            cost.pack()

            Label(frame_add_vehicle, text="").pack()
            Button(frame_add_vehicle, text="Add Vehicle", width=13, height=1, activebackground = "grey", command = lambda : [getvalues_3()]).pack(pady = 5)
            
        def edit_vehicles_1():
            frame_edit_vehicle = Frame(start)
            frame_edit_vehicle.pack(side = TOP)

            frame_back = Frame(start)
            frame_back.pack(side = BOTTOM , anchor = SW)
            Button(frame_back, text="Back", width=4, height=1, activebackground = "grey", command = lambda:[frame_edit_vehicle.destroy(), frame_back.destroy(), administer_vehicles()]).pack(side = BOTTOM)

            
            def getvalues_4():
                ID.get()
                i = int(ID.get())
            
                def edit_vehicles_2():
                    frame_edit_vehicle_2 = Frame(start)
                    frame_edit_vehicle_2.pack(side = TOP)

                    frame_back = Frame(start)
                    frame_back.pack(side = BOTTOM , anchor = SW)
                    Button(frame_back, text="Back", width=4, height=1, activebackground = "grey", command = lambda:[frame_edit_vehicle_2.destroy(), frame_back.destroy(), edit_vehicles_1()]).pack(side = BOTTOM)
                    
                    def getvalues_5():

                        vehicle_type.get()

                        if(vehicle_type.get() == "sedan"):
                            update_vehicle = Sedan(i,brand.get(),model.get(),int(year.get()),color.get(),vehicle_type.get(),int(cost.get()))
                            collection_2.update_one({"ID": i},{"$set":update_vehicle.create_vehicle()})
                            tkinter.messagebox.showinfo('Vehicle status','Vehicle has been updated.')

                        if(vehicle_type.get() == "SUV"):
                            update_vehicle = SUV(i,brand.get(),model.get(),int(year.get()),color.get(),vehicle_type.get(),int(cost.get()))
                            collection_2.update_one({"ID": i},{"$set":update_vehicle.create_vehicle()})
                            tkinter.messagebox.showinfo('Vehicle status','Vehicle has been updated.')

                        if(vehicle_type.get() == "coupe"):
                            update_vehicle = Coupe(i,brand.get(),model.get(),int(year.get()),color.get(),vehicle_type.get(),int(cost.get()))
                            collection_2.update_one({"ID": i},{"$set":update_vehicle.create_vehicle()})
                            tkinter.messagebox.showinfo('Vehicle status','Vehicle has been updated.')
                                
                    Label(frame_edit_vehicle_2, text="").pack()
                    Label(frame_edit_vehicle_2, text="Brand :").pack()
                    brand = Entry(frame_edit_vehicle_2)
                    brand.pack()

                    Label(frame_edit_vehicle_2, text="").pack()
                    Label(frame_edit_vehicle_2, text="Model :").pack()
                    model = Entry(frame_edit_vehicle_2)
                    model.pack()

                    Label(frame_edit_vehicle_2, text="").pack()
                    Label(frame_edit_vehicle_2, text="Year :").pack()
                    year = Entry(frame_edit_vehicle_2)
                    year.pack()

                    Label(frame_edit_vehicle_2, text="").pack()
                    Label(frame_edit_vehicle_2, text="Colour :").pack()
                    color = Entry(frame_edit_vehicle_2)
                    color.pack()

                    Label(frame_edit_vehicle_2, text="").pack()
                    Label(frame_edit_vehicle_2, text="Type :").pack()
                    vehicle_type = Entry(frame_edit_vehicle_2)
                    vehicle_type.pack()

                    Label(frame_edit_vehicle_2, text="").pack()
                    Label(frame_edit_vehicle_2, text="Cost :").pack()
                    cost = Entry(frame_edit_vehicle_2)
                    cost.pack()

                    Label(frame_edit_vehicle_2, text="").pack()
                    Button(frame_edit_vehicle_2, text="Edit Vehicle", width=13, height=1, activebackground = "grey", command = lambda : [getvalues_5()]).pack(pady = 5)

                vehicle_object = collection_2.find({"ID":i})
                if vehicle_object.count() == 0 :
                    tkinter.messagebox.showerror('Ivalid ID','Enter correct ID')

                else:
                    frame_edit_vehicle.destroy()
                    frame_back.destroy()
                    edit_vehicles_2()

            Label(frame_edit_vehicle, text="").pack()
            Label(frame_edit_vehicle, text="ENTER VEHICLE ID", fg = "purple").pack()
            Label(frame_edit_vehicle, text="").pack()

            Label(frame_edit_vehicle, text="").pack()
            Label(frame_edit_vehicle, text="ID :").pack()
            ID = Entry(frame_edit_vehicle)
            ID.pack()

            Label(frame_edit_vehicle, text="").pack()
            Button(frame_edit_vehicle, text="Edit Vehicle", width=13, height=1, activebackground = "grey", command = lambda : [getvalues_4()]).pack(pady = 5)
            
        def delete_vehicles():
            frame_h = Frame(start)
            frame_h.pack(side = TOP)

            frame_back = Frame(start)
            frame_back.pack(side = BOTTOM , anchor = SW)
            Button(frame_back, text="Back", width=4, height=1, activebackground = "grey", command = lambda:[frame_h.destroy(), frame_back.destroy(), administer_vehicles()]).pack(side = BOTTOM)

            Label(frame_h, text="").pack()
            Label(frame_h, text="ENTER VEHICLE ID", fg = "purple").pack()
            Label(frame_h, text="").pack()

            Label(frame_h, text="").pack()
            Label(frame_h, text="ID :").pack()
            ID = Entry(frame_h)
            ID.pack()

            def del_values():
                ID.get()
                j = int(ID.get())

                del_vehicle = collection_2.find({"ID":j})
                if del_vehicle.count() == 0 :
                    tkinter.messagebox.showerror('Ivalid ID','Enter correct ID')

                else :
                    collection_2.delete_one({"ID": j})
                    tkinter.messagebox.showinfo('Vehicle status','Vehicle Deleted')

            Label(frame_h, text="").pack()
            Button(frame_h, text="Delete Vehicle", width=13, height=1, activebackground = "grey", command = lambda : [del_values()]).pack(pady = 5)

    def view_users():
        frame_v = Frame(start)
        frame_v.pack(side = TOP)
        frame_w = Frame(start)
        frame_w.pack(side = TOP, anchor = NW)

        frame_back = Frame(start)
        frame_back.pack(side = BOTTOM , anchor = SW)
        Button(frame_back, text="Back", width=4, height=1, activebackground = "grey", command = lambda:[frame_v.destroy(), frame_w.destroy(), frame_back.destroy(), main_menu()]).pack(side = BOTTOM)

        Label(frame_v, text="").pack()
        Label(frame_v, text="LIST OF USERS", fg = "purple").pack()
        Label(frame_v, text="").pack()

        c = collection.find({"user_type":"customer"})
        i = 1
        for d in c :
            Message(frame_w, text = str(i) + ". \n" + "Customer Name   : " + d["name"]  + "\n" + "Vehicle rented \t: " + str(d["has_rented"]), width = 200 ).pack(side = TOP,anchor = W)
            i = i+1

    def view_rentals():
        frame_v = Frame(start)
        frame_v.pack(side = TOP)
        frame_w = Frame(start)
        frame_w.pack(side = TOP, anchor = NW)

        frame_back = Frame(start)
        frame_back.pack(side = BOTTOM , anchor = SW)
        Button(frame_back, text="Back", width=4, height=1, activebackground = "grey", command = lambda:[frame_v.destroy(), frame_w.destroy(), frame_back.destroy(), main_menu()]).pack(side = BOTTOM)

        Label(frame_v, text="").pack()
        Label(frame_v, text="LIST OF RENTALS", fg = "purple").pack()
        Label(frame_v, text="").pack()

        c = collection_2.find({})
        i = 1
        for d in c :
            Message(frame_w, text = str(i) + ". \n" + "Vehicle brand   : " + d["brand"] + "\n" + "Vehicle model  : " + d["model"] + "\n" + "Vehicle rented  : " + str(d["is_rented"]), width = 200 ).pack(side = TOP,anchor = W)
            i = i+1


    Button(frame_mainmenu, text = "Administer Vehicles", width = 15, activebackground = "grey", command = lambda :[frame_mainmenu.destroy(),frame_back.destroy(), administer_vehicles()]).pack(pady = 5)
    Button(frame_mainmenu, text = "View Users", width = 15, activebackground = "grey", command = lambda :[frame_mainmenu.destroy(),frame_back.destroy(), view_users()]).pack(pady = 5)
    Button(frame_mainmenu, text = "View Rentals", width = 15, activebackground = "grey", command = lambda :[frame_mainmenu.destroy(),frame_back.destroy(), view_rentals()]).pack(pady = 5)

def main_menu_customer():
    
    frame_a = Frame(start)
    frame_a.pack(side= TOP)

    frame_back = Frame(start)
    frame_back.pack(side = BOTTOM , anchor = SW)
    Button(frame_back, text="Back", width=4, height=1, activebackground = "grey", command = lambda:[frame_a.destroy(), frame_back.destroy(), login_page_customer()]).pack(side = BOTTOM)


    Label(frame_a, text="").pack()
    Label(frame_a, text="MAIN MENU", fg = "purple").pack()
    Label(frame_a, text="").pack()

    Button(frame_a, text = "View Vehicles", width = 15, activebackground = "grey", command = lambda :[frame_a.destroy(),frame_back.destroy(), view_vehicles_2()]).pack(pady = 5)
    Button(frame_a, text = "View My Rentals", width = 15, activebackground = "grey", command = lambda :[frame_a.destroy(),frame_back.destroy(), view_my_rentals()]).pack(pady = 5)
    
    def view_vehicles_2():

        frame_b = Frame(start)
        frame_b.pack(side = TOP)

        frame_back = Frame(start)
        frame_back.pack(side = BOTTOM , anchor = SW)
        Button(frame_back, text="Back", width=4, height=1, activebackground = "grey", command = lambda:[frame_b.destroy(), frame_back.destroy(), main_menu_customer()]).pack(side = BOTTOM)


        Label(frame_b, text="").pack()
        Label(frame_b, text="LIST OF VEHICLES", fg = "purple").pack()
        Label(frame_b, text="").pack()

        Button(frame_b, text = "View all vehicles", width = 15, activebackground = "grey", command = lambda :[frame_b.destroy(),frame_back.destroy(),view_all_vehicles()]).pack(pady = 5)
        Button(frame_b, text = "View vehicles by type", width = 15, activebackground = "grey", command = lambda:[frame_b.destroy(),frame_back.destroy(),view_vehicles_by_type()]).pack(pady = 5)

        def view_all_vehicles():

            frame_c = Frame(start)
            frame_c.pack(side = TOP)

            frame_back = Frame(start)
            frame_back.pack(side = BOTTOM , anchor = SW)
            Button(frame_back, text="Back", width=4, height=1, activebackground = "grey", command = lambda:[frame_c.destroy(), frame_back.destroy(), view_vehicles_2()]).pack(side = BOTTOM)


            Label(frame_c, text="").pack()
            Label(frame_c, text="LIST OF VEHICLES", fg = "purple").pack()
            Label(frame_c, text="").pack()

            c = collection_2.find({"is_rented":bool(False)})
            v = StringVar()

            for d in c :
                Radiobutton(frame_c,text = d["brand"] +" - " + d["model"] + "\nCost - Rs." + str(d["cost"]) , value = d["ID"],variable = v, padx = 5, justify = LEFT).pack(anchor = W)
                Message(frame_c,text = " ").pack()

            def get_values_vehicle():
                
                question = tkinter.messagebox.askyesno("Proceed","Do you want to rent this vehicle ?")

                if question == True:
                    
                    frame_d = Frame(start)
                    frame_d.pack(side = TOP)

                    frame_back = Frame(start)
                    frame_back.pack(side = BOTTOM , anchor = SW)
                    Button(frame_back, text="Back", width=4, height=1, activebackground = "grey", command = lambda:[frame_d.destroy(), frame_back.destroy(), view_all_vehicles()]).pack(side = BOTTOM)

                    
                    def dateval():

                        collection_2.update_one({"ID":float(v.get())},{"$set": {"is_rented":bool(True)}})
                        collection.update_one({"ID":current_user_ID},{"$set": {"has_rented":bool(True)}})
                        q = collection_2.find_one({"ID":float(v.get())})

                        insert_rental_info = rental_info(float(v.get()),q["brand"]+" "+q["model"],current_user_ID,str(a.get_date()),q["cost"],bool(True))
                        collection_3.insert_one(insert_rental_info.add_rental_info())
                        tkinter.messagebox.showinfo("Booked","The vehicle you selected has been rented to you.")
                        frame_d.destroy()
                        frame_back.destroy()
                        view_all_vehicles()

                    Label(frame_d,text = "Select Date").pack(padx = 10, pady = 10)
                    a = DateEntry(frame_d, width= 15, bg = "blue", fg = "red", borderwidth = 3)
                    a.pack()
                    Button(frame_d, text = "Click Here", command = lambda : [dateval()]).pack(pady = 5)            

                else:
                    view_all_vehicles()

            Button(frame_c, text = "Book", width = 15, activebackground = "grey", command = lambda :[frame_c.destroy(),frame_back.destroy(), get_values_vehicle()]).pack(pady = 5)

        def view_vehicles_by_type():

            frame_c = Frame(start)
            frame_c.pack(side = TOP)

            frame_back = Frame(start)
            frame_back.pack(side = BOTTOM , anchor = SW)
            Button(frame_back, text="Back", width=4, height=1, activebackground = "grey", command = lambda:[frame_c.destroy(), frame_back.destroy(), view_vehicles_2()]).pack(side = BOTTOM)


            Label(frame_c, text="").pack()
            Label(frame_c, text="CHOOSE VEHICLE TYPE", fg = "purple").pack()
            Label(frame_c, text="").pack()

            vehicle_type_list = ["sedan","SUV","coupe"]
            clicked = StringVar()
            clicked.set(vehicle_type_list[0])

            OptionMenu(frame_c,clicked,*vehicle_type_list).pack()
            Label(frame_c, text="").pack()
            Button(frame_c, text = "Show vehicles", command = lambda :[frame_c.destroy(),frame_back.destroy(),chosen_type()]).pack(pady = 5)

            def chosen_type():
                frame_c = Frame(start)
                frame_c.pack(side = TOP)

                frame_back = Frame(start)
                frame_back.pack(side = BOTTOM , anchor = SW)
                Button(frame_back, text="Back", width=4, height=1, activebackground = "grey", command = lambda:[frame_c.destroy(), frame_back.destroy(), view_vehicles_2()]).pack(side = BOTTOM)

                vehicle_type = collection_2.find({"is_rented":bool(False),"type":str(clicked.get()) })
                v = StringVar()

                for vehicle in vehicle_type :
                    Radiobutton(frame_c,text = vehicle["brand"] +" - " + vehicle["model"] + "\nCost - Rs." + str(vehicle["cost"]) , value = vehicle["ID"],variable = v, padx = 5, justify = LEFT).pack(anchor = W)
                    Message(frame_c,text = " ").pack()

                def get_values_vehicle():
                    
                    question = tkinter.messagebox.askyesno("Proceed","Do you want to rent this vehicle ?")

                    if question == True:
                        
                        frame_d = Frame(start)
                        frame_d.pack(side = TOP)

                        frame_back = Frame(start)
                        frame_back.pack(side = BOTTOM , anchor = SW)
                        Button(frame_back, text="Back", width=4, height=1, activebackground = "grey", command = lambda:[frame_d.destroy(), frame_back.destroy(), view_all_vehicles()]).pack(side = BOTTOM)

                        def dateval():

                            collection_2.update_one({"ID":float(v.get())},{"$set": {"is_rented":bool(True)}})
                            collection.update_one({"ID":current_user_ID},{"$set": {"has_rented":bool(True)}})
                            q = collection_2.find_one({"ID":float(v.get())})

                            insert_rental_info = rental_info(float(v.get()),q["brand"]+" "+q["model"],current_user_ID,str(a.get_date()),q["cost"],bool(True))
                            collection_3.insert_one(insert_rental_info.add_rental_info())
                            tkinter.messagebox.showinfo("Booked","The vehicle you selected has been rented to you.")
                            frame_d.destroy()
                            frame_back.destroy()
                            view_all_vehicles()

                        Label(frame_d,text = "Select Date").pack(padx = 10, pady = 10)
                        a = DateEntry(frame_d, width= 15, bg = "blue", fg = "red", borderwidth = 3)
                        a.pack()
                        Button(frame_d, text = "Click Here", command = lambda : [dateval()]).pack(pady = 5)            

                    else:
                        chosen_type()

                Button(frame_c, text = "Book", width = 15, activebackground = "grey", command = lambda :[frame_c.destroy(),frame_back.destroy(), get_values_vehicle()]).pack(pady = 5)

    def view_my_rentals():

        frame_b = Frame(start)
        frame_b.pack(side = TOP)

        frame_back = Frame(start)
        frame_back.pack(side = BOTTOM , anchor = SW)
        Button(frame_back, text="Back", width=4, height=1, activebackground = "grey", command = lambda:[frame_b.destroy(), frame_back.destroy(), main_menu_customer()]).pack(side = BOTTOM)

        Label(frame_b, text="").pack()
        Label(frame_b, text="MY RENTALS", fg = "purple").pack()
        Label(frame_b, text="").pack()

        rental_info = collection_3.find({"customer_id":current_user_ID})

        i = 1
        for vehicle in rental_info :
            Message(frame_b, text = str(i) + ". \n" + "Vehicle Name   : " + vehicle["vehicle_name"]  + "\n" + "Customer ID     : " + str(vehicle["customer_id"]) + "\n" + "Rental Date       : " + vehicle["rental_date"] + "\n" + "Is Active            : " + str(vehicle["is_active"]), width = 200 ).pack(side = TOP,anchor = W)
            i = i+1

               
start = Tk()
start.geometry("500x425")
frame_begin = Frame(start)
frame_begin.pack()
def begin():
    frame_begin.destroy()
    frame_start = Frame(start)
    frame_start.pack()
    Label(frame_start, text="Select your user type :").pack()
    Label(frame_start, text="").pack()
    Button(frame_start, text="Admin", width=10, height=1, activebackground = "grey", command = lambda : [frame_start.destroy(), login_page()]).pack(side = TOP, pady = 5)
    Button(frame_start, text="Customer", width=10, height=1, activebackground = "grey", command = lambda : [frame_start.destroy(), login_page_customer()]).pack(side = TOP, pady = 5)

begin()
start.mainloop()
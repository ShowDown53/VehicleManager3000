#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Car import Car

vehicle1 = Car("Dacia", "1300", "1200000", "1989/02/30")
vehicle2 = Car("BMW", "i3", "6151", "2015/05/01")
vehicle3 = Car("Fičo", "Turbo Beštija", "6666", "1966/06/06")
vehicle4 = Car("Honda", "Ftec", "3.14", "It doesn't need servicing yo")

vehicles = [vehicle1, vehicle2, vehicle3, vehicle4]

def list_vehicles(vehicles):
    for index, vehicle in enumerate(vehicles):
        print "%s| %s %s with %s miles on the clock. Last serviced: %s" % (index+1, vehicle.make, vehicle.model, vehicle.mileage, vehicle.service_date)

    if not vehicles:
        print "You have no vehicles in your aplication. Select option 'b' to add a vehicle."

def add_vehicle(vehicles):
    make = raw_input("Please enter the vehicle make: ")
    model = raw_input("Please enter the vehicle model: ")
    mileage = raw_input("Enter the current odometer reading: ")
    service_date = raw_input("Please enter the date of the last service (YYYY/MM/DD): ")

    new_vehicle = Car(make=make, model=model, mileage=mileage, service_date=service_date)
    vehicles.append(new_vehicle)

    print  "%s %s was added to your vehicles." % (make, model)

def edit_mileage(vehicles):
    print "Here is the list of your vehicles: "

    for index, vehicle in enumerate(vehicles):
        print str(index+1) + "| " + vehicle.make + " " + vehicle.model

    vehicle_id = raw_input("Which vehicle's odometer reading would you like to edit? Enter the number next to the vehicle: ")
    id_transform = vehicles[int(vehicle_id) - 1]

    updated_mileage = raw_input(("Please enter the new odometer reading for %s %s: ") % (id_transform.make, id_transform.model))
    id_transform.mileage = updated_mileage
    print "Mileage for %s %s updated." % (id_transform.make, id_transform.model)
    print ""

def edit_service_date(vehicles):
    print "Here is the list of your vehicles: "

    for index, vehicle in enumerate(vehicles):
        print str(index+1) + "| " + vehicle.make + " " + vehicle.model

    vehicle_id = raw_input("Which vehicle's last service would you like to edit? Enter the number next to the vehicle: ")
    id_transform = vehicles[int(vehicle_id) - 1]

    updated_service_date = raw_input(("Please enter the last service date %s %s: ") % (id_transform.make, id_transform.model))
    id_transform.service_date = updated_service_date
    print "Service date for %s %s updated." % (id_transform.make, id_transform.model)
    print ""

def delete_vehicle(vehicles):
    print "Here is the list of your vehicles: "

    for index, vehicle in enumerate(vehicles):
        print str(index + 1) + "| " + vehicle.make + " " + vehicle.model

    print ""
    vehicle_id = raw_input("Which vehicle would you like to delete? Enter the number next to the vehicle: ")
    id_transform = vehicles[int(vehicle_id) - 1]

    vehicles.remove(id_transform)
    print ""
    print "Vehicle %s %s was removed." % (id_transform.make, id_transform.model)

def save_2_file(vehicles):
    with open("ListOfCars.txt", "w+") as ListOfCars:
        ListOfCars.write("This is the list of your cars:\n\n")
        i = 1
        for index, vehicle in enumerate(vehicles):
            ListOfCars.write(str(i) + "| " + vehicle.make + " " + vehicle.model +  " with " + vehicle.mileage +  " miles on the clock. Last serviced: " + vehicle.service_date + "\n")
            i += 1
        ListOfCars.write("\nList created with Vehicle Manager 3000. (v0.1)")


print "Hi! I'm Vehicle Manager 3000."

while True:
    print ""
    print "Please select one of the options listed below:"
    print "A| See a list of all vehicles"
    print "B| Add a new vehicle"
    print "C| Delete a vehicle"
    print "D| Edit a vehicle's current odometer reading"
    print "E| Edit the last service date for a vehicle"
    print "F| Save vehicle date to TXT file"
    print "G| Close program"
    print ""

    choose = raw_input("Choose an option from A to G: ")

    if choose.lower() == "a":
        list_vehicles(vehicles)
    elif choose.lower() == "b":
        add_vehicle(vehicles)
    elif choose.lower() == "c":
        delete_vehicle(vehicles)
    elif choose.lower() == "d":
        edit_mileage(vehicles)
    elif choose.lower() == "e":
        edit_service_date(vehicles)
    elif choose.lower() == "f":
        save_2_file(vehicles)
    elif choose.lower() == "g":
        print "Thanks for using Vehicle Manager 3000!"
        break

    else:
        print "You didn't enter a valid choice. Choose an option from A to G."
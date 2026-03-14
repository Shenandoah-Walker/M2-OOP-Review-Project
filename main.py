#Parking Ticket Simulation test file

from ParkedCar import ParkedCar
from ParkingMeter import ParkingMeter
from PoliceOfficer import PoliceOfficer

#Scenario 1: A car is parked legally (within purchased time)
print("\n=== Scenario 1: Car Parked Legally ===")

#Create a ParkedCar object
car1 = ParkedCar("Toyota", "Camry", "Red", "XYZ123", 30)

#Create a ParkingMeter object
meter1 = ParkingMeter(40)

#Create a PoliceOfficer object
officer1 = PoliceOfficer("John Doe", 5678)

#Officer inspects the car (create a ticket object)
ticket1 = officer1.inspect_car(car1, meter1)

#Since the car is parkede legally, no ticket should be issued
if ticket1 is None:
    print("Car is legally parked. No ticket issued.")
else:
    print(ticket1)

#Scenario 2: A car is parked illegally with less than 1 hour over the purchased time
print("\n=== Scenario 2: Car Parked Illegally (Less Than 1 Hour Over) ===")

#Create a ParkedCar object
car2 = ParkedCar("Honda", "Accord", "Blue", "ABC987", 70)

#Create a ParkingMeter object
meter2 = ParkingMeter(60)

#Create a PoliceOfficer object
officer2 = PoliceOfficer("Jane Smith", 1234)

#Officer inspects the car
ticket2 = officer2.inspect_car(car2, meter2)

#Since the car is parked illegally, a ticket should be issued. If it is not, print an error message.
if ticket2 is None:
    print("Error: Ticket should have been issued but wasn't.")
else:
    print("Ticket issued:")
    print(ticket2)

#Scenario 3: A car is parked illegally with more than 1 hour over the purchased time
print("\n=== Scenario 3: Car Parked Illegally (Multiple Hours Over) ===")

#Create a ParkedCar object
car3 = ParkedCar("Ford", "Mustang", "Black", "LMN456", 190)

#Create a ParkingMeter
meter3 = ParkingMeter(60)

#Create a PoliceOfficer
officer3 = PoliceOfficer("James Brown", 4321)

#Officer inspects the car
ticket3 = officer3.inspect_car(car3, meter3)

#Since the car is parked illegally, a ticket should be issued
if ticket3 is None:
    print("Error: Ticket should have been issued but wasn't.")
else:
    print("Ticket issued:")
    print(ticket3)

#Scenario 4: Multiple cars in a parking lot
print("\n=== Scenario 4: Multiple Cars in a Parking Lot ===")

#Create a list of ParkedCar objects
cars = [
    ParkedCar("Nissan", "Altima", "White", "AAA111", 20),   #A legal car
    ParkedCar("Chevy", "Malibu", "Silver", "BBB222", 45),   #A legal car
    ParkedCar("Kia", "Soul", "Green", "CCC333", 75),        #A car parked less than 1 hour over
    ParkedCar("BMW", "X5", "Black", "DDD444", 125),         #A car parked more than 1 hour over
    ParkedCar("Audi", "A4", "Gray", "EEE555", 250)          #A car parked more than 1 hour over
]

#Create ParkingMeter objects for each car
meters = [
    ParkingMeter(30),
    ParkingMeter(50),
    ParkingMeter(60),
    ParkingMeter(60),
    ParkingMeter(60)
]

#Create one officer to check all the cars in the lot
lot_officer = PoliceOfficer("Sarah Green", 9999)

#Loop through all cars and inspect them. Print tickets as needed.
for i in range(len(cars)):
    print(f"\nInspecting Car #{i+1}")
    ticket = lot_officer.inspect_car(cars[i], meters[i])

    if ticket is None:
        print("Car is legally parked. No ticket issued.")
    else:
        print("Ticket issued:")
        print(ticket)

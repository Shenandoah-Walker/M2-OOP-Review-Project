from ParkingTicket import ParkingTicket

class PoliceOfficer:

   #This method takes inputs to create a PoliceOfficer object that contains the officer's name and badge number.
    def __init__(self, name, badge_number):
        self.__name = name
        self.__badge_number = badge_number

    #This method returns the officer's name.
    def get_name(self):
        return self.__name
       
   #This method returns the officer's badge number.
    def get_badge_number(self):
        return self.__badge_number

    #This method takes a ParkedCar object and a ParkingMeter object as arguments. It checks if the car's time has expired and if so, tells the ParkingTicket class to issue a ticket.
    def inspect_car(self, car, meter):
        parked = car.get_minutes_parked()
        purchased = meter.get_minutes_purchased()

        if parked > purchased:
            illegal_minutes = parked - purchased
            return ParkingTicket(car, self, illegal_minutes)
        else:
            return None

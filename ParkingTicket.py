import math

class ParkingTicket:

    #This method takes inputs to create a ParkingTicket object that contains the car, officer name, badge number, illegal minutes, and fine.
    def __init__(self, car, officer, illegal_minutes):
        self.__car = car
        self.__officer_name = officer.get_name()
        self.__badge_number = officer.get_badge_number()
        self.__illegal_minutes = illegal_minutes
        self.__fine = self.calculate_fine()

    #This method calculates the fine based on the number of illegal minutes.
    #The first hour costs $25 and each additional hour costs $10.
    def calculate_fine(self):
        hours = math.ceil(self.__illegal_minutes / 60)

        if hours == 1:
            return 25.0
        else:
            return 25.0 + (hours - 1) * 10.0

    #This method returns a string containing the ticket information.
    def __str__(self):
        return (
            "Car: " + str(self.__car) +
            "\nOfficer Name: " + self.__officer_name +
            "\nBadge Number: " + self.__badge_number +
            "\nIllegal Minutes: " + str(self.__illegal_minutes) +
            "\nFine: $" + str(self.__fine)
        )

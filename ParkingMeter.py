#Responsible for knowing:
#• Number of minutes of parking time purchased

class ParkingMeter:
    #This method takes inputs to create a ParkingMeter object that contains the number of minutes of parking time purchased.
    def __init__(self, minutes_purchased=60):
        self.set_minutes_purchased(minutes_purchased)

    #This method returns the number of minutes of parking time purchased.
    def get_minutes_purchased(self):
        return self.__minutes_purchased

    #This method sets the number of minutes of parking time purchased. It also validates the input to ensure it is a positive number.
    def set_minutes_purchased(self, minutes):
        try:
            if minutes <= 0:
                raise ValueError("Minutes purchased must be greater than 0.")
            self.__minutes_purchased = minutes
        except ValueError as e:
            print(e)



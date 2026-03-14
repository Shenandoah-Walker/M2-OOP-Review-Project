class ParkingTicket:

  #This method takes inputs to create a ParkingTicket object that contains the car, officer name, badge number, illegal minutes, and fine.
  def __init__(self, car: ParkedCar, officer: PoliceOfficer, illegal_minutes: int):
    self.__car = car
    self.__officer_name = officer.get_name()
    self.__badge_number = officer.get_badge_number()
    self.__illegal_minutes = illegal_minutes
    self.__fine = self.calculate_fine()

    calculate_fine(self):
     # Formula:
      #$25 for the first hour or part, + $10 for each additional hour or part
      #→ ceil(illegal_minutes / 60)
    #implementation
     hours = math.ceil(self.__illegal_minutes / 60)

     if hours == 1:
        self.__fine = 25

     else if  hours > 1:
        self.__fine = 25 + (hours - 1) * 10

     else:
       
     
class  PoliceOfficer:


  #This method takes inputs to create a PoliceOfficer object that contains the officer's name and badge number.

  def __init__(self, name, badge_number):
     self.__name = name
     self.__badge_number = badge_number

   #This method takes a ParkedCar object and a ParkingMeter object as arguments. It checks if the car's time has expired and if so, tells the ParkingTicket class to issue a ticket.

  def inspect_car(self, car, meter, illegal):
      if car.get_minutes_parked() > meter.get_minutes_purchased():
          illegal = True
          return illegal     
         
      else:
          print("No ticket issued.")
          return None


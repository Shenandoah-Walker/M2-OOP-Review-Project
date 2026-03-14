#ParkedCar class

class ParkedCar:
  #This method takes inputs to create a ParkedCar object that contains the make, model, color, license number, and minutes parked of a parked car.
  def __init__(self, make, model, color, license_number, minutes_parked = 60):
      self.__make = make
      self.__model = model
      self.__color = color
      self.__license_number = license_number
      self.set_minutes_parked(minutes_parked)

  #This method returns the minutes the car has been parked.
  def get_minutes_parked(self):
      return self.__minutes_parked

  #This method sets the minutes the car has been parked, validating that the number of minutes is positive.
  def set_minutes_parked(self, minutes):
      try:
          if minutes <= 0:
              raise ValueError("Minutes parked must be greater than 0.")
          self.__minutes_parked = minutes
      except ValueError as e:
          print(e)

  #This method returns a string containing the car's information.
  def __str__(self):
      return "Make: " + self.__make + "\nModel: " + self.__model + "\nColor: " + self.__color + "\nLicense Number: " + self.__license_number + "\nMinutes Parked: " + str(self.__minutes_parked)

  
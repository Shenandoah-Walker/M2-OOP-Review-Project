#Abtract BasicShape class

from abc import ABC, abstractmethod

class BasicShape(ABC):

  #This method will contain 2 protected attributes: area and name
   def __init__(self, area, name):
     self._area = area
     self._name = name

  #This method will return the area of the shape
   @property
   def area(self):
      return self._area

  #This method will set the area of the shape
   @area.setter
   def area(self, area):
      self._area = area
     
  #This method will return the name of the shape
   @property
   def name(self):
      return self._name

  #This method will set the name of the shape
   @name.setter
   def name(self, name):
      self._name = name

  #This method will calculate the area of the shape. It will be overridden by the subclasses
   @abstractmethod
   def calc_area(self):
      pass

  
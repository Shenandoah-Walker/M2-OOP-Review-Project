#Abtract BasicShape class

from abc import ABC, abstractmethod

class BasicShape(ABC):

  #This method will contain 2 protected attributes: area and name
   def __init__(self, area, name):
     self._area = area
     self._name = name

  #This method will return the area of the shape
   def getArea(self):
      return self._area
     
  #This method will return the name of the shape
   def getName(self):
      return self._name

  #This method will calculate the area of the shape. It will be overridden by the subclasses
   @abstractmethod
   def calc_area(self):
      pass

  
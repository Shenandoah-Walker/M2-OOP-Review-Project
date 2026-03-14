#Circle class

from BasicShape import BasicShape

class Circle(BasicShape):
   
   #This method will contain 3 protected attributes: x_center, y_center, and radius
   def __init__(self, x_center, y_center, radius, name = "Circle"):
      self._x_center = x_center
      self._y_center = y_center
      self._radius = radius
      super().__init__(0, name)
      self.calc_area()

   #This method will calculate the area of the circle
   def calc_area(self):
      self._area = 3.14 * self._radius * self._radius

  #This method will return the x coordinate of the center of the circle
   @property
   def x_center(self):
      return self._x_center
      
   #This method will return the y coordinate of the center of the circle
   @property
   def y_center(self):
      return self._y_center

   #This method will return the radius of the circle.
   @property
   def radius(self):
      return self._radius

   #This method will set the radius of the circle.
   @radius.setter
   def radius(self, value):
       self._radius = value
       self.calc_area()
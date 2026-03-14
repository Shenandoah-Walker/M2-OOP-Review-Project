#Rectangle class

from BasicShape import BasicShape

class Rectangle(BasicShape):

  def __init__(self, length, width, name = "Rectangle"):
     self._length = length
     self._width = width
     super().__init__(0, name)
     self.calc_area()

 #This method will calculate the area of the rectangle
  def calc_area(self):
      self._area = self._length * self._width

  #This method will return the length of the rectangle
  @property
  def length(self):
     return self._length

  #This method will set the length of the rectangle
  @length.setter
  def length(self, length):
     self._length = length
     self.calc_area()

  #This method will return the width of the rectangle
  @property
  def width(self):
      return self._width

  #This method will set the width of the rectangle
  @width.setter
  def width(self, width):
     self._width = width
     self.calc_area()


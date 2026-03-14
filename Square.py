#Square class

from Rectangle import Rectangle

class Square(Rectangle):

   #This method will contain 1 protected attribute: side
   def __init__(self, side, name = "Square"):
      self._side = side
      super().__init__(side, side, name)
      self.name = name


  #This method will return the side of the square
   @property
   def side(self):
       return self._side

  #This method will set the side of the square
   @side.setter
   def side(self, side):
      self._side = side
      self.length = side
      self.width = side




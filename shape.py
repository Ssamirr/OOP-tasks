import math

class Shape():
  def __init__(self,color,filled):
    self.color = color
    if filled == True:
        self.filled = "filled"
    else:
        self.filled = "not filled"

  def toString(self):
    return f"A Shape with color of {self.color} and {self.filled}"

shape = Shape("green",True)
print(shape.toString())
  
class Circle(Shape):
  def __init__(self,radius):
    self.radius = radius
  
  def getArea(self):
    return f"Area Circle-{3.14*math.pow(self.radius,2)}"
  def getPerimeter(self):
    return f"Perimeter Circle-{2*3.14*self.radius}"

  def toString(self,obj):
    return f"A Circle with radius={self.radius}, which is a subclass of {obj.toString()}"

circle = Circle(5)
print(circle.toString(shape))

class Rectangle(Shape):
  def __init__(self,width,length):
    self.width = width
    self.length = length

  def getArea(self):
    return f"Area Rectangle-{self.width*self.length}"

  def getPerimeter(self):
    return f"Perimeter Rectangle-{2*(self.width+self.length)}" 

  def toString(self,obj2):
    return f"A Rectangle with width={self.width} and length={self.length}, which is a subclass of {obj2.toString()}"

rectangle = Rectangle(3,4)
print(rectangle.toString(shape))

class Square(Rectangle):
    def __init__(self,width,height):
        super().__init__(width,height)

square = Square(4,4)
print(square.getArea())
    
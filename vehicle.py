class Vehicle():
    positionX = 50
    positionY = 50
    speed = 60
    isOn = False

    def __init__(self,numofWheels,color,engine):
      self.numofWheels = numofWheels
      self.color = color
      self.engine = engine

    def accelerate(self):
      self.speed +=1

    def moveForward(self,x,y):
      self.positionX += x
      self.positionY += y

    def moveBackwards(self,x,y):
      self.positionX -= x
      self.positionY -= y

    def ignition():
      if self.isOn == False:
        self.isOn = True
      if self.isOn == True:
        self.isOn = False

    def getColor(self):
      print(self.color)

    def setColor(self,Color):
      self.color = Color

    def getNumofWheels(self):
      print(self.numofWheels)
    
    def setNumofWheels(self,num):
      self.numofWheels = num
    
    def __str__(self):
      print(f"NumofWheels={self.numofWheels}")
      print(f"Color={self.color}")
      print(f"Engine={self.engine}")
      print(f"PositionX={self.positionX}")
      print(f"PositionY={self.positionY}")
      print(f"Speed={self.speed}")
      print("Tamamlandi")


vehicle = Vehicle(4,'black',3)
vehicle.__str__()
vehicle.accelerate()
vehicle.moveForward(20,30)
vehicle.moveBackwards(20,10)
vehicle.setColor("Green")
vehicle.setNumofWheels(6)
vehicle.__str__()




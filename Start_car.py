#Car Starter 
  class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    
    def start_car(self):
        self.clutch = True
        self.acc = True
        print("Car Started...")
car1 = Car()
car1.start_car()

class car:
  @staticmethod
  def start():
    print("Car started...")
  @staticmethod
  def stop():
    print("Car stopped...")

class Tata(car):
  def __init__(self, brand):
    self.brand = brand

class Punch(Tata):
  def __init__(self, type):
    self.type = type

car1 = Punch("Electrical")
print(car1.type)
car1.start()
car1.stop()
 

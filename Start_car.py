Car Starting
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
 

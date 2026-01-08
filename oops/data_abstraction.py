from abc import ABC ,abstractmethod
class vehicle(ABC):
  @abstractmethod
  def start(self):
    pass

class car(vehicle):
  def start(self):
    print('car starts with a key') 

class bike(vehicle):
  def start(self):
    print('bike starts with a button')  

car=car()
bike=bike()

car.start()
bike.start()



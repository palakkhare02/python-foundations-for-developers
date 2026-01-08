# constructor is special method when the object created use to setupe the property inside the method in oython.
"""
__init__()
"""

# without constructor
class Car:
  def set_details(self,brand,color):
    self.brand=brand
    self.color=color

car1=Car()
car1.set_details("Tesla","Red")
 
print(car1.brand)
print(car1.color)

# with constructor
class car:
  def __init__(self ,brand ,color):
    self.brand=brand
    self.color=color

car1=car('Tesla','Red')    #values automatically set
print(car1.brand , car1.color) 


"""
constructor syntax:
class ClasssName:
   def __init__(self,parameter1,parameter2):
       self.property1=parameter1
       self.property2=parameter2

___init__() --constructor
self.property : store value inside object
types of constructo :
1.default constructor-no parameter (self)only pass self
2.prameterized constructor (self,age,name)
3. contructor with default values(self ,name="unknown" ,age=0)
"""
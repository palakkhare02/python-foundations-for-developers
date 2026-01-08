# create class
class car():
  # inside class function called Method
  def start(self):
    print("Car is starting....")
  def stop(self):
    print("Car is stopping....")

car1=car()      #object 1
car2=car()      #object 2

car1.start()    #method call
car1.stop()

print("____________________________________")

car2.start()
car2.stop()
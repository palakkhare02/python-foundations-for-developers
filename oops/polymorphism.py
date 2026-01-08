# polymorphism with classes method overriding
class bird:
  def sound(self):
    print("birds make sound")

class crow(bird):
  def sound(self):
    print('crows say "caw-caw"')

class parrot(bird):
  def sound(self):
    print("parrot sounds ,squawk")  

bird1=crow()
bird2=parrot()

bird1.sound()
bird2 .sound()


# polymorphism with operatos -operator overloading
print(10+7)
print('hello'+'world')
print([1,2]+[3,4])

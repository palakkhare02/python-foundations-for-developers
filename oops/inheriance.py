# basic inheritance 
class animal:
  def speak(self):
    print('Animal make sounds')

class Dog(animal):
  def bark(self):
    print('dogs bark')

dog=Dog()
dog.bark()
dog.speak()

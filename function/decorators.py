"""
example
burger-function
extra cheese- extra feature

main function-fuction add
without changing the main function code
"""

def my_decorator(func):
  def wrapper():
    print("something is happening before the function is called")
    func()
    print("something is happening after the functiong is called")
  return wrapper
@my_decorator
def say_hello():
  print("hello")

say_hello()      #eral example of decorator -2 factor authentication
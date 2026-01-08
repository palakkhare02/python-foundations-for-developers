def greet(name): #name parameter
  """
  displaying a hi message to user #docstring 
  """
  print("Hi",name)
greet("palak")  #palak -argument
 
'''
parameter-placeholder for values
arguments- actual values that pass at the time of function calling
3type of argument-positional,keyword ,default argument
''' 

# positional argument

def greet1(name ,city): 
  print(f'welcome {name} to the {city}')
greet1("palak","mumbai")

# keyword argument
greet1(name="palak",city="mumbai")

# default argument
def greet1(name="palak",city="goa"): 
  print(f'welcome {name} to the {city}')
greet1("shyam","delhi")
greet1()

# return statement - use to exit a function and go back the place where return called

def get_full_name(first_name,last_name):
  '''return the full name , in a neated format'''
  full_name=f'{first_name} {last_name}'
  return full_name
name=get_full_name("raju","awasthi")
print(name)


"""
function naming,length of function, avoid global variable
"""

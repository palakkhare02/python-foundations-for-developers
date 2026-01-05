age=int(input('enter your age ='))
if (age>=18 and age<101):
  print('you can vote!')
elif age<=0:
  print("invalid age")
elif age >=101:
    print("greater age")
else:
   print("error occurred!")    
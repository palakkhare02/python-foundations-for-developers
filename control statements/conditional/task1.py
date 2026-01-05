# take input from user and according to input perform the operation

num1=float(input("enter number 1 = "))
num2=float(input("enter number 2 = "))

choice=input("enter your choice + - * / // %  ** :")

if choice == "+":
  print(f' Addition : {num1+num2}')

elif choice == "-":
  print(f' Subtraction : {num1-num2}')
  
elif choice == "*":
  print(f' Multiplication : {num1*num2}')

elif choice == "/":
  print(f' Division : {num1/num2 }')

elif choice == "//":
  print(f' Floor division : {num1//num2}')

elif choice == "%":
  print(f' Modulus : {num1 % num2}')

elif choice == "**":
     print(f'Exponential : {num1 ** num2}')
        







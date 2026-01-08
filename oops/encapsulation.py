class bankAccount:
  def __init__(self,account_number,balance):
    self.account_number=account_number
    self.__balance=balance  #private variable

  def deposite(self,amount):
    self.__balance += amount
    print(f'Deposited {amount}. New balance {self.__balance}')

  def get_balance(self):
    return self.__balance

account = bankAccount('12012014',5000)

account.deposite(500)
print(account.get_balance())

# print(account.__balance)  this line shows attribute error bcoz balance is private variable using getter and setter to control these variable.


    
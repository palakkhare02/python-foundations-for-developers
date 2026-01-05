# ask user to a number then skip that from range 

start=int(input('enter start ='))
stop=int(input('enter stop ='))

if stop<=start:
  print('Invalid input')

skip= int(input ('enter number that you want to skip from range = '))

for i in range(start,stop+1):
  if i==skip:
    continue
  print(i)


"""
generator fi=unctions that behave like iterator
generate on demand value
1time=1value

"""
# yield leyword
def count_down(num):
  while num>0:
    yield num  #yield one value at a time
    num -= 1

# using generator
for number in count_down(5):
  print(number)

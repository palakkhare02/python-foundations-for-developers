# split() : Splits a string into a list based on a delimiter (default is space)

text = "Python is easy to learn"
words = text.split()
print(words)
# Output: ['Python', 'is', 'easy', 'to', 'learn']


# split() with a custom delimiter
text = "apple,banana,mango"
fruits = text.split(",")
print(fruits)
# Output: ['apple', 'banana', 'mango']



# join() : Joins elements of an iterable (like list or tuple) into a single string
#          using the specified string as a separator

words = ['Python', 'is', 'easy']
sentence = " ".join(words)
print(sentence)
# Output: Python is easy


# join() with custom separator
numbers = ['1', '2', '3']
result = "-".join(numbers)
print(result)
# Output: 1-2-3

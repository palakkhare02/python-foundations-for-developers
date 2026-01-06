"""
List Creation Methods and List Methods in Python
Author: Betu
Description: Different ways to create lists and use common list methods
"""

# 1. List using [] brackets


numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]

print("Bracket list:", numbers)
print("Names list:", names)



# 2. List using list() constructor


letters = list("Python")
print("List from string:", letters)



# 3. List using range()


range_list = list(range(1, 6))
print("Range list:", range_list)

even_numbers = list(range(2, 11, 2))
print("Even numbers:", even_numbers)



# 4. List Comprehension


squares = [x * x for x in range(1, 6)]
print("Squares:", squares)

even_list = [x for x in range(1, 11) if x % 2 == 0]
print("Even list:", even_list)


# 5. Nested List


matrix = [[1, 2], [3, 4], [5, 6]]
print("Nested list:", matrix)



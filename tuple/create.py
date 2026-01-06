"""
Tuple Creation and Tuple Methods in Python
Author: Betu
Description: Different ways to create tuples and tuple methods with examples
"""

# 1. Tuple using () brackets

t1 = (10, 20, 30)
print("Tuple using ():", t1)


# 2. Single element tuple

t2 = (5,)     # comma is compulsory
print("Single element tuple:", t2)


# 3. Tuple without parentheses (packing)

t3 = 1, 2, 3
print("Tuple packing:", t3)


# 4. Tuple using tuple() constructor

t4 = tuple([4, 5, 6])
print("Tuple from list:", t4)

t5 = tuple("Python")
print("Tuple from string:", t5)


# 5. Tuple using range()

t6 = tuple(range(1, 6))
print("Tuple using range:", t6)



# 6. Nested Tuple


t7 = ((1, 2), (3, 4))
print("Nested tuple:", t7)


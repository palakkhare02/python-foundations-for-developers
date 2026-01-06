# TUPLE METHODS

nums = (10, 20, 30, 20, 40)

# count() → counts occurrences
print("Count of 20:", nums.count(20))

# index() → returns index of element
print("Index of 30:", nums.index(30))


# TUPLE OPERATIONS

# Concatenation
a = (1, 2)
b = (3, 4)
print("Concatenation:", a + b)

# Repetition
print("Repetition:", a * 3)

# Membership
print(20 in nums)
print(50 not in nums)



# Tuple Unpacking


x, y, z = (100, 200, 300)
print("Unpacked values:", x, y, z)
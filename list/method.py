# LIST METHODS EXAMPLES


nums = [10, 20, 30]

# append() → add element at end
nums.append(40)
print("After append:", nums)

# insert() → add element at specific index
nums.insert(1, 15)
print("After insert:", nums)

# extend() → add multiple elements
nums.extend([50, 60])
print("After extend:", nums)

# remove() → remove specific value
nums.remove(20)
print("After remove:", nums)

# pop() → remove by index
nums.pop(2)
print("After pop:", nums)

# index() → find index of element
print("Index of 30:", nums.index(30))

# count() → count occurrences
nums.append(30)
print("Count of 30:", nums.count(30))

# sort() → sort list
nums.sort()
print("Sorted list:", nums)

# reverse() → reverse list
nums.reverse()
print("Reversed list:", nums)

# copy() → copy list
nums_copy = nums.copy()
print("Copied list:", nums_copy)

# clear() → remove all elements
nums.clear()
print("After clear:", nums)

# min max method
number1 = [10, 5, 20, 3, 15]

print("List:", number1)
print("Minimum value:", min(number1))
print("Maximum value:", max(number1))
"""
Aliasing and Copy in Python
Description: Difference between aliasing, shallow copy, and deep copy
"""

# 1. Aliasing


original_list = [10, 20, 30]

# Both variables point to the SAME object
alias_list = original_list

alias_list.append(40)

print("Original list:", original_list)
print("Alias list:", alias_list)

# Both change because they share the same memory

"""
Shallow Copy in Python
Description: Explanation and examples of shallow copy
"""

# Example 1: Shallow copy with simple list


list1 = [1, 2, 3]
list2 = list1.copy()

list2.append(4)

print("Original list:", list1)
print("Shallow copy list:", list2)

# Only copied list changes (no nested object)



# Example 2: Shallow copy with nested list (IMPORTANT)


nested_list = [[10, 20], [30, 40]]

shallow_copy = nested_list.copy()
shallow_copy[0].append(99)

print("\nOriginal nested list:", nested_list)
print("Shallow copied list:", shallow_copy)

# Both change because inner list is shared


# Example 3: Shallow copy using slicing


data = [[1, 2], [3, 4]]
copy_data = data[:]

copy_data[1].append(100)

print("\nOriginal data:", data)
print("Copied data:", copy_data)



# Example 4: Shallow copy using copy module


import copy

items = [[5, 6], [7, 8]]
items_copy = copy.copy(items)

items_copy[0].append(50)

print("\nOriginal items:", items)
print("Shallow copied items:", items_copy)

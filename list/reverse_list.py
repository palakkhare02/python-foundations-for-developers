"""
This program reverses a list in place without using any built-in reverse functions.

It swaps elements from the beginning and the end of the list moving towards the center.
"""

l = [1, 2, 3, 4, 5]

for i in range(0, len(l) // 2):
    other = len(l) - i - 1
    temp = l[i]
    l[i] = l[other]
    l[other] = temp

print(l)

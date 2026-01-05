"""
Topics Covered:
1. Arithmetic Operators
2. Comparison Operators
3. Logical Operators
4. Assignment Operators
5. Identity Operators:
- is
- is not

6. Membership Operators:
- in
- not in
7. Bitwise Operators

"""
# Arithmetic Operators
a = 10
b = 3

print("Arithmetic Operators")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)  # it remove deciaml points from output
print("Modulus:", a % b)
print("Exponent:", a ** b)  #calculate power

print("\n-----------------------------\n")

# Comparison Operators

print("Comparison Operators")
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater Than:", a > b)
print("Less Than:", a < b)
print("Greater or Equal:", a >= b)
print("Less or Equal:", a <= b)

print("\n-----------------------------\n")


# Logical Operators

x = True
y = False

print("Logical Operators")
print("AND:", x and y)
print("OR:", x or y)
print("NOT x:", not x)

print("\n-----------------------------\n")

# Assignment Operators

c = 5
print("Assignment Operators")

c += 2   # c = c + 2
print("After += :", c)

c -= 1   # c = c - 1
print("After -= :", c)

c *= 3   # c = c * 3
print("After *= :", c)

c //= 2  # c = c // 2
print("After //= :", c)

print("\n-----------------------------\n")

# Identity Operators

print("IDENTITY OPERATORS\n")

a = 10
b = 10
c = a
d = 20

print("a is b:", a is b)
# True → both point to same object (small integers are cached)

print("a is c:", a is c)
# True → c refers to same object as a

print("a is d:", a is d)
# False → different values, different memory location

print("a is not d:", a is not d)
# True → objects are not the same

print("\n-----------------------------\n")

# Example with lists
list1 = [1, 2, 3]
list2 = [1, 2, 3]

print("list1 == list2:", list1 == list2)
# True → values are same

print("list1 is list2:", list1 is list2)
# False → different memory locations

print("\n-----------------------------\n")


# Membership Operators

print("MEMBERSHIP OPERATORS\n")

numbers = [10, 20, 30, 40]
name = "python"

print("20 in numbers:", 20 in numbers)
# True → 20 exists in list

print("50 not in numbers:", 50 not in numbers)
# True → 50 does not exist in list

print("'p' in name:", 'p' in name)
# True → character exists in string

print("'z' not in name:", 'z' not in name)
# True → character does not exist

"""
Quick Difference:
- 'is' checks memory location (identity)
- '==' checks value
- 'in' checks presence of value in sequence
"""
"""
Bitwise Operators in Python
===========================

Bitwise operators work on the binary (0s and 1s) representation of numbers.

Operators:
&   Bitwise AND
|   Bitwise OR
^   Bitwise XOR
~   Bitwise NOT
<<  Left Shift
>>  Right Shift
"""

# Bitwise AND (&)

a = 5    # Binary: 0101
b = 3    # Binary: 0011

print("Bitwise AND (&)")
print("5 & 3 =", a & b)
# 0101
# 0011
# ----
# 0001  → 1

print("\n-----------------------------\n")

# ---------------------------------
# Bitwise OR (|)
# ---------------------------------
print("Bitwise OR (|)")
print("5 | 3 =", a | b)
# 0101
# 0011
# ----
# 0111  → 7

print("\n-----------------------------\n")

# ---------------------------------
# Bitwise XOR (^)
# ---------------------------------
print("Bitwise XOR (^)")
print("5 ^ 3 =", a ^ b)
# 0101
# 0011
# ----
# 0110  → 6

print("\n-----------------------------\n")

# ---------------------------------
# Bitwise NOT (~)
# ---------------------------------
print("Bitwise NOT (~)")
print("~5 =", ~a)
# Formula: ~(n) = -(n + 1)
# ~5 = -(5 + 1) = -6

print("\n-----------------------------\n")

# ---------------------------------
# Left Shift (<<)
# ---------------------------------
print("Left Shift (<<)")
print("5 << 1 =", a << 1)
# 0101 << 1 → 1010 → 10
# Left shift = multiply by 2

print("\n-----------------------------\n")

# ---------------------------------
# Right Shift (>>)
# ---------------------------------
print("Right Shift (>>)")
print("5 >> 1 =", a >> 1)
# 0101 >> 1 → 0010 → 2
# Right shift = divide by 2

"""
Quick Summary:
- &  → both bits must be 1
- |  → any one bit is 1
- ^  → bits must be different
- ~  → bit inversion
- << → multiply by 2
- >> → divide by 2
"""

"""
BODMAS Rule (Operator Precedence in Python)
==========================================

BODMAS tells us the order in which operations are performed in an expression.

B – Brackets ()
O – Orders (powers, exponents) **
D – Division /
M – Multiplication *
A – Addition +
S – Subtraction -

Python follows the same rule to evaluate expressions.
"""



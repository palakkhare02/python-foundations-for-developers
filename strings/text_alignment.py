# -------- Methods for text alignment --------
# rjust() → Right justify
# Aligns the string to the right by adding spaces on the left
text = "Python"
print(text.rjust(10))   # Output: '    Python'


# ljust() → Left justify
# Aligns the string to the left by adding spaces on the right
text = "Python"
print(text.ljust(10))   # Output: 'Python    '


# center() → Center alignment
# Aligns the string to the center by adding spaces on both sides
text = "Python"
print(text.center(10))  # Output: '  Python  '


# -------- Methods to remove whitespace --------

# strip() → Removes whitespace from both left and right sides
text = "  Hello World  "
print(text.strip())    # Output: 'Hello World'


# lstrip() → Removes whitespace from the left side only
text = "  Hello World  "
print(text.lstrip())   # Output: 'Hello World  '


# rstrip() → Removes whitespace from the right side only
text = "  Hello World  "
print(text.rstrip())   # Output: '  Hello World'
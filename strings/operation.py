# len() -return integer
str="python"
print(len(str))

# concatenation done only strings
name="palak"
sur_name="khare"
print("hyy" ,name + sur_name)

# Python String Inbuilt Methods with Definitions (Using Comments)

# --------------------------------------------------
# lower() : Converts all characters of a string to lowercase
text = "HELLO World"
print(text.lower())        # Output: hello world


# --------------------------------------------------
# upper() : Converts all characters of a string to uppercase
text = "hello World"
print(text.upper())        # Output: HELLO WORLD


# --------------------------------------------------
# title() : Capitalizes the first letter of each word in the string
text = "python programming language"
print(text.title())        # Output: Python Programming Language


# --------------------------------------------------
# capitalize() : Capitalizes only the first character of the string
text = "python is easy"
print(text.capitalize())  # Output: Python is easy


# --------------------------------------------------
# strip() : Removes leading and trailing spaces from the string
text = "   hello   "
print(text.strip())       # Output: hello


# --------------------------------------------------
# lstrip() : Removes leading (left side) spaces from the string
text = "   hello"
print(text.lstrip())      # Output: hello


# --------------------------------------------------
# rstrip() : Removes trailing (right side) spaces from the string
text = "hello   "
print(text.rstrip())      # Output: hello


# --------------------------------------------------
# replace() : Replaces old substring with new substring
text = "I like Java"
print(text.replace("Java", "Python"))  # Output: I like Python


# --------------------------------------------------
# find() : Returns index of first occurrence of substring, -1 if not found
text = "python programming"
print(text.find("program"))            # Output: 7


# --------------------------------------------------
# index() : Returns index of substring, gives error if not found
text = "python programming"
print(text.index("python"))             # Output: 0


# --------------------------------------------------
# split() : Splits string into a list based on spaces or delimiter
text = "Python is powerful"
print(text.split())                     # Output: ['Python', 'is', 'powerful']


# --------------------------------------------------
# join() : Joins elements of a list into a single string
words = ["Python", "is", "easy"]
print(" ".join(words))                  # Output: Python is easy


# --------------------------------------------------
# startswith() : Checks if string starts with given value
text = "python.py"
print(text.startswith("python"))        # Output: True


# --------------------------------------------------
# endswith() : Checks if string ends with given value
text = "python.py"
print(text.endswith(".py"))             # Output: True


# --------------------------------------------------
# count() : Counts number of occurrences of a substring
text = "banana"
print(text.count("a"))                  # Output: 3


# --------------------------------------------------
# isalpha() : Returns True if string contains only alphabets
text = "Python"
print(text.isalpha())                   # Output: True


# --------------------------------------------------
# isdigit() : Returns True if string contains only digits
text = "12345"
print(text.isdigit())                   # Output: True


# --------------------------------------------------
# isalnum() : Returns True if string contains alphabets and digits
text = "Python123"
print(text.isalnum())                   # Output: True


# --------------------------------------------------
# isspace() : Returns True if string contains only whitespace
text = "   "
print(text.isspace())                   # Output: True


# --------------------------------------------------
# swapcase() : Converts uppercase letters to lowercase and vice versa
text = "PyThOn"
print(text.swapcase())                  # Output: pYtHoN


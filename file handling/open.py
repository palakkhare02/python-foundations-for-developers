"""
open("file_name.txt","mode")
"""

file=open(r"C:\Users\apk14\OneDrive\Desktop\python\python-foundations-for-developers\file handling\file.txt","r")
content=file.read()
print(content)
file.close()
try:
  file=open(r"C:\Users\apk14\OneDrive\Desktop\python\python-foundations-for-developers\exception handling\errors.txt","r")
  content=file.read()
  print(content)

except FileNotFoundError:
  print("file not found")

finally:
  file.close()  
  print("file operation completed")  
with open(r"C:\Users\apk14\OneDrive\Desktop\python\python-foundations-for-developers\file handling\data.txt","a") as file:
  content=input("enter data to append: ")
  file.write(content)
  print("append successfully")
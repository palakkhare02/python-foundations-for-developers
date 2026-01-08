class Student:
  def __init__(self,name,age,grade):
    self.name=name
    self.age=age
    self.grade=grade

# creating object
student1=Student("palak",20,"A+")    
student2=Student("pari",22,"A")  

print(student1.name,student1.age,student1.grade)
print(student2.name,student2.age,student2.grade)
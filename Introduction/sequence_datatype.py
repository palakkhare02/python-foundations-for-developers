"""
ordered collection of data type 
string -'abc',"bc".strings immutable.
list- group of variable store in single variable using [] ,tuple
"""

text="this is a string"
print(text)

my_list=['data1','data2','data3']
print(my_list)

my_tuple=('data1','data2','data3')
print(my_tuple)


"""
Set data type -set(mutable) and frozen set(immutable)
"""

unique_number={1,25,2,2,4,4,1,3,8}  #set
print(unique_number)


immutable_number=frozenset([1,25,2,2,4,4,1,3,8]) #frozen set
print(immutable_number)


"""
Mapping data types -dictionary(key value pairs),
"""
person={
  'name':'gopal',
  'age':100,
  'number':213466
}
print(person)

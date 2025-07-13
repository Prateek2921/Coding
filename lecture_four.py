#dictionary in pythons
"""
info = {
    "Name":"Prateek",
    "key":"Value",
    "learning":"coding"
}

print(type(info))
# Accessing values in a dictionary

print(info["Name"]) 
        #or
print(info.get("Name"))
  
  # Adding a new value to the key 
info["Name"] = "aman mishra"
print(info["Name"])
"""
#null_dict = {}
#null_dict["key"] = "Apnacollege"
#print(null_dict)

# Nested dictionary 
"""
student = {
    "name": "Prateek",
    "subjects":{
        "subject1": "Python",
        "subject2": "Java",
        "subject3": "c++"
    }
}"""

#print(student["subjects"]["subject1"])
#print(student.keys())    # return all keys 

#print (student.values())   # returns all values

#print(student.items())   #returns all (key, value) pair as a tuples

#print(student.get("name"))  # returns the value of the key if it is in the dictionary
#student.update({
 #   "city" : "Greater Noida"        #update the dictionary with new key and value 
#})
#print(student)
"""
print(list(student.keys()))

mol1 = (list(student.keys()))  #changing its type into a list

print (type(mol1))"""

 # Sets in python ( set ignore duplicate values and is unordered)
"""
collection = {1 ,2 ,3 , 4}

print (collection)
print(type(collection)) 

collection1 = set() # empty set 

print (type(collection1)) """

#set.add(value) ->adds an element
#set.remove(value)->remove an element
#set.clear()->empties the set
#set.pop()-> removes a random value 
#set.union(set2)-> combines both set values and return new values
#set.intersection(set2)-> combines common values and return new values
"""
set1 = {1,2,3}
set2 = {2,3,4}

print(set1.union(set2))  # {1,2,3,4}

print(set1.intersection(set2))  #{2,3}"""

#dictionary = {
 #   "cat"   : "a small animal",
 #   "table" : ["a piece of furniture" , "list of facts and figures"]
#}

#print(dictionary)

#classrooms = {"python","java","python","c++","javascript","java","python", "c++","c"}

#print(len(classrooms))

marks = {}

x = int(input ("enter physics :"))

marks.update({
    "physics" : x
})
y = int(input ("enter chemistry :"))

marks.update({
    "chemistry" : y
})
z = int(input ("enter Maths :"))

marks.update({
    "Maths" : z
})

print(marks)
#strings are immutable in python but list are mutable
""""
str = "hello"
print(str[0])
str[0]= "y" 
"""
#student = ["karan", 95.4, 17, "delhi"]

#print(student[0])

#student[0] = "Prateek"
#print(student) 

#list Methods 
#list.append(value) - adds one element at the end
#list.sort() - sorts the list in ascending order
#list.sort(reverse=True) - sort list in descending order
#list.reverse() - reverse the list
#list.insert(index, value) - inserts value at index
"""
list = [2 , 1 , 3]
list.insert(1 , 5)
print (list)
"""

#list.pop(index) - removes element at index
#list.remove(value) - remove first occurance of value
 
 #tuples in python 
"""
tup = (87 ,64 ,33 ,76,33, 64)
print(type(tup))
 
print(tup[1:3]) # slicing works in tuples like this

# return index of first occurrences 
print(tup.index(64)) #return index of occurance of 64

print(tup.count(33))"""
""""
movies =[]

mov1 = input("Enter first movie name : ")
mov2 = input("Enter second movie name : ")
mov3 = input("Enter third movie name : ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)"""

list1 = [1, 2, 3, 2, 1]
list2 = [1, 2, 3, 4, 5]

copy_list1 = list1.copy()
copy_list1.reverse()

if(list1 ==copy_list1):
    print("List1 is a palindrome")
else:
    print("List1 is not a palindrome")

copy_list2 = list2.copy()
copy_list2.reverse()

if(list2 == copy_list2):
    print("List2 is a palindrome")
else:
    print("List2 is not a palindrome")

    
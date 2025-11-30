marks1 = 56.6
marks2 =45.3
marks3 = 56.3
marks4 = 67.7
marks = [marks1 , marks2 , marks3 ,marks4]
print(marks)
print(type(marks))
print(marks[0])# It givves the value of index from the list
print(len(marks)) # It gives the length of the list(marks)


student = ["arjun",67,65.6,"Aayush"]
student[0]=90
student[0]= 10*80/100
print(student)

# List Slicing 
# Similar to String Slicing 
teacher = ["disha","pinki","riya","Rani"]
print(teacher)
print(teacher[1:3]) # Ending index is not included
print(teacher[-2:-1 ])

number = [1,3,2,6,4,7,8,3,0,3]
print(number.sort())
print(number)

# If we want to sort the list in descending order 
print(number.sort(reverse=True))
print(number)

fruits = ["apple","banana"]
print(fruits.append("kela"))
print(fruits)

fruits.insert(1,"Papita")
print(fruits)

fruits.remove("kela")
print(fruits)

fruits.pop(2)
print(fruits)
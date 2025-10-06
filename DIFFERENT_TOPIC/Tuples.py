# Creating Empty Tuples :
tup = (1,4,5,5.6,6.5,45.4,6.5)
print(tup)
print(type(tup))
print(tup.index(4))
print(tup)

print(tup.index(6.5))
print(tup.count(6.5))

# Write a program to enter the name of their 3 favourite movies and store them in the list 
movie1 = input("Enter first movie")
list = []
print(list)
print(list.append(movie1))
print(list)

movie2 = input("Enter second movie")
list.append(movie2)
print(list)



#Write a program to check if a list contains a palindrome of Elements (use copy() methods)
list1 = ["m","a","a","m"]
list2 = list1.copy()
list1.reverse()
print(list1 ,"",list2)
if(list2 == list1):  
    print("Palindrome")
else:
    print("Not a palindrome")


# Write a program to count the numbers of students with the "A" grade in the 
# following tuple 
grade = ("C","D","A","A","B","B","A")
grade.count("A")
print(grade.count("A"))

#Write a program to store the abovve values  in a list  & sort them from
# "A" to "D"....




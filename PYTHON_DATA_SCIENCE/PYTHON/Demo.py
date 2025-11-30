name = "aayush pateriya"
print(name)
number = 56
print(number)


# The input will change recognize 56
# the user value as String whether it is number 

age = input("Enter your age")
print(type(age))

marks = int(input("enter your age"))
print("The age of the student is :",age)
# Type casting happened below 
print("the data type of marks is : ",type(marks))


# Sum of two numbers 
num1 = input("Enter the number")
num2= input("Enter another number")
result = int(num1)+int(num2)
print("The result of the number is : ",result)
print("The type of the  abovve result is :",type(result))

# Program to print the side of the square and print it area too 
side = input("Enter the side of the square")
side=int(side)
print("The side of the area is : ",side ,"and the data type of the side is :",type(side))
area = pow(side,2)
print("The area of the square obtained is :",area )

# Write a program to print the two pointing numbers and print the averge orf these number 
n1 = input("Enter first number")
n2 = input("Enter second number")
n1 = float(n1)
n2= float(n2)
totalvalue=2
ag = (n1+n2)/totalvalue
print("the average obtained is : ",ag)

# To find the square of the number (**)
s = input("Enter the number")
s = float(s)
square = print("the area of the  square  in float is : ",s**2)

# Write a program to input the two floating point number and finding their average 
n1 = float(input("Enter the number 1"))
n2 = float(input("Enter the number 2"))
average = n1+n2
result = average/2
print("The average of the number obtained is : ",result)

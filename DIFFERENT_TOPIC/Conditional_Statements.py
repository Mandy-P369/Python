# For the program to check the light at the traffic signal 
light = input("Enter the light")
if(light=="red"):
    print("Red light shown , You need to stop")
elif(light=="yellow"):
    print("Yellow light shown , You need to be ready to go ")
elif(light=="green"):
    print("You need to go ")
else:
    print("No command follow ")


    
# The program to check the student grage according to their marks 
marks = int(input("Enter the marks"))
if(marks==0 and marks>=0 and marks<=28):
    print("Grade E")
elif(marks>=24 and marks<=50 ):
    print("Grade D")
elif(marks>50 and marks<=69):
    print("Grade C")
elif(marks>69 and marks<=89):
    print("Grade B")
elif(marks>89 and marks>100):
    print("Grade A")


    # Practise Question : 
# 1. Write a program to check  if a number entered by the user is odd or even ..
# 2. Write a program to find the greatest of 3 numbers entered by the user..
# 3. Write a program to chekc if the number is multiple of 7 or not..


# You're working on a program to manage a student database. Students have a name, ID, and 
# major. You want to create a text file (students.txt) to store this information. 
# Task: 
# Write a Python program that: 
# 1. Declares variables: 
# 2. Opens the file: 
# 3. Prompts the user: 
# 4. Writes to the file: 
# Make another program to display data.
class StudentDetails:
    def __init__(self, name, id, major):
        self.name = name
        self.id = id
        self.major = major

    def display_Dictionary(self):
        return {
            "name": self.name,
            "id": self.id,
            "major": self.major
        }

fname = input("Enter the file name: ")
r = int(input("how much records you want to insert inside the dictionary "))
with open(fname, 'a') as f:
    for i in range(r):
        name = input("Enter your name: ")
        try:
            id = int(input("Enter your valid id:"))
        except ValueError:
            print("Invalid Id! Using id=0")
            id = 0
        major = input("Enter your major subjects: ")
        
        student = StudentDetails(name, id, major)  
        f.write(str(student.display_Dictionary()) + "\n")

print("Data saved successfully!")
print("\n--- Student Data ---")
with open(fname, 'r') as file:  
    for line in file:
        print(line.strip())

    
     



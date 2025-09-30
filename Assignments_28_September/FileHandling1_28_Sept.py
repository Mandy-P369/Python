# Write a program to get rollno and marks of 5 students. 
# Store the details of the passed students in a file named ‘passed.txt’ and store the 
# others in a separate file named ‘failed.txt’
try:
    for i in range(3):     
        name = input("Enter the name")
        rollno= int(input("Enter the rollno :"))
        marks1= int(input("Enter English subjects marks"))
        marks2= int(input("Enter mathematics Subject marks"))
        marks3= int(input("Enter Science subjects marks "))
        marks4= int(input("Enter SST subjects marks"))
        marks5= int(input("Enter Hindi subjects marks "))
        Totalmarks = marks1+marks2+marks3+marks4+marks5
        print("The totalmarks of the students are : ",Totalmarks)
        avg=(marks1+marks2+marks3+marks4+marks5)/5
        print("The average of the Students are :",avg)

        # if(marks1<=0 and marks1>=100 and marks2<=0 and marks2>=100 and marks3<=0 and marks3>=100
        #    and marks4<=0 and marks4<=100 and marks5<=0 and marks5<=100):
        #     print("Marks cannot be acceptable")
        #     break 

        if(avg>0 and avg<=40):
                    print("These are the records of Failed Students inside the class")
                    fname = input("Enter the file name")
                    f = open(fname,'a')
                    result = print("The Student get failed")
                    f.write(name)
                    f.write('\n')
                    f.write(str(rollno))
                    f.write('\n')
                    f.write(str(marks1))
                    f.write('\n')
                    f.write(str(marks2))
                    f.write('\n')
                    f.write(str(marks3))
                    f.write('\n')
                    f.write(str(marks4))
                    f.write('\n')
                    f.write(str(marks5))
                    f.write('\n')
                    f.write(str(Totalmarks))
                    f.write('\n')
                    f.write(str(avg))
                    f.write('\n')
                    print("Data Saved")
                    f.close()
           
        elif(avg>=40 and avg<=100):
                    print("These are the records of passed Students")
                    mname  = input("Enter the file name")
                    m = open(mname,'a')
                    result = print("Student get passed")
                    m.write('\n')
                    m.write(name)
                    m.write('\n')
                    m.write(str(rollno))
                    m.write('\n')
                    m.write(str(marks1))
                    m.write('\n')
                    m.write(str(marks2))
                    m.write('\n')
                    m.write(str(marks3))
                    m.write('\n')
                    m.write(str(marks4))
                    m.write('\n')
                    m.write(str(marks5))
                    m.write('\n')
                    m.write(str(Totalmarks))
                    m.write('\n')
                    m.write(str(avg))
                    m.write('\n')
                    print("Data Saved")
                    m.close()

except FileNotFoundError : 
        print("\n No file exist")







    
        
# Write a program to copy the contents of a file in another. While copying replace 
# all the spaces with a comma. 
# For example : if the source file has the data 
# ‘India USA Germany Spain’ 
# the target file should contain 
# ‘India,USA,Germany,Spain’
fname = input("Enter the file name")
f = (fname,'w')
file = input("Brazil Russia India China South-Africa")
pos = file.find(' ')
length = len(file)
print("The length of the file is  : ",length)
result = " "
for i in range(length):
        if(i>=pos):
            result+=fname[i]
        print("The result obtained is : ",result)
        




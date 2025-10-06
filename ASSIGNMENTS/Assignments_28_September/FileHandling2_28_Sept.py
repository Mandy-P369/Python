# Write a program to copy the contents of a file in another. While copying replace 
# all the spaces with a comma. 
# For example : if the source file has the data 
# ‘India USA Germany Spain’ 
# the target file should contain 
# ‘India,USA,Germany,Spain’
file = "Brazil Russia India China South-Africa"
mname = input("Enter the existig file ")
m= open(mname,'w')
m.write(file)
m.close()
length = len(file)
sp = file.find(' ')
print("The length of the file is  : ",length)
for i in range(length):
       result = file.replace(' ',',')
print(result)
fname = input("Enter the file name")
f = open(fname,'w')
f.write(result)
print("\nData Saved Successfully")
f.close()



            



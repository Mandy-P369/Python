a = "aayush"
b = "pateriya"
name = a+b
print(name)

str1 = input("Enter your name")
str = len(str1)
print(str)

str2 = input("Enter another name")
st = len(str2)
print(st)

finalstring = str+st
print(finalstring)


name = input("Enter the name of the Student")
str1 = name[1:5]
print(str1) #input : aayushpateriya , Output:ayus


str2 = name[-3:-1] # input:aayushpateriya, output:iy
print(str2)



# String Functions 
str = "i" \
" am a coder "
print(str.endswith("er."))# return  true if the String ends with subString 

str2 = print(str.capitalize()) # it capitalizes the first character of the String

print(str.replace("o","a"))

print(str.find("o")) #8
print(str.count("a"))# Count the occurrence of the String , output:2


# The program to find the length of the given String by the user 
name = input("Enter the String ")
str = print(len(name))












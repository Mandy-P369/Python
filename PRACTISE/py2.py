name = "Sachin Tendulkar"
#Input : Sachin Tendulkar
#Output : S.T.
name = name.split(' ')
length = len(name)
for i in name:
    print(i[0],end='.')
print("\n")
print("______________")


# Input : Aayush Pateriya 
# Output :A.P
name = "Aayush Pateriya"
length = len(name)
print(length)
sp = name.find(' ')
lastname = "."
for i in range(length):
    if i>=sp:
        lastname+=name[i]
        print(lastname)
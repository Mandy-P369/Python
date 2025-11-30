collection = set()
collection.add(1)
print(collection)
collection.add("aayush")
print(collection)
collection.add(("aayush",20)) # We can store the tuple inside the set but we cannot 
                              # store the dictionaries and list inside the set .
print(collection)

#If the element does not exist inside the set , then it is showing the 
# key Error ...
details = {45,54,56,65}
details.add("aayush")
print(details)



details = set()
details.add("Rambharose")
print(details)
details.add("Aayush")
print(details)


# What do we mean by unshapable type 
#  Values which are immutable should be stored inside the Set .

# Union methods in Set 
set1  =set()
set1.add(1)
set1.add(2)
set1.add(3)
print("The Set 1 is :  ",set1)
set2 =set()
set2.add(4)
set2.add(5)
set2.add(6)
set2.add(3)
set2.add(2)
print("The set2 is :",set2)
print(set1.union(set2))

#Intersection methods in Set 
print(set1.intersection(set2))




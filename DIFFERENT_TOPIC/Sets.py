# Set in Python
# Set is a collection of the unordered items  .
# Each Element in the set must be the unique and immutable .
# The Set is mutable , but the element of the set is immutable .
# The numbers , String and tuples should be stored in the Sets.
details = set()
details.add(1)
print(details)
details.add("aayush")
print("The details is : ",details)


collection = {1,2,3,4,5,6,7}
print(type(collection))
print(collection)


# We can also store the String values with the numbers inside the Sets 
collection1 ={12,21,32,23,34,34,65,45,"aayush","disha"}
print(type(collection1))
print(collection1)
print(type(collection1))
print(collection1)


# Duplicate values are removed automatically from the Set 

#Set is unorrdered too .The output print is different...
collection3 = {23,54,23,23,23,65,56,56,65,76,86,45,"aayush","aayush","disha","Disha",56,78}
print(type(collection3))
print(collection3)
print(len(collection3))     


#Methods of Set 
# Addition of the element from the Set 
set = {"aayush","Disha",56,56,67,65,54,43,32,56,"Radha","Rohit"}
print(type(set))
print(set)
print(len(set))
set.add("Rambharose")
print(set)

# Removing the element from the set 
set.remove("aayush")
print(set)
set.remove(67)
print("After removing element :",set)

# Popping Element from the Set 
set.pop() # removing first element directly from the Set .
print("After popping Element :",set)

set.pop() # removing first element directly from the Set .
print("After popping Element :",set)


# Clearing full Set 
print("The set obtained is : " ,set)
set.clear()
print("After clearing full set : ",set)









# Set is a collection of unordered items .
# Each Element in the set  must be unique and immutable .

# How to create the empty Set 
collection = set()
print(type(collection))
# Set mutable hota h tabhi to hum Elements ko add or remove kar pa rahe h
# ,but Set ke elements immutable h tabhi to hum set ke andar tuple ko pass kar skte h
# lekin list ya dictionary ko pass nahi karte .

dict = ("aayush","Disha",56,65,76)
collection = set()
collection.add(dict)
print(collection)

# Agar set ke andar bo value nahi h jo hum remove kar rahe h ,
# to waha par "key Error show hoga".

collection.add("Ramlal")
print(collection)

# collection.remove("Pandit") key Error show hoga yaha ....
print(collection)

print(len(collection))
print(len(dict))

# We are storing some information  in the dictionary .
info = {
"key" : "value",
"name" : "aayush",
"learning" : "python",
"age" : 20,
"is_adult" : True,
"marks": 98.8
}
print(info)
# We can also store the list and tuples inside the dictionary .
info2 = {
    "name" : "aayush pateriya",
    "age" : 20,
    "subjects" : ["python","java","C++","C","Rust","Kotlin"] ,
    "topics" : ("OOP's","Sets")
}
print(info2)
print(type(info2))

info2["name"]="Disha Pateriya"
print(info2)



# Nested Dictionaries 
# We can also create the dictionary inside the dictionary 
details = {
    "name" : "aayush pateriya",
    "age" :20,
    "score" : {
        "chem":45,
        "physics" : 56,
        "biology":87
    }
}
print(details)
print(details.keys())
 
#  If we want to type cast in the list format .
print(list(details.keys()))
# If we want to type cast in the Tuple format .
print(tuple(details.keys()))
# To find the length of the keys of  dictionary 
print("the length of the dictionary is : ",len(details.keys()))



# Value methods in the dictionary 
print(details.values())
 
print("The items inside the dictionary is : ",details.items())


details.update({"City" : "Sagar"})
details.update({"State" : "Madhya pradesh"})
print(details)
new_dict = {"Country" : "India","Gender" :"Male"}
details.update(new_dict)
print(details)


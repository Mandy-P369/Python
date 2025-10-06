# To change the String from camel case  to snake case :
def camel_to_Snake(name):
    res = ""
    for x in name:
        if x.isupper():
            res+="_"+x.lower()
        else:
            res+=x
    return res.lstrip("_")
name = "myVariableName"
print(camel_to_Snake(name))


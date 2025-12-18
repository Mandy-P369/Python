data =  1,2,76,23,65,34,56
with open(r"C:\DEMO\SampleText.txt", "r") as f:
    data = f.read()
    print(data)
    num="" 
    for i in range(len(data)):
        if data[i]==",":
            print(int(num))
            num=""
        else :
            num+=data[i] 

# with open(r"C:\DEMO\DemoText","r") as f:
#     data = f.read()
#     print(data)


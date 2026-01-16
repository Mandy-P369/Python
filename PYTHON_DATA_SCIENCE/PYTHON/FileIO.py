# File Output/Input :
# f = open("C:\DEMO\DemoText","r")
# data = f.read()
# print(data)
# f.close()

f = open("C:\DEMO\DemoText","r+")
data = f.write("I belong to India")
print(f.read())
f.close()
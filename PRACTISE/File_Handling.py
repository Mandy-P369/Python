try:    
    fname =input("Enter the file you want to create :  \t")
    data = input("Enter the data ")
    f = open(fname,'w')
    f.write(data)
    f.close()

    mname = input("Enter the file you want to read")
    mname+='.txt'
    f = open(fname,'r')
    str = f.read()
    print(str)
    f.close()
except FileNotFoundError: 
    print("No file exist inside the PC")
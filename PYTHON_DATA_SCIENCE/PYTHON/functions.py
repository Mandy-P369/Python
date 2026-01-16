# To make code more readable, efficient,maintainable,reusable,extensible 
def greet():
    """
    Description : This function will print the welcome message 
    return   : This function will return the welcome message
    """
    description = "Radhey Radhey"
    return description 

# greet()
name= greet()
print(name+",stay connect")

def intr()->str:
    desc = 'My name is ayush pateriya'
    return desc

greet = intr()
print(greet)

# Function to add the even and odd sum from the list ..
def even_odd_sum(lst):
    even_sum = 0
    odd_sum = 0
    for i in lst : 
        if i%2==0:
            even_sum+=i
        elif i%2==1:
            odd_sum+=i
    return even_sum,odd_sum


sum_even,sum_odd  = even_odd_sum([11,12,13,14,15,16,17,18,19,21,32,43,54,65,76,87,98,90,45,56,55,32,56])
print(sum_even,sum_odd)

# Functions : Positional keywords 
def details(name,age):
    print('My name is ' + name + 'and I am '+str(age))
details('aayush',21)


# Functions : Keywords Arguements 
def details(name='aayush',age=21):
    print('My name is '+ name +'I am'+str(age))
details()

def hello(*args,**kwargs):
    # print("My name is "+ args + "I am "+kwargs)
    print(args)
    print(kwargs)

    # Description : The keywords arguement will be shown inside
    # dictionary and positional arguements in list format
hello('aayush','pateriya',age=21,dob=2005,day=5,month='january')


def details(*args,**kwargs):
    print(args)
    print(kwargs)

lst = (('aayush','pateriya'))
dict = {'name' : 'aayush','surname' : 'pateriya' }
details(*lst,**dict)
print(details()) # None

def details(*args ,**kwargs) : 
    print(args)
    print(kwargs)
    
details(45,45,name='aayush')
    





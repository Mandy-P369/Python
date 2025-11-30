import math 
# Input end value
end = int(input("Enter the end number: "))
start = 1   # starting number
i = 2       # power (square)
store = []  # list for storing results
while start <= end:
    res = math.pow(start, i)   # start^2
    print("{start}^{i} = {res}")
    store.append(res)          # append result to list
    start += 1   # increment
print("Stored results:", store)

data = {"aayush",20,"btirt"}
print(data )
print(type(data))


ch = 'a'
print(ch)
val = ord(ch)
print(val)



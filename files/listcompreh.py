mystring = 'hello'

mylist = []
for letter in mystring: 
    mylist.append(letter)
print(mylist)




mystring = 'hello'
mylist = [letter for letter in mystring]
print(mylist)


mylist = [num for num in range(0,11)]
print(mylist)

mylist = [num**2 for num in range(0,11)]
print(mylist)

mylist = [x**2 for x in range(0,11) if x%2==0]
print(mylist)

mylist = [x**3 for x in range(0,11) if x%1==0]
print(mylist)

celsius = [0,10,20,34.5]
fahrenheit = [( (9/5)*temp + 32) for temp in celsius]
print(fahrenheit)

fahrenheit = []
for temp in celsius:
    fahrenheit.append(( (9/5)*temp + 32))
print(fahrenheit)

mylist = []

for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)
print(mylist)






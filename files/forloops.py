mylist = [1,2,3,4,5,6,7,8]

for num in mylist:
    print(num)



mylist = [1,2,3,4,5,6,7,8]

for num in mylist:
    print('hello')



mylist = [1,2,3,4,5,6,7,8]
for num in mylist:
    if num % 2 == 0: 
        print(num)
    else: 
        print(f'Odd Number: {num}')




mylist = [1,2,3,4,5,6,7,8]

list_sum = 0

for num in mylist:
    list_sum = list_sum + num
print(list_sum)



mystring = 'hello world'

for letter in mystring:
    print(letter)


for letter in 'hello world':
    print(letter)



tup = (1,2,3)
for item in tup:
    print(item)



mylist= [(1,2), (3,4),(5,6),(7,8)]
len(mylist)
for item in mylist:
    print(item)


mylist= [(1,2), (3,4),(5,6),(7,8)]

for (a,b) in mylist:
    print(a)
    print(b)


mylist= [(1,2), (3,4),(5,6),(7,8)]
for a,b in mylist:
    print(a)
    print(b)

mylist= [(1,2), (3,4),(5,6),(7,8)]

for a,b in mylist:
    print(b)


mylist= [(1,2), (3,4,5,6),(7,8)]

for item in mylist:
    print(item)


d = {'k1' : 1, 'k2': 2, 'k3': 3}

for item in d: 
    print(item)


d = {'k1' : 1, 'k2': 2, 'k3': 3}

for item in d.items(): 
    print(item)



d = {'k1' : 1, 'k2': 2, 'k3': 3}

for key,value in d.items(): 
    print(value)

d = {'k1' : 1, 'k2': 2, 'k3': 3}

for values in d.values(): 
    print(value)


print(set([1,1,2,3]))






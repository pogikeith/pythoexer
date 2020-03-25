def square(num):
    return num**2
my_nums = [1,2,3,4]
for item in map(square, my_nums): 
    print(item)

print(list(map(square, my_nums)))


def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'Even'
    else:
        return mystring[0]


names = ['andy', 'bob', 'cat']
print(map(splicer, names))


def check_even(num):
    return num%2 == 0
mynums = [1,2,3,4,6]
print(list(filter(check_even, mynums)))


def check_even(num):
    return num%2 == 0
mynums = [1,2,3,4,6]
for n in filter(check_even, mynums): 
    print(n)


def square(num):
    result = num **2 
    return result
print(square(3))


def square(num):
     
    return num **2
print(square(3))



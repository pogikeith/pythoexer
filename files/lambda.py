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

print(list(map(splicer, names)))



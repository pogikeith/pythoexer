st = 'Sam print only the words that start with s in this sentence'
print(st.split())

for word in st.split():
    if word[0] == 's' or word[0] == 'S': 
        print(word)


st = 'Sam print only the words that start with s in this sentence'
print(st.split())

for word in st.split():
    if word[0].lower()== 's': 
        print(word)


mylist = []
for num in range(0,11,2):
    print(num)



st = 'print every word in this sentence if it has even number of letters'
for word in st.split():
    if len(word) %2 == 0:
        print(word)

st = 'print every word in this sentence if it has even number of letters'
for word in st.split():
    if len(word) %2 == 0:
        print(word + '  is even')



for num in range(1,101):
    if num%3 == 0 and num%5 == 0:
        print('FizzBuzz')
    elif num%3 == 0: 
        print('fizz')
    elif num%5 == 0:
        print('buzz')
    else:
        print(num)


for num in range(1,81):
    if num%3 == 0 and num%5 == 0:
        print('FizzBuzz')
    elif num%3 == 0: 
        print('fizz')
    elif num%5 == 0:
        print('buzz')
    else:
        print(num)


def myfunc(a):
    if a == True: 
        return 'Inside'
    elif a == False: 
        return 'Outside'


def myfunc(x,y,z):
    if z == True:
        return x
    else:
        return y






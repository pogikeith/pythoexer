mylist = [1,2,3]

for num in range(10):
    print(num)


for num in range(3,10):
    print(num)


mylist = [1,2,3,4,5,6,7]

for num in range(0,11,10):
    print(num)


list(range(0,11,2)) 




index_count = 0

for letter in 'abcde':
    print('at index {} the letter is {}'.format(index_count, letter))
    index_count += 1 



index_count = 0
word = 'abcde'
for letter in word:
    print(word[index_count])
    index_count += 1 




word = 'abcde'
for _ in enumerate (word):
    print(_) 



word = 'abcde'
for index,letter in enumerate (word):
    print(index) 
    print(letter)
    print('\n')



mylist1 = [1,2,3]
mylist2 = ['a','b','c']
zip(mylist1,mylist2)




mylist1 = [1,2,3]
mylist2 = ['a','b','c']
for _ in zip(mylist1,mylist2):
    print(_)




mylist1 = [1,2,3]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]
for _ in zip(mylist1,mylist2,mylist3):
    print(_)


mylist1 = [1,2,3]
mylist2 = ['a','b','c']

joinedlist = mylist1 + mylist2
print(joinedlist)



mylist1 = [1,2,3,4,5,6]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]
for _ in zip(mylist1,mylist2,mylist3):
    print(_)




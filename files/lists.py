my_list = [1,2,3,4,5]

len(my_list)

print(len(my_list))

my_list = [1,2,3]

print(my_list[0])
print(my_list[1:])

my_lista = ['one', 'two', 'three']
list_two = ['four', 'five']

print(my_lista + list_two)

new_list = ['one,' 'two', 'three', 'four', 'five']
new_list[0] = 'ONE ALL CAPS'
print(new_list)
new_list.append('six')
print(new_list)
new_list.append('seven')
print(new_list)

pop_list = ['one', 'two', 'three', 'four', 'five']
print(pop_list.pop())
print(pop_list)

pop_list = ['one', 'two', 'three', 'four', 'five']
print(pop_list.pop(0))
print(pop_list)

sort_list = ['a', 'e','x' , 'b' , 'c']
numb_list = [4,1,8,3]
print(sort_list.sort())
print(sort_list)
print(numb_list)
print(numb_list.sort())
print(numb_list)


sort_list = ['a', 'e','x' , 'b' , 'c']
numb_list = [4,1,8,3]
print(sort_list.reverse())
print(sort_list)
print(numb_list)
print(numb_list.reverse())
print(numb_list)


list3 = [1,2,[3,4, 'hello']]
list3[2][2] = 'goodbye'
print(list3)

list4 = [1,2,3,4]
print(sorted(list4))

list5 = [1,2,3,44,3,22,5,6,7,2,3,4]
print(set(list5))

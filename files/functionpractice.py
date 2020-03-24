# def lesser_two(a,b):
#     if a%2 == 0 and b%2 == 0: 
#         if a < b:
#             result = a
#         else:
#             result = b
#     else:
#         if a > b: 
#             result = a
#         else: 
#             result = b 
# lesser_two(2,9)
str='keith'
stringlength=len(str)
slicedString=str[stringlength::-1]
print (slicedString) 

s = 'keith is amazing'

stringlength=len(s)
slicedString2=s[stringlength::-1]
print (slicedString2) 

for num in range(1,10):
    if num%2 !=0:
        print(num)


mylist = [1,2,3,2,3,4,3,4] 
def has_33(nums):
    for i in range(0,len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True 
        return False

print(has_33([1,2,3,3]))
  

# mylist = [1,2,3,2,3,4,3,4] 
# def has_33(nums):
#     for i in range(0,len(nums)-1):
#         if nums[i:i+2] == [3,3]
#             return True 
#     return False

# print(has_33([1,2,3,3]))
  
my_list = [1,2,3]
print(my_list[::-1])

my_list = [1,2,3]
print(my_list)




# def spy_game(nums):
#     code = [0,0,7, 'x']

#     for num in nums:
#         if num == code[0]:
#             code.pop(0)

# def lesser_of_two(a,b): 
#     if a%2 == 0 and b%2 == 0: 
#         if a < b: 
#             result = a 
#         else:
#             result = b
#     else:
#         if a > b:
#             result = a
#         else:
#             result = b

def old_mcdonald(name):
    first_letter = name[0]
    inbetween = name[1:3]
    fourth_letter = name[3]
    rest = name [4:]

    return first_letter + inbetween + fourth_letter + rest
print(old_mcdonald)
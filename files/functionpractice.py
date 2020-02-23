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
  
# */stop here/*
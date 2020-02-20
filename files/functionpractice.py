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

for num in range(1,100):
    if num%2 !=0:
        print(num)

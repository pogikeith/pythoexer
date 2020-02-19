
def myfunc(**kwargs):
  if 'fruit' in kwargs:
    print('my fruit is {}'.format(kwargs['fruit']))
  else:
    print('no fruit')
myfunc()
   
myfunc(fruit='apple', veggie = 'lettuce')
   

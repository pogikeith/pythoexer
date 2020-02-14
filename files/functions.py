def name_function(): 
    print('Hello')
name_function()


def say_hello(name): 
    print('hello '+ name)
say_hello('jose')


def say_hello(name='NAME'): 
    print('hello '+ name)
say_hello()


result =  say_hello('AL')


def say_hello(name='NAME'): 
    return 'hello '+ name
result =  say_hello('VAL')
print(result)


def add(n1,n2):
    return n1+n2
result = add(20,30)
print(result)


#find out if word dog is in string

def dog_check(string):
    if 'dog' in string: 
        return True
    else: 
        return False
dog_check('my dog ran away')


def dog_check(string):
    if 'dog' in string.lower(): 
        return True
    else: 
        return False
dog_check('my dog ran away')


def dog_check(string):
    if 'dog' in string.lower():
        return True
    else: 
        return False
dog_check('my dog ran away')


def dog_check(string):
    return 'dog' in string.lower()
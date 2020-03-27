x = 25
def printer():
    x=50
    return x
print(x)
print(printer())

# //global
name = 'this is global string'

def greet(): 
    name = 'Im a local'
    def hello():
        print('hello ' +name)
    hello()
greet()


x = 50
def func(x):
    print(f'X is {x}')

    x=200
    print(f'i just locally changed x to {x}')
func(x) 
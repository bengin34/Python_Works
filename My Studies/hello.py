def function(): # Don't be confused, we use 'def()' to create a function. 
                # You will see it in the next lessons.
    """
Hi, I am the docstring of this code. 
If you need any information about this function or module, read me. 
It can help you understand how the module or function works.
    """
print(function.__doc__)

example1 = 'sometimes what you say is less important than how you say it'
print(type(example1))

f = 3.14  # the type is float
print(type(f)) 

s = bool(f)  # converting float to string
print(type(s)) 

i = 3

f = float(i)
print(f, '\n')
print(type(f)) 


x = 39
v = "11"
y = "2.5"
z = "I am at_"

print(x-int(v))
print(x-float(y))
print(z+str(x))

color = 'red'  # str type variable
season = 'summer'
price = 250  # int type variable
pi = 3.14  # float type variable
color = 'blue'  # You can always assign a new value to a created variable
price = 100  # value of 'price' is changed
season = 'winter'  

print(color, price, season, sep=' * ')

a = 5
b = 55
c = 555
c = a
b = c
a = b

print(a, b, c, sep=', ')

# pi = 3.14159
# print(pi)

first_num = input('Please enter a number')
second_num = input('Please enter another number')

print(int(first_num) + int(second_num))
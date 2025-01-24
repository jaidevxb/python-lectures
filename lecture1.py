# type() is a function that returns the data type of the object
print(type(69)) # <class 'int'>
print(type(6.9)) # <class 'float'>
print(type([1,2,3])) # <class 'list'>
print(type(True)) # <class 'bool'>

# type conversion or type casting
print(float(62)) # 62.0
print(int(2.6)) # 2 (acts like floor)
print(round(4.6)) # 5 
print(int(True)) # 1
print(float(round(5.8))) # 6.0

# expressions -> combine objects and operators
print(5/3) # 1.6666666666666667
print(type(5/3)) # <class 'float'>
print(int(5/3)) # 1

# PEMDAS
# MD and AS -> left to right
print((4+5) * 2) # 18
print(4 + 5 * 2) # 14
print(5 + 2 * 10 / 2**2) # 10.0 true division(/) always returns float
# + , - , * -> if both are int result is int if either or both are float result is float
print(10 % 3)

# variables
pi = 355/113
print(pi) # 3.1415929203539825
radius = 5
area = pi * radius**2
print(area) # 78.53982300884957
print(round(area)) # 79

celcius = 50
fahrenheit = (celcius * 9/5) + 32 
print(fahrenheit) # 122.0
print(int(fahrenheit)) # 122 
# fahrenheit = int((celcius * 9/5) + 32)

meter = 100 # meter is 100
feet = 3.2808 * meter # meter is 100 and feet is 328.08
meter = 200 # meters is rebound to 200

x = 10
y = 20
print(f"before swap x = {x} y = {y}") # x = 10 y = 20
temp = x
x = y
y = temp
print(f"after swap x = {x} y = {y}") # x = 20 y = 10

# Finger Ex lecture 1
""" Assume 3 variables are already defined for you: a, b, and c. 
Create a variable called total that adds a and b then multiplies the result by c. 
Include a last line in your code to print the value: print(total) """ 
# """ can be used for multiline comment but they are string literals

a = 10
b = 20
c = 5
total = (a + b) * c
print(total) # 150






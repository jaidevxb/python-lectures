# str -> sequence of case sensitive characters enclosed within ' ' " " or ''' '''
a = "Jaidev"
b = 'EEE'
c = a + ''' ''' + b # concatenate use +
print(c) # Jaidev EEE
# multiline strings are stored in triple quotes
d = "jaidev
eee"
print(d) # error
e = 'HI '
print (e * 3) # repeat use * (HI HI HI)
print((e + "Jaidev ") * 3) # HI Jaidev HI Jaidev HI Jaidev 
i = ':'
f = ')'
print(i + 2*f)

# len() -> function used to retrive the length of string
len("Jaidev") # 6
m = "Jaidev EEE 1st Year"
len(m) # 19
m[0] # 'J' 0 based indexing
m[6] # ' '
m[-1] # 'r'
m[-5] # ' '
m[0] == m[-19] # True

# slicing -> to get substring [start:stop:step] -> step not necessary if not specified by default 1
l = "abcdefgh"

l[3:6] # def
l[3:6:2] # df
l[:] # abcdefgh
l[::-1] # hgfedcba
l[4:1:-2] # ec

# input output in python

print("Hello World!") # Hello World!
get = input("Enter a word : ") # Hi
print(get) # Hi
num = int(input("Enter a number : ")) # the default type in string in input fn
print(num) # 15 or whatever no. i give
print(type(num)) # <class 'int'>
num2 = input("Enter 2nd number : ") # 20
print(num2) # 20
print(type(num2)) # <class 'str'>

# given 5 for both num
print(num * 3) # 15
print(num2 * 3) # 555

# Newton's method to find roots eg (g^3-x=0)

x = int(input("Enter a number to find cube root:"))
g = int(input("Enter a guess to start with:"))
print("The cube of current guess is:",g**3)
next_g = g - ((g**3-x)/(3*g**2))
print("The next guess is", next_g) # finds the next guess

# F string -> formatted string bracketed by {}

num = 3000
fraction = 1/3
print(num*fraction, 'is', fraction*100, '% of', num)
print(num*fraction, 'is', str(fraction*100) + '% of', num)
print(f'{num*fraction} is {fraction*100}% of {num}')

# branching -> if, if else, if elif else
number = 3
guess = int(input("enter a number : "))
print(number == guess)

num = 5
guess= int(input("Guess a number : "))
if num == guess: # True / False
    print("Both numbers are same") 
elif num > guess:
    print("Guess is too low") 
else: # can use this also as elif else is not mandatory like c++ (in else if ladder)
    print("Guess is too high")




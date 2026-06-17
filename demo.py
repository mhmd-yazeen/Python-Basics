print("Hai")
print("Yazin")
print("Welcome to Python")
print("\n")

# variables
# Variables are used to store data in memory. They can be of different types such as integers, floats, strings, etc.
# Varible with same values are stored in defferent memory locations
A = 10
a = 50
A = 20
print(id(a)) 
print(id(A))
print(type(A))
print("The value of a is:", a)
print("\n")

#Data Types
A = 5
print(type(A)) #Int
A = 5.67
print(type(A)) #Float
A = "Hello"
print(type(A)) #String
print("\n")

# Arithmetic Operator
#Addition
print(5+6)
#Subtraction
print(10-6)
#Multiplication
print(2*5)
#Division
print(20/2)
#Exponent, Power
print(2**4)
#Floor Divison , Quatiant
print(15//2)
#Modulus , Reminder
print(15%2)
print("\n")

# Comparisson Operators
# Equal to
a=10
b=15
print (a == b)
# Not Equal to
a=10
b=15
print(a != b)
# Greather than
a=10
b=15
print(a > b)
# Less than
a=10
b=15
print(a < b)
# Greather than or =
a=10
b=15
print(a >= b)
# Less than or =
a=10
b=15
print(a <= b)
print("\n")


# Conditional Statements
# If , Elif , else
age = 18
if age < 18:
    print("Not eligible")
else:
    print("Eligible")
print("\n")

# Logical Operators
# And , Or , Not
a=10
b=20
if (a>5 and b>5):
    print("Ok")
print("\n")

a=10
b=20
if (a>5 or b>5):
    print("Ok")
print("\n")

a=10
b=20
if (not a==10):
    print("Ok")
print("\n")


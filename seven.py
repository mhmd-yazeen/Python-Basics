# needed to split the list into two parts
a = [11,13,14,15,16,17,18,19,20,21]
b = len(a)//2
l = []
l1 = []
for i in range(len(a)):
    if i < b:
        l.append(a[i])
    else:
        l1.append(a[i])
print(l)
print(l1)
print()

# print the largest and smallest number
a = [11,1,100,-900,10,15,16]
l = max(a)
li = min(a)
print(f"largest = {l}")
print(f"smallest = {li}")
print()

a = [11,1,100,-900,10,15,16]
largest = 0
smallest =0
for i in a:
    if i > largest:
        largest = i
    elif i < smallest:
        smallest = i
print("largest is ", largest)
print("smallest is", smallest)
print()


# functions
# bloack of code which is executed when it is called
# def functionname(<argument>)
    #code to be executed

def hello():
    print("Hello how are you")

hello() #calling the function
hello()
print()

# arguments - values to be passed to an function
# parameters

def add(a,b): # former parameter
    print("addition",a+b)
    print("subtraction",a-b)
a = 152
b = 124
add(a,b) # actual parameter

# types of argumeents
# 1.possitional argument
def add(a,b):
    print(a+b)
add(5,10)
# 2.keyword argument
def add (a,b):
    print(a+b)
add(b=5,a=20)

def name(fname,mname,lname):
    print(fname+" "+mname+" "+lname)
name(fname='rahul',mname = 'mohan',lname = ' mr')

# 3.default argument
def add (a=0,b=0):
    print(a+b)
add()
add(3)
add(4,3)

# return statement


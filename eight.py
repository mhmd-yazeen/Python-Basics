# return statement
def add1(a,b):
    return "Faslim"

# the value of the function is given in retun
print(add1(1,2))
print()

# lambda function
# anonymous function
# Lambda arguments : expression
z = lambda x,y : x+y
print(z(2,3))
print()
# product of 3 numbers
pro = lambda x,y,z : x*y*z
print("product of three number: ",pro(2,3,5))
print()
# square of an number 
sq = lambda x : x**2
print("square of number: ",sq(5))
print()
# perimeter of an circle
per = lambda x : 2*3.15*x
print("Perimeter is ",per(6))
print()
# Area of traingle
are = lambda x,y : (1/2*(x*y))
print("Area is", are(5,4))
print()
# Average of 5 numbers
avg = lambda a,b,c,d,e : 1/5*(a+b+c+d+e)
print("Average is",avg(5,8,4,6,1))
print()
# Square root of an number
squ = lambda x : x**1/2
print("Square root", squ(5))
print()
# full name of person
full = lambda fname,mname,lname: fname+mname+lname
print(full("faslim"," rahim"," son"))
print()

# Turney operator 
age = 21
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

print("eligible") if age >= 18 else print("not eligible")

check = lambda  age : "eligible" if age >= 18 else "not eligible"
print(check(21))

# Age Calculator
# Bmi calculator


# Swapping of two numbers
A = 5
B = 10
temp = A
A = B
B = temp
print(A)
print(B)
print("\n")

A = 5
B = 10
A ,B = B , A
print(A)
print(B)
print("\n")

A = 5
B = 10
A = A + B #15
B = A - B #5
A = A - B #10
print(A)
print(B)
print("\n")

# Check an number is even or odd
Num = 10
if Num%2 == 0:
    print("Even")
else:
    print("Odd")
print("\n")


#check if an number is multiple  of 5
Num = 18
if Num%5 == 0:
    print("Multiple of 5")
else:
    print("Not Multiple of 5")
print("\n")

# Largest of two numbers
a = 10
b = 20
if a>b:
    print("a is greather")
else:
    print("b is greater")
print("\n")

Mark = 50
if Mark > 70:
    print("A")
elif Mark > 60:
    print("B")
elif Mark > 50:
    print("C")
else:
    print("Fail")
print("\n")

# Check if an number is Possitive , Negative or Zero
Num = -15
if Num > 0:
    print("Possitive")
elif Num < 0:
    print("Negative")
else:
    print("Zero")
print("\n")

# Largest of three Number
a = 10
b = 11
c = -100
if (a>b and a>c):
    print("a is largest")
elif (b>a and b>c):
    print("b is largest")
else:
    print ("c is largest")
print("\n")

# check an numbe is multipe of 3 and 5
num = 17
if (num%3 == 0 or num%5 ==0):
    print("Multiple of 3 & 5")
else:
    print("Not Multiple")

#for adding two numbers
a = "10"
b = "20"
print (a+" "+b)
print(a+b)
print("\n")

A = int(input("Enter the first number:"))
B = int(input("Enter the second number:"))
print(A+B)

# Sum of first 10 number
num = 1
sum = 0
while num <= 10:
    sum = sum+num
    num = num+1
print(sum)
print("\n")

# sum of odd number and even numbers in 100
num = 1
odd_sum = 0
even_sum = 0
while num <= 100:
    if num%2==0:
        even_sum = even_sum + num
    else:
        odd_sum = odd_sum+num
    num = num+1
print(odd_sum)
print(even_sum)

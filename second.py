# sum of digits in an number
num = 12345
sum = 0
dig = 0
while num > 0:
    dig = num % 10
    sum = sum + dig
    num = num // 10
print(sum)
print("\n")

# reverse of an number
num = 12345
rev = 0
dig = 0
while num > 0:
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10
print(rev)
print("\n")

# factorial of an number
num = 5
# num = int(input("Enter the numbers : "))
fac = 1
while num > 0:
    fac = fac * num
    num = num - 1
print(fac)
print("\n")

# for loop
# range (start,stop,step)
for i in range (1,10,2):
    print (i)
print("\n")

# 100 number sum
sum = 0
for i in range (101):
    sum = sum + i
print(sum)
print("\n")

# Factorial of an number
num = 5
fact = 1
for i in range(num):
    fact = fact*num
    num = num-1
print (fact)
print("\n")

# Multiplication table of an number
num = 5
for i in range(1,11):
    print(f'{num} x {i} = {num*i}')
print("\n")

# Sum and average of numbers
count = int(input("Enter the number : "))
sum = 0
for i in range (count):
    num = int(input("Enter you number :"))
    sum = sum + num
# print(f"Sum is {sum}")
print("sum is",sum)
print(f"Average is {sum/count}")


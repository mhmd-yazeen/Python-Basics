# Fibonacci Sequence
# 1,1,2,3,5,8,13,21,34,55

num = int(input("Enter the number: "))
a =0
b =1
for i in range(num):
    print(a, end=" ")
    temp = a + b
    a = b
    b = temp
print("\n")



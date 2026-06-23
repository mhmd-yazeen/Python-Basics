num = 153
temp = num
num1 = num
amg = 0
count = 0
while num1>0:
    num1 = num1//10
    count = count+1
for i in range(count):
    dig = num%10
    amg = amg + dig**count
    num = num//10
print(amg)
if temp == amg:
    print(f"{temp} is amstrong number")
else:
    print(f"{temp} not an amstrong number")


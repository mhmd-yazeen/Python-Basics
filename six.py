# Nested loops

for i in range(1,6):
    for j in range(1,6):
        for k in range(1,6):
            print(i,j,k)
print()

for i in range (5):
    print("\n")
    for j in range(5):
        print("*",end=" ")
print()

# patterns 
for i in range (5):
    for j in range (1,i+1):
        print("*",end=" ")
    print()
print()

num = 6
for i in range (num):
    for j in range (num,i,-1):
        print("*",end=" ")
    print()
print()

# pyramid pattern
num = 6
for i in range(num):
    for j in range(num-i):
        print(" ",end = "")
    for i in range(i+1):
        print("* ",end = "")
    print()
print()

# chess pattern
num = 7
for i in range(1,num):
    for j in range(1,num):
        m = (i+j) % 2
        if m == 0:
            print("W",end=" ")
        else:
            print("B",end=" ")
    print( )


# capital H and I in pattern
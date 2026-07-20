string = input()
x = 0
y = 0
for i in range(len(string)):
    if string[i] == 'z':
        x = x + 1
    elif string[i] == 'o':
        y = y + 1
    else:
        print("invalid choice")

temp = 2 * x       

if temp == y:
    print("Yes")
else:
    print("no")



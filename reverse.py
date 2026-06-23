# reverrse of an string without using [::-1]
a = "Hello"
for i in range(len(a)-1, -1, -1):
    print(a[i],end = "")
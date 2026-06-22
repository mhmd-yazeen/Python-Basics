# find vowels and there position in a string
# a = input("Enter the word :")
a ="Yazeen"
l = ["a","e","i","o","u","A","E","I","O","U"]
for i in range(len(a)):
    if a[i] in l:
        print(i,"-",a[i])
print("\n")

# in operator membership operator 
# for i in 

# create a list of even numbers and odd numbers from first 100
a = 101
odd = []
even =[]
for i in range (a):
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(f"Odd number - {odd}")
print(f"Even number - {even}")
print("\n")


# Remove duplicates from the list
lis = [1,2,3,4,1,3,4,2,7,8,9,2,3,4,5]
b = []
for i in lis:
    if i not in b:
        b.append(i)
print(f"List - {b}")

#break continue pass
# break - break the loop
for i in range(1,10):
    if i == 5:
        break
    print(i)
print("\n")
# continue - skip the current iteration
for i in range(1,10):   
    if i == 5:
        continue
    print(i)
print("\n")
# pass - do nothing using for error skipping
for i in range(1,10):
    if i == 5:
        pass
    print(i)
print("\n")


# input n word  make it an sentance
# reverrse of an string without using [::-1]
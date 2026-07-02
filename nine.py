# Recursion
def counttozero(num):
    print(num)
    if num == 0:
        return
    return counttozero(num-1)

def main():
    num = 5
    counttozero(num)
main( )
print( )

# sum of 10 numbers
def sum10 (num):
    if num == 0:
        return 0
    return num + sum10(num - 1)

print(sum10(5))

# scope of an variable 
# scope - area in which it is recognised

name = "Ameen" # global scope
def myname():
    name = "Jithin" # local scope
    print(name)
    def nickname():
        name = "Athul" # local scope
        print(name)
    nickname()

print(name) #global name
myname()
print()
# L E G B
# local enclosing global built jn

# modules

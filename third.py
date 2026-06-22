
#list
# list is a collection of items which is ordered and changeable. it allows duplicate members.
mylist = [1,2,3.5,"mohan",4,5]
# list can store int,float
#list are orderd
#list are indexed 0,1,2,3,4,5 and -6,-5,-4,-3,-2,-1

list = [10,20,30,40,50,60]
print(list)
#[start:end:step]
print(list[0])
print(list[2:5:1])
print(list[:5])
print(list[::2])
print(list[-2])
print(list[::-1])
print(mylist[2:4])
print("\n")

# list concept can also be use in strings

name = "Muhammed Yazeen"
print(name[0:6])
print(name[:5])
print(name[::2])
print(name[::-1]) # for reversing an string (step = -1)
print(name[14]==name[-1]) 
print("\n")

# list are mutable
list = [10,20,30,40,50,60]
list[2] = "mohan"
print(list)
# string are imutable
# list are nested a[b[0,1]]
list = [10,20,[100,[1000],200],50]
print(list[2][0])
print(list[2][1][0])
print("\n")

# inbuilt methods
# append - to add an element to the last position
l = [10,20,30,40,50]
l.append(100)
l.append(200)
print(l)
print("\n")

# extend - to add an list of elements to the list
l = [10,20,30,40,50]
l.extend("Yazeen")
l.extend([12,22,"Yazeen",10])
print(l)
print("\n")

#insert - to add an element to an index position
# insert(index,value)
l = [10,20,30,40,50]
l.insert(0,100)
l.insert(2,"Yazeen")
print(l)
print("\n")

# remove - to remove the element from the list
# remove(element)
l = [10,20,30,40,50,"yazeen",10]
l.remove(10)
l.remove("yazeen")
print(l) 
print("\n")

# pop to remove the element from last or using index
# pop(index)
l = [10,20,30,40,50,10]
l.pop()
l.pop(0)
l.pop(0)
print(l) 
print("\n")

# tuple
# collection of data ()
# has order and index
# tuple is imutable (no change posible)
t = (10,20,30,40,50)
print(t)
print(t[1])
print(t[::-1]) # reversing
print("\n")

# for loop using str, list & tuples
# tuple
t = (10,20,30,40,50)
for i in range(len(t)):
    print(i,t[i])
print("\n")

# list
l = ["Tata","Mahindra","Toyota","Maruti"]
for i in range(len(l)):
    print(i,l[i])
print("\n")


l = ["Tata","Mahindra","Toyota","Maruti"]
num = len(l)
print(num)
for i in range(num):
    print(i,l[i])



# set
# collection of data {}
a = {1,2,3,4}
b = {2,4,1,3}
print(a == b)
print("\n")

# unordered and no index
seet = {"apple","banana","cherry"}
for i in seet:
    print(i)
print("\n")

# a = set(a) to covert to set
# to remove duplicate values from a list
a = [10,20,14,14,10,20,14,50,60,50]
a = set(a)
print(a)
print("\n")

#operators in set
a = {5,1,2,3,4}
b = {4,5,6,7,8}
print(a.union(b))
print(a|b)
print(a.intersection(b))
print(a&b)
print(a-b)
print(b-a)
print("\n")

# dictonery
# collections of data{ key : value}
# has no index
data = {"name" : "Yazeen", "age" : "21", "city" : "kochi"}
print(data["name"])
print(data["age"])
print(data["city"])
print("\n")

data = { }
data["name"] = "Yazeen" #input("Enter the name :")
data["age"] = 21 #input("Enter the age :")
data["city"] = "kochi" #input("Enter the city :")
data["email"] = "myazeen@gmail" #input("Enter the mail adress :")
print(data)
print("\n")

#dictoney are mutable dict
#dictoney are dynamic
data["name"] = "priya"
print(data)

print(data.get("name")) 
print(data["email"])
print(data.keys()) # get key in dict
print(data.values()) # get the values in dict
print(data.items()) # get the key value pair
data.update({"number": 7025860960})
print(data) 
data.pop("name") # remove the key and value
print(data)
data.popitem() # remove the last modifed key
print(data)
data.clear() # clear all the datas
print(data)
print("\n")

data = {'name': 'priya', 'age': '21', 'city': 'kochi', 'email': 'myazeeb', 'number': 7025860960}
for i in data:
    print(i,data[i])
print("\n")
for i in data.keys():
    print(i)
print("\n")
for i in data.values():
    print(i)
print("\n")
for i,j in data.items(): # i for key and j for values ( for tuples )
    print(i,j)
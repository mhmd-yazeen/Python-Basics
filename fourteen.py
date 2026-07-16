# Decorators
# functions that enhances other function

def saymyname(fun):
    def wrapper():
        print("Say my Name")
        fun()
        print("You are right")
    return wrapper

@saymyname
def add():
    print("add 2 numbers")
@saymyname
def hello():
    print("HELLLOOOO")

hello()
add()
print()

def num(*args):
    print(args)
num(10,20,30,35)

def fullname(**kwargs):
    print(kwargs)
fullname(fname="mohan",lname="das")
print()


# Time
import time
print(time.time())
print(time.ctime())
print(time.ctime(0))

# start = time.time()
# for i in range(1,6):
#     print(i," Hello")
#     time.sleep(1)
# stop = time.time()
# print("total time:",stop - start)



def totaltime(fun):
    def wrapper(*args,**kwargs):
        start = time.time()
        fun(*args,**kwargs)
        stop= time.time()
        print(f"total time : {stop-start}")
    return wrapper

@totaltime
def myname(n):
    for i in range(n):
        print(i)
        time.sleep(1)

myname(5)

# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40






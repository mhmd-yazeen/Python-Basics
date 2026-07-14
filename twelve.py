#inheritance
# Single level
# Multiple level

class person1:
    def __init__(self):
        pass
    def walk(self):
        print("Person 1 can walk")
    def smile(self):
        print("Person 1 can smile ")
    def speak(self):
        print("Person 1 can Speak")

class person2(person1):
    def __init__(self):
        pass
    def fly(self):
        print("Person 2 can fly")
    def swim(self):
        print("Person 2 can swim")
    def speak(self):
        print("Person 2 can Speak")

class person3(person2):
    def __init__(self):
        pass
    def read(self):
        print("Person 3 can walk")
    def write(self):
        print("Person 3 can smile ")
    def speak(self):
        print("Person 3 can Speak")
        super().fly()

class person4(person3):
    def __init__(self):
        pass
    def sleep(self):
        print("Person 4 can sleep")
    def eat(self):
        print("Person 4 can eat ")
    def speak(self):
        print("Person 4 can Speak")
        super().speak()

# class person5(person1,person2,person3,person4):
#     def __init__(self):
#         pass
#     def speak(self):
#         print("Person 5 can Speak")

p4=person4()
p4.speak()
print()

# polymorphsm
# Poly - many and morph - form

# operator overloading
class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self,otr):
        return self.m1+self.m2,otr.m1+otr.m2
    def __sub__(self,otr):
        return self.m2-self.m1,otr.m2-otr.m1
    def __mul__(self,otr):
        return self.m1*self.m2,otr.m1*otr.m2
    def __truediv__(self,otr):
        return self.m2/self.m1,otr.m2/otr.m1
    def __gt__(self,otr):
        return self.m2>self.m1,otr.m2>otr.m1

s1 = Student(6,12)
s2 = Student(9,18)
print(s1+s2)
print(s1-s2)
print(s1*s2)
print(s1/s2)
print(s1>s2)


#  method overriding
class A:
    def __init__(self):
        pass
    def hello(self):
        print("A hello")

class B:
    def __init__(self):
        pass
    def hello(self):
        print("B Hello")

b = B()
b.hello()



# Exception
# events that affect the execution of our program

try:  
    a = 5
    b = s
    print(a/b)
except Exception as e:
    print("you have an error",e)
print("Answer")
print()

try:
    a = "Das"
    b = 5
    print(a/b)
except ZeroDivisionError:
    print("You cannot divide a number with zero")
except ValueError:
    print("Check Values")
except TypeError:
    print("check types")
finally:
    print("this will always execute")
print()

# raise keyword 

# class myerror(Exception):
#     pass
# name = "das"
# if name == "das":
#     raise myerror("name should not be das")


# to delete from the memory
# a = 5
# del(a)
# print(a)

# file handling
# read text based

file1 = open("data.txt","r")
print(file1.read())
file1.close()

# over write
file2 = open("myfile.txt","w")
file2.write("this month is july ")
file2.close

file3 = open("myfile.txt","a")
file3.write("\nHello")
for i in range(1,100):
    file3.write(f"\nJohns {i}")

# with open("myfile.txt")


import os

#os.mkdir("images") - for creating file
#os.remove("data.txt") - for removing file
#os.rename("myfile.txt","demo.txt")
pat = "C:\\Users\\HP\\OneDrive\\Desktop\\Hello.txt.txt"
if os.path.exists(pat):
    if os.path.isfile(pat):
        print("file exixts")
    elif os.path.isdir(pat):
        print("folders exists")



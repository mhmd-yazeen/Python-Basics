# check if an number is prime or not
#2,3,5,7,13
num = int(input("Enter the number: "))
if num>1:
    for i in range(2,num):
        if num%i == 0:
            print(f"{num} is not a prime number")
            break
        else:
            print(f"{num} is a prime number")
            break
else:
    print("Not an prime number")
    


#strings
# Sequence of Series "Mohan"

Name = "Yazeen"
print(Name)
print(type("Name"))
print("\n")

name = "Yazeen's Iphone"
print(name)
print("\n")

B = '''Gandi once said that "say not to violence" '''
print(B)
print("\n")

#escape sequence 
# \'  \'
# \"  \"
# \n for new line
# \t for tab
# \b for backspace

name = 'Yazeen\'s Iphone'
print(name)
print("\n")

B = 'Gandi once said that : \n\t\t \"say not to violence\" '
print(B)
print("\n")

#raw String
C = r'Gandi \b once \tsaid that : \n\t\t \"say not to violence\" '
print(C)
print("\n")

#type conversion
# str()  int()  float()  
#implicit type conversion
#explicit type conversion


#string formatting
name = "Yazeen"
age = 20
print(f"My name is {name} and my age is {age}")

#conditional statements
#loops

i = 1
while i <= 10:
    print(i)
    i = i + 1
print("Finish")
print("\n")


i = 50
while i <= 10:
    print(i)
    i = i + 1
print("Finish")
print("\n")

# Sum of first 10 number
num = 1
sum = 0
while num <= 10:
    sum = sum+num
    num = num+1
print(sum)
print("\n")

# sum of odd number and even numbers in 100
num = 1
odd_sum = 0
even_sum = 0
while num <= 100:
    if num%2==0:
        even_sum = even_sum + num
    else:
        odd_sum = odd_sum+num
    num = num+1
print(odd_sum)
print(even_sum)

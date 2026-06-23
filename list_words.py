# list of words to an string 
num =int(input("Enter the number of words:"))
words = [ ]
for i in range(num):
    word = input("Enter the word :")
    words.append(word)
words1 = " ".join(words)
print(words1)
print(type(words1))




#output
# Enter the number of words:2
# Enter the word :hai
# Enter the word :hello
# hai hello
# <class 'str'>
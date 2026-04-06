# Lecture 2 Practice 4
#  Find greatest of 3 numbers
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

if (a>=b and a>=c):
    print(a,"is largest number")
elif (b>=c):
    print(b,"is largest number")
else:
    print(c,"is largest number")

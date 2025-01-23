# Print Hello World
print("Hello World!")

#Input Number and print it
a=int(input("Enter First Number - "))
print("Your number Is - ", a)

#Print String
c = "Kunj"
print(c)

#Basic if - else statement
a = 70
b = 20
if(a>b):
    print("A is greater than B")
else:
    print("B is greater than A")

#Swap Numbers
i = 23
j = 32
k = 0

print("I is ", i)
print("J is ", j)
print("After Swap")

k = i
i = j
j = k

#OR a,b=b,a

print("After Swap I is ", i)
print("After Swap J is ", j)

#WAP to input basic salary, HRA, DA. Calculate Gross Salary

z=int(input("Enter Basic Salary - "))
x=int(input("Enter HRA - "))
c=int(input("Enter DA - "))

GS = z + x + c

print("Gross Salary Is - ", GS)

#Basic Loops

i=1
while(i<=10):
    print(i)
    i=i+1

for i in range(1, 11):
    print(i)


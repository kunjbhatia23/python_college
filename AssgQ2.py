#Print all numbers in a range divisible by a given number
n=int(input("Enter Number - ")) 
for i in range (1,n+1):
    if(n%i) == 0:
        print(i)
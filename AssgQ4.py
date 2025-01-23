#Program to find sum of digits in a number

num=int(input("Enter Number - ")) 
sum = 0

while num > 0:
    rev = num % 10
    sum += rev
    num = num // 10

print("Sum Of The Digits Is - ", sum)
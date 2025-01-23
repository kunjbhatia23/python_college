#Program to find smallest divisor of an integer (other than 1)

def find_smallest_divisor(n):
    for i in range(2, n + 1):
        if n % i == 0:
            return i
number = int(input("Enter an integer greater than 1: "))
result = find_smallest_divisor(number)
print(f"The smallest divisor of {number} other than 1 is: {result}")
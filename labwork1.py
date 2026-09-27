#-----EXERCISE 1-----
radius = float(input("Enter circle radius? "))
area = 3.14 * radius * radius
print(f"Circle area = {area}")



#-----EXERCISE 2-----
celsius = input("Enter the temperature in Celsius? ")
fahrenheit = float(celsius) * 9 / 5 + 32
print(f"{celsius} (C) = {fahrenheit} (F)")



#-----EXERCISE 3-----
num = int(input("Enter a number? "))

is_prime = True
if num < 2:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is a NOT prime number")



#-----EXERCISE 4-----
num = int(input("Enter a number? "))

sum_divisors = 0
for i in range(1, num):
    if num % i == 0:
        sum_divisors += i

if sum_divisors == num and num > 0:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is a NOT perfect number")



#-----EXERCISE 5-----
my_list = ['Blue', 'Yellow', 'Black', 'Red', 'White', 'Green', 'Orange', 'Purple', 'Pink', 'Brown']

color = input("What is your favorite color? ")
if color in my_list:
    print(f"Your color is at index {my_list.index(color)} in my list")
else:
    print("Sorry, I could not find your color")



#-----EXERCISE 6-----
print("range1:", list(range(7)))          # Output: 0, 1, 2, 3, 4, 5, 6
print("range2:", list(range(1, 11, 3)))   # Output: 1, 4, 7, 10
print("range3:", list(range(5, 0, -1)))   # Output: 5, 4, 3, 2, 1
print("range4:", list(range(6, -3, -2)))  # Output: 6, 4, 2, 0, -2



#-----EXERCISE 7-----
def remove_dollar_sign(s):
    return s.replace("$", "")



#-----EXERCISE 8-----
def extract_even(l):
    return [x for x in l if x % 2 == 0]



#-----EXERCISE 9-----
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result



#-----EXERCISE 10-----
def get_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors



#-----EXERCISE 11-----
import math

print("--- Calculate distance between two points ---")
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"The distance between the two points is: {distance}")



#-----EXERCISE 12-----
def print_pattern(m, n):
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                print("* ", end="")
            else:
                print("  ", end="")
        print() 
for i in range(1, 11):
    print(i)


# Get user input for the number
number = int(input("Enter a number: "))


range_limit = 10


print(f"Multiplication table for {number}:")
for i in range(1, range_limit + 1):
    result = number * i
    print(f"{number} * {i} = {result}")


    # Get user input for the maximum number
max_number = int(input("Enter a positive integer: "))


sum_of_numbers = 0
current_number = 1


while current_number <= max_number:
    sum_of_numbers += current_number
    current_number += 1


print(f"The sum of natural numbers up to {max_number} is: {sum_of_numbers}")

# List of names
names = ["Ali", "akbar", "khan", "arsalan", "muzamil"]


print("List of Names:")
for name in names:
    print(name)


    # Get user input for the number
number = int(input("Enter a non-negative integer: "))


factorial = 1
current_number = 1


while current_number <= number:
    factorial *= current_number
    current_number += 1


print(f"The factorial of {number} is: {factorial}")



def fibonacci(n):
    fib_series = [0, 1]

    for i in range(2, n):
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)

    return fib_series

# Get the number of terms from the user
num_terms = int(input("Enter the number of Fibonacci terms you want: "))


if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    
    result = fibonacci(num_terms)
    print(f"Fibonacci series up to {num_terms} terms: {result}")





def reverse_number(number):
    reversed_num = 0

    while number > 0:
        digit = number % 10
        reversed_num = (reversed_num * 10) + digit
        number = number // 10

    return reversed_num

# Get the number from the user
user_number = int(input("Enter a number to reverse: "))


result = reverse_number(user_number)
print(f"Reversed number: {result}")






def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0

    for char in input_string:
        if char in vowels:
            vowel_count += 1

    return vowel_count

# Get the input string from the user
user_input = input("Enter a string: ")


result = count_vowels(user_input)
print(f"Number of vowels in the string: {result}")




def is_palindrome(number):
    original_number = number
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = (reversed_number * 10) + digit
        number = number // 10

    return original_number == reversed_number

# Get the number from the user
user_number = int(input("Enter a number to check for palindrome: "))


if is_palindrome(user_number):
    print(f"{user_number} is a palindrome.")
else:
    print(f"{user_number} is not a palindrome.")




    
sum_of_squares = 0


for num in range(1, 6):
    
    sum_of_squares += num ** 2


print("Sum of the squares of numbers from 1 to 5:", sum_of_squares)

# Get input from the user
number = int(input("Enter a number: "))


if number % 2 == 0:
    print("Even")
else:
    print("Odd")


    # Get input from the user
year = int(input("Enter a year: "))


if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


    # Get input from the user
age = int(input("Enter your age: "))


if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")



    # Get input from the user
username = input("Enter your username: ")
password = input("Enter your password: ")


if username == "admin" and password == "12345":
    print("Login successful.")
else:
    print("Login failed.")




    # Get input from the user
number = float(input("Enter a number: "))


if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")




    # Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))


max_number = max(num1, num2, num3)

# Print the result
print(f"The maximum of {num1}, {num2}, and {num3} is: {max_number}")




# Get input from the user
score = float(input("Enter the numeric score: "))


if 90 <= score <= 100:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
elif 60 <= score < 70:
    grade = "D"
else:
    grade = "F"


print(f"The grade for the score {score} is: {grade}")




number = int(input("Enter a number: "))


is_prime = True


if number <= 1:
    is_prime = False
else:
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break


if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")



    
year = int(input("Enter a year: "))


if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")




    
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


if num1 > num2:
    print(f"The larger number is: {num1}")
elif num1 < num2:
    print(f"The larger number is: {num2}")
else:
    print("The two numbers are equal.")
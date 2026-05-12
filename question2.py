

a=print("Hello, world!")

print(type(a))

#1. write a program and take the three number and finds the sum of the three number

num1=int(input("Enter the first number :"))
num2=int(input("Enter the second number :"))
num3=int(input("Enter the third number :"))

sum=num1+num2+num3

print("The sum of the three number is=", sum)



#2. write a program for print all prime numbers up to 100 Starts of the prime number will be decide of the users.

start = int(input("Enter starting number: "))

for num in range(start, 101):
    if num > 1:
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num)

# Method 2: while loop
print("Using while loop:")
i = 5
while i <= 50:
    print(i)
    i += 5

# write a program and add two number using function
#1. write a program and take the three number and finds the sum of the three number

def add(num1,num2,num3):
    return num1+num2+num3

num1=int(input("Enter the first number :"))
num2=int(input("Enter the second number :"))
num3=int(input("Enter the third number :"))

sum=add(num1,num2,num3)
sum1=add(num1,num2,num3)


print("The sum of the three number is=", sum)
print("The sum of the three number is=", sum1)

def add(a, b):
    return a + b

def operation(func, x, y):
    return func(x, y)

result = operation(add, 10, 20)

print(result)

table = [5 * i for i in range(1, 11)]

for num in table:
    print(num)

import statistics

def process_data(lst):
    # Matrix conversion
    matrix = []
    for i in range(0, len(lst), 3):
        row = lst[i:i+3]
        while len(row) < 3:
            row.append(None)
        matrix.append(row)
    while len(matrix) < 3:
        matrix.append([None, None, None])

    # Tuple and statistics
    tup = tuple(lst)
    mean = statistics.mean(tup)
    median = statistics.median(tup)

    try:
        mode = statistics.mode(tup)
    except:
        mode = "No unique mode"

    # Dictionary output
    result = {
        "Matrix": matrix,
        "Tuple": tup,
        "Mean": mean,
        "Median": median,
        "Mode": mode
    }

    return result


user_list = list(map(int, input("Enter numbers: ").split()))
print(process_data(user_list))

# Write a program using functions to add two numbers. If the sum of these two numbers is greater than the middle value of a user-provided list, print the set of all numbers in the list located between the start and the middle value. If the sum is equal to the middle value, print a dictionary where the key is the index of the middle value and the value is the middle value itself. If the sum is less than the middle value, print a tuple containing all numbers in the list that appear after the middle value.[1, 2]

def add_numbers(a, b):
    return a + b

def process_list(lst, total):
    middle_index = len(lst) // 2
    middle_value = lst[middle_index]

    if total > middle_value:
        result = set(lst[0:middle_index])   # between start and middle
        print("Set:", result)

    elif total == middle_value:
        result = {middle_index: middle_value}
        print("Dictionary:", result)

    else:
        result = tuple(lst[middle_index + 1:])  # after middle value
        print("Tuple:", result)


# Example list
numbers = [1, 2]

# Input two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum_result = add_numbers(num1, num2)

print("Sum:", sum_result)

process_list(numbers, sum_result)
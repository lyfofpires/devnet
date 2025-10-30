"""
4. Write a Python program to find those numbers which are divisible by 7 and multiples of 5,
between 1500 and 2700 (both included)
"""

# numbers that are divisible by 7 and are multiples of 5

numbers = []
for number in range(1500,2700):
    if number % 7 == 0 and number % 5 == 0 :
        numbers.append(str(number))

print(numbers)

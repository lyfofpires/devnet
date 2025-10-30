"""
1. Write a Python program that calculates the area of a circle,
based on the radius entered by the user.
"""
import math

# area_of_a_circle
r = eval(input("type in your radius: \n"))
area_of_a_circle = 3.14159 * r ** 2print(area_of_a_circle)

"""
2. Write a Python program that accepts the user's first and last name and prints 
them in reverse order with a space between them
"""

# reverse_username
first_name = input("enter your first name: ")
last_name = input("enter your last name: ")

print(last_name + " " + first_name)

"""
3. Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"] 
"""
# color list
color_list = ["Red", "Green", "White", "Black"]

print(color_list[0] +"\n"+ color_list[3])

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

"""
5. Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
Expected Output: 60°C is 140 in Fahrenheit45°F is 7 in Celsius6. 
"""

# temperature
which_one = input("from celsius to fahrenheit, type "C", from fahrenheit to celsius, type "F" : ")

if which_one == "C":
    celsius = float(input(" enter temperature in celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is {fahrenheit}°F in Fahrenheit")

elif which_one == "F":
    fahrenheit = float(input(" enter temperature in fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F is {round(celsius)}°C")

else:
    print("Invalid input. type C or F")


"""
6.Write a Python program to create a class representing a Circle. 
Include methods to calculate its area and perimeter.
"""

# class circle

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14159 * self.radius
"""
5. Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
Expected Output: 60°C is 140 in Fahrenheit45°F is 7 in Celsius6.
"""

# temperature
which_one = input("from celsius to fahrenheit, type C, from fahrenheit to celsius, type F : \n")

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

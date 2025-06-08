FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

temp = float(input("Enter the temperature to convert: "))
temp_scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if temp_scale == "C":
    print(f"{temp}°{temp_scale} is {convert_to_fahrenheit(temp)}°F")
elif temp_scale == "F":
    print(f"{temp}°{temp_scale} is {convert_to_celsius(temp)}°C")
else:
    print("Invalid temperature. Please enter a numeric value and correct temperature scale.")









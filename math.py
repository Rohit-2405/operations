import math

try:
    number = float(input("Enter a number: "))

    if number <= 0:
        print("Natural logarithm is only defined for positive numbers.")
    else:
        sqrt_val = math.sqrt(number)
        log_val = math.log(number)  
        sine_val = math.sin(number)  
        print(f"Square Root: {sqrt_val}")
        print(f"Natural Logarithm: {log_val}")
        print(f"Sine (in radians): {sine_val}")
except ValueError:
    print("Invalid input. Please enter a valid number.")

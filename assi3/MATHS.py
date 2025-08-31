import math


try:
    number = float(input("Enter a number: "))

    if number <= 0:
        print("Logarithm and square root are only defined for positive numbers.")
    else:
       
        square_root = math.sqrt(number)
        natural_log = math.log(number)
        sine_value = math.sin(number)

       
        print(f"\nResults for the number {number}:")
        print(f"Square Root      : {square_root}")
        print(f"Natural Log (ln) : {natural_log}")
        print(f"Sine (radians)   : {sine_value}")
except ValueError:
    print("Invalid input! Please enter a numeric value.")

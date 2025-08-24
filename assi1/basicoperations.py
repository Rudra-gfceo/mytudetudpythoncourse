# Take input from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Perform operations
addition = a+ b
subtraction = a-b 
multiplication =a *b


if a == 0 or b == 0:
    division = "Undefined (division involving zero is not allowed)"
else:
    division =  a / b



# Display the results
print("\nResults")
print(f"Addition: {a} + {b} = {addition}")
print(f"Subtraction: {a} - {b} = {subtraction}")
print(f"Multiplication: {a} * {b} = {multiplication}")
print(f"Division: {a} / {b} = {division}")

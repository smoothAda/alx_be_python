# multiplication_table.py
# Generates a multiplication table for a given number using a for loop

try:
    number = int(input("Enter a number to see its multiplication table: "))

    for i in range(1, 11):
        product = number * i
        print(f"{number} * {i} = {product}")

except ValueError:
    print("Please enter a valid integer.")

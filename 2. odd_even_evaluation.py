def check_even_odd(number):
    # Check if the number is negative
    if number < 0:
        number_type = "Negative"
    else:
        number_type = "Positive"

    # Check if the number is even or odd
    if number % 2 == 0:
        return f"{number_type} Even"
    else:
        return f"{number_type} Odd"


# Example usage:
num = int(input("Enter an integer: "))
result = check_even_odd(num)
print(f"The number {num} is {result}.")

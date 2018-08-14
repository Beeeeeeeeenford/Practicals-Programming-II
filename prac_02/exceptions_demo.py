"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator > 0:
        fraction = numerator / denominator
        print(fraction)
    else:
        print("Cannot divide by zero!")
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

"""
1. When will a ValueError occur?
    When the user inputs anything that is not a whole number.
2. When will a ZeroDivisionError occur?
    When the user inputs the number 0 into the denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    You could check if the denominator is greater than 0 to run the code.
"""
#write a program to find the factorial of a nummber
# Function to calculate the factorial of a number
def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        result = 1
        for i in range(2, number + 1):
            result *= i
        return result

# Input from the user
num = int(input("Enter a number: "))

# Call the function and print the result
fact = factorial(num)
print(f"The factorial of {num} is {fact}.")

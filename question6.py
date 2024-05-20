#write a program to find the maximum of two numbers
# Function to find the maximum of two numbers
def find_max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

# Input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Call the function and print the result
max_num = find_max(num1, num2)
print(f"The maximum of {num1} and {num2} is {max_num}.")

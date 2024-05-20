#write a program to find if the given number is prime no or not
# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True  # 2 is the only even prime number
    if number % 2 == 0:
        return False  # other even numbers are not primes
    # Check for factors from 3 to the square root of the number
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

# Input from the user
num = int(input("Enter a number: "))

# Call the function and print the result
if is_prime(num):
    print(f"The number {num} is a prime number.")
else:
    print(f"The number {num} is not a prime number.")

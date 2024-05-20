# find if the given number is a palindrome or not?
# Function to check if a number is a palindrome
def is_palindrome(number):
    # Convert the number to a string
    num_str = str(number)
   
    if num_str == num_str[::-1]:
        return True
    else:
        return False

num = int(input("Enter a number: "))

if is_palindrome(num):
    print(f"The number {num} is a palindrome.")
else:
    print(f"The number {num} is not a palindrome.")

def is_palindrome(number):

    num_str = str(number)
  
    if num_str == num_str[::-1]:
        return True
    else:
        return False
num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"The number {num} is a palindrome.")
else:
    print(f"The number {num} is not a palindrome.")
def is_palindrome(number):
    num_str = str(number)
    if num_str == num_str[::-1]:
        return True
    else:
        return False
num = int(input("Enter a number: "))

if is_palindrome(num):
    print(f"The number {num} is a palindrome.")
else:
    print(f"The number {num} is not a palindrome.")

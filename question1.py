# write a python code to find if the given number is odd or even?

def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
num = int(input("Enter a number: "))
result = check_odd_even(num)
print(f"The number {num} is {result}.")


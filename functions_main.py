
# DRY - Dont Reapet Yourself

def say_hello(say_to):
    print(f"Hello, {say_to}!")


say_hello("Y.R")
say_hello(say_to="World")
say_hello(say_to="Python")
print("Hello after function")


def calculate(num_1, num_2,):
    print("Getting numbers...")
    result = num_1 + num_2
    print("Calculating result...")
    print(f"{result = }")

calculate(2, 8)
calculate(num_2=100, num_1=200)
def add_numbers(a, b):
    return a + b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("Addition of two numbers")
    x = get_number("Enter first number: ")
    y = get_number("Enter second number: ")
    result = add_numbers(x, y)
    # Print as int when there's no fractional part
    if result.is_integer():
        result = int(result)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()

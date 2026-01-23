# Program to generate first n Fibonacci numbers

n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fibonacci sequence:")
    print(0)
else:
    a = 0
    b = 1

    print("Fibonacci sequence:")

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

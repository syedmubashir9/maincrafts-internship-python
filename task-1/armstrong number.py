# Program to check whether a number is an Armstrong number

num = int(input("Enter a number: "))

temp = num
sum_of_powers = 0
digits = len(str(num))

while temp > 0:
    digit = temp % 10
    sum_of_powers = sum_of_powers + (digit ** digits)
    temp = temp // 10

if sum_of_powers == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is NOT an Armstrong number")

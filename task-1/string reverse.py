# Program to reverse a string

string = input("Enter a string: ")

reversed_string = ""

for ch in string:
    reversed_string = ch + reversed_string

print("Reversed string:", reversed_string)

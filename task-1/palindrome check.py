# Program to check whether a word is a palindrome

word = input("Enter a word: ")

reversed_word = ""

for ch in word:
    reversed_word = ch + reversed_word

if word == reversed_word:
    print("The word is a Palindrome")
else:
    print("The word is NOT a Palindrome")

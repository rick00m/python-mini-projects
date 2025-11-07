# Palidrome checker

original = input("Please enter your word: ").lower()
reversed = original [::-1]
if original == reversed:
    print("Your word is a palindrome")
else:
    print("Your word is not a palindrome")
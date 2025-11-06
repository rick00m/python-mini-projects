# Simple calculator to test arithmetic operator functions

arithm_type = input("""For Multiplication, type [1]
For Division, type [2]
For Addition, type [3]
For Subtraction, type [4]
For Modulus, type [5]
Please enter: """)

if arithm_type == "1":
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    
    num1 = int(num1)
    num2 = int(num2)

    result = num1 * num2
    print(int(result))

if arithm_type == "2":
    num1 = input("Enter the first number: ")
    num2 = input("Enter the divider: ")

    num1 = int(num1)
    num2 = int(num2)

    result = num1 / num2 
    print(int(result))

if arithm_type == "3":
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    num1 = int(num1)
    num2 = int(num2)

    result = num1 + num2 
    print(int(result))

if arithm_type == "4": 
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    num1 = int(num1)
    num2 = int(num2)

    result = num1 - num2
    print(int(result))

if arithm_type == "5":  
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    num1 = int(num1)
    num2 = int(num2)

    result = num1 % num2
    print(int(result))

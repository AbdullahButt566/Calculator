number1 = int(input("Enter First Number: "))
number2 = int(input("Enter Second Number: "))
operation = input("Enter Operation (+ , - , / , * ): ")
if operation == "+":
    print(f"Output: {number1+number2}")
elif operation == "-":
    print(f"Output: {number1-number2}")
elif operation == "*":
    print(f"Output: {number1*number2}")
elif operation == "/":
    print(f"Output: {number1/number2}")
else:
    print("Not a valid operation")

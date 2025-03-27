num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))

operation = input("enter any operation: ")
if (operation == '+'):
    result = num1 + num2
elif (operation == '-'):
    result = num1 - num2
elif (operation == '*'):
    result = num1 * num2
elif (operation == '/'):
    result = num1 / num2
else:
    print("input character is not recognized")   

print(result)

user_numbers = set()
while len(user_numbers) < 7:
    try:
        num = int(input("Enter a number: "))
        if num  in user_numbers:
           print("error: this num already in set")
        else:
            user_numbers.add(num)
       
    except ValueError:
     print("invalid,please enter only numbers")

print("all 7 numbers")

print(user_numbers)

for num in user_numbers:
    print(num)
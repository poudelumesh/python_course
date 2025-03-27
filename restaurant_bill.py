print("please select a menu")
print("Burger: $10 - press 1")
print("Burger: $12 - press 2")
print("Burger: $15 - press 3")

choice = input("please enter the menu number")

number_guest = int(input("please enter the number of guest: "))

if choice == "1":
    total_price = number_guest * 10
elif choice == "2":
    total_price = number_guest * 12
elif choice == "3":
    total_price = number_guest * 15

print(f"the total without discount is ${total_price}")       

if total_price >= 200:
    total_with_discount = total_price - total_price * 0.2
    print(f"the total with discount is ${total_with_discount}")  

elif  total_price >= 100:
    total_with_discount = total_price - total_price * 0.1
    print(f"the total with discount is ${total_with_discount}")  
   
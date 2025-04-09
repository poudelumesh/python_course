products = [{"name": "one plus","price": 300},
             {"name": "laptop", "price": 500},
             {"name": "headphone", "price": 50},
              {"name": "keyboard", "price": 40},]

careers = [{"name": "uber", "price": 15},
                     {"name": "pathao", "price": 10},
                     {"name": "foodmandu", "price": 8},
                     {"name": "indrive", "price": 7},]

for index, product in enumerate(products):
    print(f"for {product["name"]} - ${product["price]} press {index}")

while True:
    user_product_index = int(input("please enter the product number: ")) 
    try:
        user_product_index = int("user_product_index")
        if user_product_index >= 0 and user_product_index < len(products):
         break  
        else:
           print("This product does not exit")
    except ValueError:
        print("please enter only number")

user_product = products[user_product_index]


for index, career in enumerate(careers):
    print(f"for {career["name"]}press {index}")

while True:
    user_career_index = int(input("please enter the career number: ")) 
    try:
        user_career_index = int("user_career_index")
        if user_career_index >= 0 and user_career_index < len(careers):
         break  
        else:
           print("This career does not exit")
    except ValueError:
        print("please enter only number")
             
user_career = careers[user_career_index]
print(f"you choose {user_product["name"]} - ${user_product["price"]}")
print(f"you choose {user_career["name"]} - ${user_career["price"]}")
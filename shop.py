products = [{"name": "one plus","price": 300},
             {"name": "laptop", "price": 500},
             {"name": "headphone", "price": 50},
              {"name": "keyboard", "price": 40},]

delivery_company = [{"name": "uber", "price": 15},
                     {"name": "pathao", "price": 10},
                     {"name": "foodmandu", "price": 8},
                     {"name": "indrive", "price": 7},]

for index, product in enumerate(products):
    print(f"for {product["name"]}press {index}")

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
user_product = product[user_product_index]

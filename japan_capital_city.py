
answer = "Tokyo"
attempts = 0
max_attempts = 5

while True:
    user_answer = input("What is the capital of Japan?: ")
    attempts += 1  

    if user_answer == answer:  
        print("Correct answer.")
        break  

    if attempts == max_attempts:  
        print("Sorry, the correct answer is Tokyo.")  
        break  

    print(f"Incorrect. Attempts: {attempts}/{max_attempts}")
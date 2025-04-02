correct_password = "ABCD"
max_attempt = 3
attempt = 0
input_password = ""

while attempt < max_attempt and input_password != correct_password:
    input_password = input("Enter your password:\n")
    if input_password == correct_password:
        print("Access granted")
else:
    attempt += 1
    print("incorrect password. Number of attempt {attempt}/{max_attempt}")
    if attempt == max_attempt:
        print("too many attempts. your account is blocked")        



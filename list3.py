marks = []

while True:
    user_mark = input("Enter your mark(or press Enter to finish): ")
    if user_mark == "":
        break
    else:
        marks.append(int(user_mark))

if marks:
    total = sum(marks)
    average = sum(marks)/len(marks)
    print(f"total marks: {total}")
    print(f"average marks: {average}")

else:
    print("wrong calculation")


    

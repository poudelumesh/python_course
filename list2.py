games = []
while True:
    game = input("Enter your favorite game: ")
    if game == "":
        break
    else:
        games.append(game)

print("your favorite games: ")   
for game in games:
    print(game) 
games = [
    {"name": "free fire",
    "editor": "umesh",
    "year": 2017 }
]
new_game = {
    "name": input("Enter the name: "),
    "editor": input("Enter the editor name: "),
    "year": input("Enter the established year: ")
}

games.append(new_game)

for game in games:
    print("game :" ,game["name"])
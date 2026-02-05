players = {"Virat", "Rohit", "Dhoni", "Jadeja", "Sai"}
playersList = list(players)

i = 0
while i < len(playersList):
    j = i + 1
    while j < len(playersList):
        print({playersList[i], playersList[j]})
        j += 1
    i += 1


# {"Virat", "Sai"}
# {"Virat", "Jadeja"}
# {"Virat", "Dhoni"}
# {"Virat", "Rohit"}
# {"Sai", "Jadeja"}
# {"Sai", "Dhoni"}
# {"Rohit", "Sai"}
# {"Jadeja", "Dhoni"}
# {"Rohit", "Jadeja"}
# {"Rohit", "Dhoni"}

print()
print()

### way-2
players = {"Virat", "Rohit", "Dhoni", "Jadeja", "Sai"}
i = 0
for player1 in players:
    i += 1
    for player2 in list(players)[i::]:
        print({player1, player2})

# Homework 3 - Board Game System
# Name:Tori Gregory
# Date:4/4/26


def loadGameData(filename):
    """Reads game data from a file and returns it as a list."""
    data = []
    with open(filename, "r") as file:
        for line in file:
            data.append(line.strip())
    return data


def displayGame(data):
    """Displays the current game state."""
    print("\nCurrent Game State:")
    for item in data:
        print(item)
def changeturn(data, turn):
    if data[0] == "0: Player 1":
        data[0] = "0: Player 2"
    elif data[0] == "0: Player 2":
        data[0] = "0: Player 1"
    else:
        print("change turn failed")

def movePlayer(data):
    """Example function to simulate moving a player."""
    import random
    dice = random.randint(1,6)
    print("You rolled " + str(dice))
    if dice in (1, 5):
        if data[0] == "0: Player 1":
            data[1] = "1: Player 1"
        else:
            data[1] = "1: Player 2"
    elif dice in (2, 6):
        if data[0] == "0:Player 1":
            data[2] = "2: Player 1"
        else:
            data[2] = "2: Player 2"
    elif dice == 3:
        if data[0] == "0: Player 1":
            data[3] = "3: Player 1"
        else:
            data[3] = "3: Player 2"
    elif dice == 4:
        if data[0] == "0: Player 1":
            data[4] = "4: Player 1"
        else:
            data[4] = "4: Player 2"
def decideWin(data):
    if data[4] == "4: Player 1":
        print("Player 1 Wins!")
    elif data[4] == "4: Player 2":
        print("Player 2 Wins!")
def main():
    filename = "events.txt"   # Students can rename if needed

    gameData = loadGameData(filename)
    displayGame(gameData)

    # Example interaction
    turn = 1
    while turn <= 6:
        continueplay = input("do you want to roll the dice? (y/n)" )
        if continueplay == "y":
            movePlayer(gameData)
            displayGame(gameData)
            print("Current turn is " + str(turn) + " out of 6")
            changeturn(gameData, turn)
            turn = turn + 1
        else:
            break
    decideWin(gameData)
    print(gameData)

if __name__ == "__main__":
    main()

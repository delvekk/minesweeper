import random
import sys


def get_number_of_mines():
    while True:
        print("Witaj w grze Saper")
        number = int(input("Ile min ma znajdować się na planszy?\n"))
        if number > 0 and number < 81:
            print("Na planszy będzie znajdować się {} min".format(number))
            break
        else:
            print("Zła liczba, sprobuj jeszcze raz")
    return number


def deploy_mines(numberOfMines):
    minesTab = []
    for z in range(0, numberOfMines):
        while True:
            x = random.randint(1, 9)
            y = random.randint(1, 9)
            xy = str(x) + "." + str(y)
            if xy in minesTab:
                continue
            else:
                minesTab.append(xy)
                break
    return minesTab


def number_of_neighboring_mines(coordinate, minesTab):
    coordinateString = str(coordinate)
    xInt = int(coordinateString[0])
    yInt = int(coordinateString[2])
    if coordinateString in minesTab:
        return 9
    else:
        if xInt == 1:
            if yInt == 1:
                possibleMines = ["1.2", "2.1", "2.2"]
            elif yInt == 9:
                possibleMines = ["1.8", "2.8", "2.9"]
            else:
                possibleMines = [str(round(coordinate - 0.1, 1)), str(round(coordinate + 0.1, 1)),
                                 str(round(coordinate + 1.0, 1)),
                                 str(round(coordinate + 0.9, 1)), str(round(coordinate + 1.1, 1))]
        elif xInt == 9:
            if yInt == 1:
                possibleMines = ["8.1", "8.2", "9.2"]
            elif yInt == 9:
                possibleMines = ["9.8", "8.8", "8.9"]
            else:
                possibleMines = [str(round(coordinate - 0.1, 1)), str(round(coordinate + 0.1, 1)),
                                 str(round(coordinate - 1.0, 1)),
                                 str(round(coordinate - 0.9, 1)), str(round(coordinate - 1.1, 1))]
        else:
            if yInt == 1:
                possibleMines = [str(round(coordinate + 0.1, 1)), str(round(coordinate + 1.0, 1)),
                                 str(round(coordinate - 0.9, 1)), str(round(coordinate + 1.1, 1)),
                                 str(round(coordinate - 1.0, 1))]
            elif yInt == 9:
                possibleMines = [str(round(coordinate - 0.1, 1)), str(round(coordinate + 1.0, 1)),
                                 str(round(coordinate + 0.9, 1)), str(round(coordinate - 1.1, 1)),
                                 str(round(coordinate - 1.0, 1))]
            else:
                possibleMines = [str(round(coordinate - 0.1, 1)), str(round(coordinate + 0.1, 1)),
                                 str(round(coordinate + 1.0, 1)), str(round(coordinate - 1.0, 1)),
                                 str(round(coordinate - 0.9, 1)), str(round(coordinate + 0.9, 1)),
                                 str(round(coordinate + 1.1, 1)), str(round(coordinate - 1.1, 1))]

    count = 0
    for a in possibleMines:
        if a in minesTab:
            count += 1
    return count


def create_board(minesTab):
    board = []
    for x in range(1, 10):
        new = []
        for y in range(1, 10):
            new.append(number_of_neighboring_mines(float(str(x) + "." + str(y)), minesTab))
        board.append(new)
    return board


def reveal_squears(coordinate, startBoard, currentBoard, alreadyChecked):
    coordinateString = str(coordinate)
    if coordinateString in alreadyChecked:
        return
    x = int(coordinateString[0])
    y = int(coordinateString[2])
    number = startBoard[x - 1][y - 1]
    if number == 9:
        currentBoard[x - 1][y - 1] = str(9)
        return 9
    else:
        alreadyChecked.append(str(x) + "." + str(y))
        if number == 0:
            currentBoard[x - 1][y - 1] = '.'
            if x == 1:
                if y == 1:
                    reveal_squears(round(coordinate + 0.1, 1), startBoard, currentBoard, alreadyChecked)
                    reveal_squears(round(coordinate + 1.0, 1), startBoard, currentBoard, alreadyChecked)
                    reveal_squears(round(coordinate + 1.1, 1), startBoard, currentBoard, alreadyChecked)
                elif y == 9:
                    reveal_squears(round(coordinate - 0.1, 1), startBoard, currentBoard, alreadyChecked)
                    reveal_squears(round(coordinate + 1.0, 1), startBoard, currentBoard, alreadyChecked)
                    reveal_squears(round(coordinate + 0.9, 1), startBoard, currentBoard, alreadyChecked)
                else:
                    reveal_squears(round(coordinate - 0.1, 1), startBoard, currentBoard, alreadyChecked)
                    reveal_squears(round(coordinate + 0.1, 1), startBoard, currentBoard, alreadyChecked)
                    reveal_squears(round(coordinate + 0.9, 1), startBoard, currentBoard, alreadyChecked)
                    reveal_squears(round(coordinate + 1.0, 1), startBoard, currentBoard, alreadyChecked)
                    reveal_squears(round(coordinate + 1.1, 1), startBoard, currentBoard, alreadyChecked)
            elif x == 9:
                if y == 1:
                    reveal_squears(round(coordinate + 0.1, 1), startBoard, currentBoard, alreadyChecked)
                    reveal_squears(round(coordinate - 1.0, 1), startBoard, currentBoard, alreadyChecked)
                    reveal_squears(round(coordinate - 0.9, 1), startBoard, currentBoard, alreadyChecked)
                elif y == 9:
                    reveal_squears(round(coordinate - 0.1, 1), startBoard, currentBoard, alreadyChecked)
                    reveal_squears(round(coordinate - 1.0, 1), startBoard, currentBoard, alreadyChecked)
                    reveal_squears(round(coordinate - 1.1, 1), startBoard, currentBoard, alreadyChecked)
                else:
                    reveal_squears(round(coordinate - 0.1, 1), startBoard, currentBoard, alreadyChecked)
                    reveal_squears(round(coordinate + 0.1, 1), startBoard, currentBoard, alreadyChecked)
                    reveal_squears(round(coordinate - 1.0, 1), startBoard, currentBoard, alreadyChecked)
                    reveal_squears(round(coordinate - 1.1, 1), startBoard, currentBoard, alreadyChecked)
                    reveal_squears(round(coordinate - 0.9, 1), startBoard, currentBoard, alreadyChecked)
            else:
                if y == 1:
                    reveal_squears(round(coordinate + 0.1, 1), startBoard, currentBoard, alreadyChecked)
                    reveal_squears(round(coordinate - 1.0, 1), startBoard, currentBoard, alreadyChecked)
                    reveal_squears(round(coordinate + 1.0, 1), startBoard, currentBoard, alreadyChecked)
                    reveal_squears(round(coordinate + 1.1, 1), startBoard, currentBoard, alreadyChecked)
                    reveal_squears(round(coordinate - 0.9, 1), startBoard, currentBoard, alreadyChecked)
                elif y == 9:
                    reveal_squears(round(coordinate - 0.1, 1), startBoard, currentBoard, alreadyChecked)
                    reveal_squears(round(coordinate - 1.0, 1), startBoard, currentBoard, alreadyChecked)
                    reveal_squears(round(coordinate + 1.0, 1), startBoard, currentBoard, alreadyChecked)
                    reveal_squears(round(coordinate - 1.1, 1), startBoard, currentBoard, alreadyChecked)
                    reveal_squears(round(coordinate + 0.9, 1), startBoard, currentBoard, alreadyChecked)
                else:
                    reveal_squears(round(coordinate - 0.1, 1), startBoard, currentBoard, alreadyChecked)
                    reveal_squears(round(coordinate + 0.1, 1), startBoard, currentBoard, alreadyChecked)
                    reveal_squears(round(coordinate - 1.0, 1), startBoard, currentBoard, alreadyChecked)
                    reveal_squears(round(coordinate + 1.0, 1), startBoard, currentBoard, alreadyChecked)
                    reveal_squears(round(coordinate - 1.1, 1), startBoard, currentBoard, alreadyChecked)
                    reveal_squears(round(coordinate + 1.1, 1), startBoard, currentBoard, alreadyChecked)
                    reveal_squears(round(coordinate + 0.9, 1), startBoard, currentBoard, alreadyChecked)
                    reveal_squears(round(coordinate - 0.9, 1), startBoard, currentBoard, alreadyChecked)
        elif number > 0 and number < 9:
            currentBoard[x - 1][y - 1] = str(startBoard[x - 1][y - 1])
            return number


def print_board(actualGrid):
    count = 0
    for x in range(1, 10):
        print("  " + str(x) + " ", end='')
    print("\n", end='')
    for y in range(0, 9):
        for x in range(0, 9):
            print(chr(9556) + chr(9552) + chr(9552) + chr(9559), end='')
        print("\n", end='')
        for x in range(0, 9):
            print(chr(9553) + " " + str(actualGrid[y][x]) + chr(9553), end='')
        print(str(count + 1) + "\n", end='')
        for x in range(0, 9):
            print(chr(9562) + chr(9552) + chr(9552) + chr(9565), end='')
        print("\n", end='')
        count += 1


def sapper():
    mines = get_number_of_mines()
    positionOfMines = deploy_mines(mines)
    startBoard = create_board(positionOfMines)
    alreadyChecked = []
    currentBoard = []
    for x in range(1, 10):
        new = []
        for y in range(1, 10):
            new.append(" ")
        currentBoard.append(new)
    print_board(currentBoard)
    while True:
        count = 0
        coord = round(float(input("Wybierz pole ")), 1)
        number = reveal_squears(coord, startBoard, currentBoard, alreadyChecked)
        print_board(currentBoard)
        if number == 9:
            print("PRZEGRAŁES")
            return
        for x in range(0, 9):
            for y in range(0, 9):
                if currentBoard[x][y] == " ":
                    count += 1
        if count == mines:
            print("WYGRAŁES")
            return


while True:
    sapper()
    while True:
        answer = input("Chcesz zagrać jeszcze raz?(Tak/Nie) ")
        if answer.lower() == "nie" or answer.lower() == "tak":
            break
        else:
            print("Podaj poprawną odpowiedź(Tak/Nie) ")
    if answer.lower() == "nie":
        sys.exit(0)

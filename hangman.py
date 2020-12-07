import random

with open('sowpods.txt') as f:
    words = list(f)

word = random.choice(words).strip()
wordList = list(word)
boardList = ["_ " for i in wordList]
wrongList = []

while True:
    lives = 6 - len(wrongList)
    board = "".join(boardList)
    print("")
    if lives == 6:
        print(" -------\n"
        "|                  ", board, "\n"
        "|\n"
        "|                  ", "incorrect letters:", wrongList, "\n")

    if lives == 5:
        print(" -------\n"
        "|   O              ", board, "\n"
        "|\n"
        "|                  ", "incorrect letters:", wrongList, "\n")

    if lives == 4:
        print(" -------\n"
        "|   O              ", board, "\n"
        "|  / \n"
        "|                  ", "incorrect letters:", wrongList, "\n")

    if lives == 3:
        print(" -------\n"
        "|   O              ", board, "\n"
        "|  /|\n"
        "|                  ", "incorrect letters:", wrongList, "\n")

    if lives == 2:
        print(" -------\n"
        "|   O              ", board, "\n"
        "|  /|\ \n"
        "|                  ", "incorrect letters:", wrongList, "\n")

    if lives == 1:
        print(" -------\n"
        "|   O              ", board, "\n"
        "|  /|\ \n"
        "|  /               ", "incorrect letters:", wrongList, "\n")

    if lives == 0:
        print(" -------\n"
        "|   O              ", board, "\n"
        "|  /|\ \n"
        "|  / \             ", "incorrect letters:", wrongList, "\n")
        print("u lose! the word was:", word)
        break

    # win condition
    if "_ " not in boardList:
        print("u win!")
        break

    guess = input("guess your letter: ").upper()

    # check if single letter and if already guessed
    if guess.isalpha() and len(guess) == 1:
        if guess in wrongList or (guess + " ") in boardList:
            print("u already guessed {}. enter another letter".format(guess))
            continue
    else:
        print("invalid input. please enter a single letter.")
        continue

    pos = -1
    for i in wordList:
        pos += 1
        if guess == i:
            boardList[pos] = i + " "

    if guess not in wordList:
        wrongList.append(guess)

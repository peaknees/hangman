import random

with open('sowpods.txt') as f:
    words = list(f)

word = random.choice(words).strip()
wordList = list(word)
boardList = ["_" for i in wordList]
wrongList = []

#create list of possible words based of length of given word
posWords = [i.strip() for i in words if len(i.strip()) == len(word)]
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#function to find letter with highest probability
def maxLetter():
    d = {}
    total = len(posWords)
    #print("total:", len(posWords))
    for letter in alphabets:
        count = 0
        for i in posWords:
            wordLetters = set(i)
            if letter in wordLetters:
                count += 1
        if count == total:
            maxletter = letter
            return maxletter
        if count > 0:
            #print(letter, count)
            d[letter] = count/total
    maxletter = max(d, key=d.get)
    return maxletter

#function to remove word based on letter position and letters that are not in word
def wordRemover():
    pos = -1
    for i in wordList:
        pos += 1
        for word in posWords:
            if list(word)[pos] != i:
                posWords.remove(word)

    if guess not in wordList:
        for word in posWords:
            if guess in set(word):
                posWords.remove(word)

while True:
    lives = 6 - len(wrongList)
    board = " ".join(boardList)
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
    if "_" not in boardList:
        print("u win!")
        break

    guess = input("guess your letter: ").upper()
    if len(guess) < 1:
        guess = maxLetter()
        print("the best letter to guess is:", guess)

    # check if single letter and if already guessed
    if guess.isalpha() and len(guess) == 1:
        if guess in wrongList or guess in boardList:
            print("u already guessed {}. enter another letter".format(guess))
            continue
    else:
        print("invalid input. please enter a single letter.")
        continue

    alphabets.remove(guess)
    pos = -1
    for i in wordList:
        pos += 1
        if guess == i:
            boardList[pos] = i

    if guess not in wordList:
        wrongList.append(guess)

    wordRemover()

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

#function to find optimal letter to guess via binary search, guesses letter if 100% inside
def binLetter():
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
            binletter = letter
            return binletter
        if count > 0:
            #print(letter, count)
            d[letter] = count/total
#function to find dict value closest to 0.5, returns key corresponding to value
    a_list = d.values()
    absolute_difference_function = lambda list_value : abs(list_value - 0.5)
    closest_value = min(a_list, key=absolute_difference_function)
    binletter = list(d.keys())[list(d.values()).index(closest_value)]
    return binletter

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
    board = " ".join(boardList)
    print("")
    print(board)
    print("incorrect letters:", wrongList)

    # win condition
    if "_" not in boardList:
        print("u win!")
        print("wrong guesses:", len(wrongList))
        break

    guess = binLetter()
    alphabets.remove(guess)
    print("guess your letter:", guess)

    pos = -1
    for i in wordList:
        pos += 1
        if guess == i:
            boardList[pos] = i

    if guess not in wordList:
        wrongList.append(guess)

    wordRemover()

'''
optimizations to code:
1. use regex to filter words faster??
2. select based on highest probablility over closest to binary?
'''

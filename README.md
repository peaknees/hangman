# hangman
simple hangman game

words from the SOWPODS dictionary: http://norvig.com/ngrams/sowpods.txt

# hangman 2.0
simple hangman game -- now with a built in solver
solver uses the following algorithm:
1. considers all possible words based on given information -- length of word, position of correct letters guessed, incorrect letters guessed
2. considers all possible letters to guess, calculates percentage of words with each letter
3. guesses letter that has closest to 50% of words (binary search)

solver was with inspiration from jan Misali's video: https://www.youtube.com/watch?v=le5uGqHKll8&ab_channel=janMisali

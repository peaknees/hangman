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

# hangman 3.0
i think that binary search isnt the optimal solution... 
now the algorithm guesses letter that has the highest percentage of words containing that letter.
ill be running it a while to collect some data to find out which version is better!

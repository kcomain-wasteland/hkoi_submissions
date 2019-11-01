'''Hangman(D304)
Hangman is a word guessing game. The game is played using a hidden English word H. 
Initially all its letters are hidden, but the player will know its length 
(the number of letters in the word). 
Next, the player will guess letters one by one. 
If H contains the letter guessed, the letter and the position(s) will be revealed.
For example, if H = abacus and the player guesses a, a_a___ will be shown to the player. 
The player will make guesses repeatedly until the all letters in H are revealed.
'''
import re

h = input()
solved = False

progress = ""
sepword = [a for a in h]
for i in sepword:
    progress += '_'
    print(progress)
while not solved:
    print()


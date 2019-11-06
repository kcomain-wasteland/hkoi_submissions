'''Hangman(D304)
Hangman is a word guessing game. The game is played using a hidden English word H. 
Initially all its letters are hidden, but the player will know its length 
(the number of letters in the word). 
Next, the player will guess letters one by one. 
If H contains the letter guessed, the letter and the position(s) will be revealed.
For example, if H = abacus and the player guesses a, a_a___ will be shown to the player. 
The player will make guesses repeatedly until the all letters in H are revealed.

L
'''
import re
word = input()
solvdict={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
current = ""
unsolved = []
solved = []
status = False

for i in [c for c in word]:
	if solvdict[i] == 0:
		solvdict[i] = 1

for i in solvdict:
	if solvdict[i] == 1:
		unsolved.append(i)


while status == False:
	current = word
	for i in unsolved:
		current = re.sub(i,'_',current)
	print(current)
	temp = input()
	for i in unsolved:
		if i == temp:
			unsolved.remove(temp)
	if len(unsolved) == 0:
		status = True
print(word)

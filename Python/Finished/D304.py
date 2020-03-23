#!/usr/bin/python3.5
# Hangman (D304)

# import re
# word = input()
# solvdict={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
# current = ""
# unsolved = []
# solved = []
# status = False
#
# for i in [c for c in word]:
# 	if solvdict[i] == 0:
# 		solvdict[i] = 1
#
# for i in solvdict:
# 	if solvdict[i] == 1:
# 		unsolved.append(i)
#
# while status == False:
# 	current = word
# 	for i in unsolved:
# 		current = re.sub(i,'_',current)
# 	print(current)
# 	temp = input()
# 	for i in unsolved:
# 		if i == temp:
# 			unsolved.remove(temp)
# 	if len(unsolved) == 0:
# 		status = True
# print(word)
#

#!/usr/bin/python3.5

# Setup variables 
chars = []
solved = []

# Get the word
word = input()

# Step 2
for i in [i for i in word]:
	if i not in chars:
		chars.append(i)

# print(f'Chars: {chars}')
# print(f'Solved: {solved}')
while len(chars) != 0:
#    print(f'Chars: {chars}')
#    print(f'Solved: {solved}')
    ch = input()
    if ch in chars:
        solved.append(ch)
        chars.remove(ch)
    out = word
    for i in chars:
        out = out.replace(i, '_')
#       print(f'replaced {i} with _')
    print(out)

"""
Steps:
1. get the word
2. split and search for characters, add them to chars
3. ask chars and add it to solved
4. if the chars is in [chars], delete it.
"""

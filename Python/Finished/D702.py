# No shebang

# Stack (D702)

stack = []
count = int(input())

for i in range(count):
	action = input()
	cmd = action.split(' ')
	if cmd[0] == "PUSH":
		stack.insert(0, int(cmd[1]))
	elif cmd[0] == "TOP":
		if len(stack) == 0:
			print("Empty")
		else:
			print(stack[0])
	elif cmd[0] == "POP":
		if len(stack) == 0:
			print("Cannot pop")
		else:
			stack.remove(stack[0])
	elif cmd[0] == "SIZE":
		print(len(stack))

# Modify the previous program such that 
# only the users Alice and Bob are greeted with their names.

name = raw_input("What is your name?\n")
if (name == "Alice" or name == "Bob"):
	print("Nice to meet you, " + name + "!")
else:
	print("Sorry, you're not allowed here.")
	
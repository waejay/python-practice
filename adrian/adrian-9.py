# Write a guessing game where the user has to guess a 
# secret number. After every guess the program tells the
# user whether their number was too large or too small. 
# At the end the number of tries needed should be printed.
# It counts only as one try if they input the same number 
# multiple times consecutively.

number_of_tries = 0
secret_number = 5
guess = 0


while True:
	previous_guess = guess
	guess = int(input("Enter a number to guess: "))

	if (guess == secret_number):
		print("Good job! Number of tries: " + str(number_of_tries))
		break
	else:
		if (previous_guess != guess):
			number_of_tries = number_of_tries + 1
		if (guess < secret_number):
			print("Your guess is too small!")
		else:
			print("Your guess is too big!")



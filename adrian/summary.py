# Print hello world

print("hello world")# Get user's name and output

# raw-input = strings
# input = integers
#--------------------
name = raw_input("What is your name?\n")
print("Nice to meet you, " + name + "!")
# Modify the previous program such that 
# only the users Alice and Bob are greeted with their names.

name = raw_input("What is your name?\n")
if (name == "Alice" or name == "Bob"):
	print("Nice to meet you, " + name + "!")
else:
	print("Sorry, you're not allowed here.")
	# Write a program that asks the user for a number n and
# prints the sum of the numbers 1 to n.

n = input("Enter a number: ")
sum = 0
for i in range(0, n + 1):
	sum = sum + i
	print sum

print("Sum of numbers 1 through " + str(n) + " is: " + str(sum))# Modify the previous program such that only 
# multiples of three or five are considered in 
# the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17

n = input("Enter a number: ")

sum = 0
for i in range(0, n + 1):
	if (i % 3 == 0 or i % 5 == 0):
		sum = sum + i

print("Sum of 1 through " + str(n) + " including only multiples of 3 and 5 is: " + str(sum))# Write a program that asks the user for a number n
# and gives them the possibility to choose between 
# computing the sum and computing the product of 1..n.

n = input("Enter a number: ")
user_input = raw_input("Enter S for sum, P for product: ")

if (user_input == 'S'):
	sum = 0
	for i in range (0, n + 1):
		sum = sum + i

	print(sum)

if (user_input == 'P'):
	product = 1
	for i in range(1, n + 1):
		product = product * i

	print(product)

# Write a program that prints a multiplication table
# for numbers up to 12.

for i in range(1, 12):
	for j in range(1,12):
			print(j*i, end=" ")
	print()
# Write a program that prints all prime numbers. 
# (Note: if your programming language does not support 
# arbitrary size numbers, printing all primes up to
# the largest number you can easily represent is fine too.)

"""
cases:
	- number % 1 == 0
	- number % number == 0
	- number % anything_else != 0
"""

isPrime = True

for num in range(1, 400):
	for i in range(2, num):
		if (num % i == 0):
			isPrime = False

	if(isPrime):
		print(num)

	isPrime = True
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


# Write a program that prints the next 20 leap years.

# current year = 2018
# next leap year = 2020

leap_year = 2020

for i in range(0, 20):
	print(leap_year)
	leap_year = leap_year + 4
	
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

# Write a program that asks the user for a number n
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


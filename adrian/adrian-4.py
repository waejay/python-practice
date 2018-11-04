# Write a program that asks the user for a number n and
# prints the sum of the numbers 1 to n.

n = input("Enter a number: ")
sum = 0
for i in range(0, n + 1):
	sum = sum + i
	print sum

print("Sum of numbers 1 through " + str(n) + " is: " + str(sum))
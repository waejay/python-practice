# Write three functions that compute the sum of the numbers
# in a list:
# using a for loop
# using a while loop#
# and recursion

numbers = [1,2,3,4,5]			# total sum = 15
print("Expected sum: 15")

""" for loop"""
sum = 0
for number in numbers:
	sum += number

print("Sum using for loop: " + str(sum))

""" while loop """
sum = 0
i = 0
while (True):
	if (i == len(numbers)):
		break
	sum += numbers[i]
	i += 1

print("Sum using while loop: " + str(sum))

""" recursively """



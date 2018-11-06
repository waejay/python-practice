# Write a function that computes the sum total of
# a list

def getTotalSum(list):

	sum = 0
	for x in list:
		sum += x

	return sum

numbers = [1,2,3,4,5, 10]

print("Expected total sum of numbers: 25")
print("Actual total sum of numbers: " + str(getTotalSum(numbers)))
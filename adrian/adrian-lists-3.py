# Write a function that checks whether an element occurs
# in a list


def isInList(element, list):

	# True if element is in list, else False
	return (element in list)


numbers = [1,2,3,4,5]

while (True):
	# Get number from user input
	number = int(input("Enter number to check: "))

	# End loop if input is -1
	if (number == -1):
		break

	# Keep checking if input is in list
	print(isInList(number, numbers))
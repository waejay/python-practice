# Write a function that returns the elements on odd
# positions in a list

def getOddElements(elements, newList):
	i = 1
	for element in elements:
		# if element is odd based on 'i'
		if (i % 2 != 0):
			# append to new list
			newList.append(element)

		i += 1

numbers = [1,2,3,4,5,6,7,8,9]
odd_numbers = []

print("Before:")
print(numbers)
print(odd_numbers)
print()

getOddElements(numbers, odd_numbers)

print("After:")
print(numbers)
print(odd_numbers)



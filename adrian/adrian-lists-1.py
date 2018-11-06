# Write a function taht returns the largest element (integer)
# in a list

numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)

largest_num = numbers[0]
for number in numbers:
	if (number > largest_num):
		largest_num = number

print("largest number is: " + str(largest_num))

# same thing except with large number added in middle

numbers = [1,2,3,4,1234,5,6,7,8,9,10]
print(numbers)

largest_num = numbers[0]
for number in numbers:
	if (number > largest_num):
		largest_num = number

print("largest number is: " + str(largest_num))



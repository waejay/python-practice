def on_all(function, list):
	for element in list:
		function(element)

def square(num):
	num = num ** 2
	return num

numbers = [1,2,3,4,5]

on_all(square, numbers)

print(numbers)





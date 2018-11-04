# Modify the previous program such that only 
# multiples of three or five are considered in 
# the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17

n = input("Enter a number: ")

sum = 0
for i in range(0, n + 1):
	if (i % 3 == 0 or i % 5 == 0):
		sum = sum + i

print("Sum of 1 through " + str(n) + " including only multiples of 3 and 5 is: " + str(sum))
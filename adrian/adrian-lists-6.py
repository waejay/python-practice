# Write a function that tests whether a string is a
# palindrome

def isPalindrome(word):
	start = 0
	end = len(word) - 1

	for i in range(0, len(word)):
		if (word[start] != word[end]):
			return False
		start += 1
		end -= 1

	return True

palindrome = "racecar"

print("Expected boolean value for racecar: True")
print("Actual: " + str(isPalindrome(palindrome)))

palindrome = "doggo"

print("Expected boolean value for doggo: False")
print("Actual: " + str(isPalindrome(palindrome)))

palindrome = "doggod"

print("Expected boolean value for doggod: True")
print("Actual: " + str(isPalindrome(palindrome)))

palindrome = "1234554321"

print("Expected boolean value for 1234554321: True")
print("Actual: " + str(isPalindrome(palindrome)))
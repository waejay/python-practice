# list of strings

names = ["john", "tyler", "tony"]

for name in names:
	print(name, end=" ")
print()						# ?? is there a default way for newline?

print(names[0])
print(names[1])
print(names[2])
print(names[-1])			# get last element

# adding to list

names = ["emily", "michelle", "mai"]
print(names)

names[1] = "lillian"
print(names)

names.append("mom")
print("after appending mom: " + str(names))

names.insert(0, "start")
print("after inserting at beginning: " + str(names))

names.insert(3, "lilmai")
print("after inserting btwn lil and mai: " + str(names))

# removing elemenets (del=position | .remove=value)
del names[0]
print("after deleting initial index: " + str(names))

names.remove("lilmai")
print("after removing lilmai: " + str(names))

print("------------------------")

print(numbers)
end = numbers.pop()

print("last element was: " + str(end))
print(numbers)

numbers.append(end)				# re-append the pop'd number
print(numbers)

print("Length of current list is: " + str(len(numbers)))

# .sort() vs sorted()

currentList = numbers

print(currentList)
print(sorted(numbers))
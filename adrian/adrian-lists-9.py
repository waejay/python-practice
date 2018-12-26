# Write a function that concatenates two lists.
#  [a,b,c], [1,2,3] → [a,b,c,1,2,3]


list1 = ['a','b','c']
list2 = [1,2,3]


### Create new list from the two arguments
def combineTwoLists(list1, list2):

	newList = []

	for element in list1:
		newList.append(element)

	for element in list2:
		newList.append(element)		

	return newList


'''
def appendTo(list1, list2):
	for element in list2:
		list1.append(element)		

	return list1
'''

combinedList = combineTwoLists(list1, list2)

print(list1)
print(list2)
print(combinedList)

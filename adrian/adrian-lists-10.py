# Write a function that combines two lists by 
# alternatingly taking elements, e.g. [a,b,c], 
# [1,2,3] → [a,1,b,2,c,3].


list1 = ['a','b','c']
list2 = [1,2,3]

def combine_alternative(list1, list2):
	newList = []

	for i in range(0, len(list1)):
		newList.append(list1[i])
		newList.append(list2[i])

	return newList


combinedAlternativeList = combine_alternative(list1, list2)

print(list1)
print(list2)
print(combinedAlternativeList)
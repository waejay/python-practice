# strings
name = "john nguyen"

if ("john" in name):
	print("john is in " + name)

print("----------------")

# s1 + s2 | concatenation
title = "sir"

print(title + " " + name)

# len() | length of string
print("length of previous string including spaces"
	+ " is : " + str(len(title + " " + name)))

alphabet = "abcdwxyz"
print(min(alphabet))
print(max(alphabet))

print("----------------")

# s2 not in s | if string isn't in string
hero = "all might"
if ("deku" not in hero):
	print("1) The hero is not deku")

hero = "deku"
if ("deku" not in hero):
	print("2) the hero is not deku")

# same thing except defaulting strings to lowercase
hero = "All Might"
if ("all might" not in hero):
	print("a) Hero is not all might")

# default string being compared to lowercase
if ("all might" in hero.lower()):
	print("b) Hero is all might")

print("----------------")

name = "john nguyen"
print(name * 3)
print((name + " ") * 3)			 # add proper spacing between strings
print(name[0])

print(len(name))
print(name[len(name) - 1])

print("----------------")

# s[i:j:k] | slicing
print("Let's try slicing!")

name = "BokuNoHero"

print(name[0:len(name)])		# note: in [i:j:k] is "i up to j"
print(name[::])					# no value indicates default values
print(name[::-1])				# -1 for "step" is backwards logic

name = "dekudekudeku"
print(name.count("deku"))
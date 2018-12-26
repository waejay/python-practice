import webbrowser, sys, pyperclip

# If cli arguments exist
if (len(sys.argv) > 1):

	# Get address from cli
	address = ' '.join(sys.argv[1:])
	print(address)

else:

	# Get address from clipboard
	address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)







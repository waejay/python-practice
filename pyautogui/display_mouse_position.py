""" 
display_mouse_position.py - Displays the X and Y coordinates of the mouse in the CLI

Modules:

- pyautogui:	module for programmatically controlling the mouse and keyboard
- sys: 			module for accessing variables used by interpreter

"""

import pyautogui, sys

help_tab_clicked = False
try:

	while True:

		# Get mouse coordinates
		x, y = pyautogui.position()

		# Max coordinates are 1679 x 1049 by default; convert to true max
		if (x == 1679 and y == 1049):
			x = 1680
			y = 1050

		# Click on the Sublime Text "Help" tab if mouse hovers
		if (595 < x < 641 and 0 < y < 21):
			if not help_tab_clicked:
				pyautogui.click()
				help_tab_clicked = True
		else:
			help_tab_clicked = False

		# Output string formatted as: "X: 1280, Y: 720"
		mouse_position_string = "X: {0}, Y: {1}".format(str(x).rjust(4), str(y).rjust(4))

		# Print mouse coordinates
		print(mouse_position_string, end = '')
		
		# Update the mouse coordinates while keeping mouse_position_string inline
		print('\b' * len(mouse_position_string), end = '', flush = True)

except KeyboardInterrupt:
	print("\n")
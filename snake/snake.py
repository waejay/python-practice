# this uses the 'curses' library which provides
# in-terminal screen-painting and keyboard-handling

import random
import curses

"""
initialize curses:
	- determine terminal type
	- send required setup codes to terminal
	- create various internal data structures

	return: a window object 
"""
stdscr = curses.initscr()		
curses.noecho()		

# remove blinking cursor
curses.curs_set(0)				

# screen height and width
screen_height, screen_width = stdscr.getmaxyx()

# create window
window = curses.newwin(screen_height, screen_width, 0, 0)

window.keypad(1)
window.timeout(100)

snake_x = screen_width / 4
snake_y = screen_width / 2

snake = [
	[snake_y, snake_x],
	[snake_y, snake_x - 1],
	[snake_y, snake_x - 2]

]

food = [screen_height / 2, screen_width / 2]

window.addch(int(food[0]), int(food[1]), 'π')

key = curses.KEY_RIGHT

while True:
	next_key = window.getch()
	key = key if next_key == -1 else next_key

	if snake[0][0] in [0, screen_height] or snake[0][1] in [0, screen_width] or snake[0] in snake[1:]:
		curses.endwin()
		quit()

	new_head = [snake[0][0], snake[0][1]]

	if key == curses.KEY_DOWN:
		new_head[0] += 1
	if key == curses.KEY_UP:
		new_head[0] -= 1
	if key == curses.KEY_LEFT:
		new_head[1] -= 1
	if key == curses.KEY_RIGHT:
		new_head[1] += 1

	snake.insert(0, new_head)
	if snake[0] == food:
		food = None
		while food is None:
			nf = [
				random.randint(1, screen_height - 1),
				random.randint(1, screen_width - 1)
			]
			food = nf if nf not in snake else None

		window.addch(food[0], food[1], curses.ASC_PI)
	else:
		tail = snake.pop()
		window.addch(int(tail[0]), int(tail[1]), ' ')

	window.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)

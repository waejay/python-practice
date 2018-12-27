from PIL import ImageGrab, ImageOps
import pyautogui, sys, time, numpy

# Coordinates based on [John's Macbook Pro]
class Coordinates():
	replayBtn = (420, 414)
	dinosaur = (182, 429)

def restart_game():
	pyautogui.click(Coordinates.replayBtn)

def dino_jump():
	pyautogui.keyDown('space')
	time.sleep(0.01)
	print("Jump")
	pyautogui.keyUp('space')

# Grab image of an absolute portion of [John's Macbook Pro] screen to determine if cacti is incoming
# return: a numpy value that changes if cacti incoming
def image_grab():
	box = (Coordinates.dinosaur[0] + 400, Coordinates.dinosaur[1] + 370, Coordinates.dinosaur[0] + 620, Coordinates.dinosaur[1] + 450)

	image = ImageGrab.grab(box)
	image.save("my_image.png")

	# Convert to gray scale for precision
	gray_image = ImageOps.grayscale(image)
	image_array  = numpy.array(gray_image.getcolors())
	
	# Print image array to test change in image_grab
	print (image_array.sum())
	return image_array.sum()

if __name__ == "__main__":
	
	# Click on browser window
	pyautogui.click((420,796))
		
	restart_game()

	# Initial second before first test jump
	time.sleep(1)

	dino_jump()

	# Jump if image_grab of cactus is incoming
	while True:
		if not image_grab() == 17847:
			dino_jump()
		
	
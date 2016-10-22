"""This is the entry point of the program."""


def create_box(height,width,character, border):
	if type(height) != int or type(width) != int or len(character) > 1 or height < 1 or width < 1 or type(character) != str:
		return "Something wasn't right"
	box = ''
	for i in range(height):
		for j in range(width):
			if border and i > 0 and i < height-1 and j > 0 and j < width-1:
				box += " "
			else:
			    box += character
		box += "\n"
	return box

if __name__ == '__main__':
    create_box(3, 4, '*', True)

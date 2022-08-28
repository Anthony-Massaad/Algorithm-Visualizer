import pygame
import random
from sort import merge_sort, selection_sort, insertion_sort
from color import Color
import time

class Button:


	def __init__(self, x, y, width, height, text, function):
		self.x = x
		self.y = y
		self.width = width 
		self.height = height
		self.color = Color.GREY.value 
		self.text = text 
		self.function = function 


	def draw(self, screen): 
		pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])
		screen.blit(self.text, (self.x+30, self.y))


	def pressed(self):
		self.change_state()
		return self.function()


	def change_state(self):
		if self.color == Color.GREEN.value:
			self.color = Color.GREY.value
		else:
			self.color = Color.GREEN.value 


class State:


	def __init__(self, x, y, done, running, default):
		self.active = False
		self.default = True
		self.done = done
		self.running = running
		self.default = default
		self.x = x 
		self.y = y 


	def draw(self, screen):
		if self.default: 
			screen.blit(self.default, (self.x, self.y))
		else:
			if self.active:
				screen.blit(self.running, (self.x, self.y))
			else: 
				screen.blit(self.done, (self.x, self.y))


	def change_state(self):
		self.active = not self.active
		self.default = False


class Visualizer: 


	def __init__(self):
		self.arr = []
		self.color = []


	def draw(self, screen, game_width, game_height):
		width_distance = game_width / len(self.arr)
		min_y = 120
		for i in range(len(self.arr)):
			x_pos = width_distance * i + width_distance / 2
			pygame.draw.line(screen, self.color[i], (x_pos, game_height), (x_pos, game_height - self.arr[i] - min_y*3), 2)


	def create_arr(self, length):
		self.arr = []
		self.color = []
		for i in range(length):
			self.arr.append(random.randint(10, 110))
			self.color.append(Color.BLACK.value)


class Timer:

	def __init__(self, text, font, x, y):
		self.start_time = 0
		self.text = text
		self.x = x
		self.y = y
		self.font = font
		self.end = 0


	def draw(self, screen, active, default):
		if active: 
			self.end = "{:.2f} s".format(time.time() - self.start_time)
			screen.blit(self.text, (self.x, self.y))
			screen.blit(render_text(self.font, str(self.end)), (self.x + 210, self.y))
		elif default: 
			screen.blit(self.text, (self.x, self.y))
			screen.blit(render_text(self.font, str(self.end)), (self.x + 210, self.y))
		elif not active: 
			screen.blit(self.text, (self.x, self.y))
			screen.blit(render_text(self.font, str(self.end)), (self.x + 210, self.y))


	def start(self):
		self.end = 0
		self.start_time = time.time()



def draw(screen, buttons, state, visualizer, timer, game_width, game_height):
	screen.fill(Color.WHITE.value)

	for button in buttons:
		button.draw(screen)
	state.draw(screen)

	visualizer.draw(screen, game_width, game_height)

	timer.draw(screen, state.active, state.default)

	pygame.display.update()
	pygame.time.delay(30)


def render_text(font, text):
	return font.render(text, False, Color.BLACK.value)


if __name__ == "__main__":
	pygame.font.init()
	pygame.init()
	GAME_WIDTH = 800
	GAME_HEIGHT = 608
	screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
	pygame.display.set_caption("Sorts Visualizer")
	font = pygame.font.SysFont('Arial', 30)
	run = True
	arr_length = 200

	visualizer = Visualizer()
	visualizer.create_arr(arr_length)

	state = State(50, 60, render_text(font, "Finished"), render_text(font, "Sorting"), render_text(font, "Select Sort")) 
	timer = Timer(render_text(font, "Time in seconds:"), font, 200, 60)
	buttons = [
		Button(50, 10, 200, 35, render_text(font, "Merge Sort"), lambda: merge_sort(visualizer.arr, visualizer.color, 0, len(visualizer.arr) - 1, lambda: draw(screen, buttons, state, visualizer, timer, GAME_WIDTH, GAME_HEIGHT))),
		Button(300, 10, 200, 35, render_text(font, "Selection sort"), lambda: selection_sort(visualizer.arr, visualizer.color, lambda: draw(screen, buttons, state, visualizer, timer, GAME_WIDTH, GAME_HEIGHT))),
		Button(550, 10, 200, 35, render_text(font, "Insertion Sort"), lambda: insertion_sort(visualizer.arr, visualizer.color, lambda: draw(screen, buttons, state, visualizer, timer, GAME_WIDTH, GAME_HEIGHT))),
	]

	while run: 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN and not state.active:
				x, y = pygame.mouse.get_pos()
				for button in buttons: 
					if button.x <= x <= button.x+button.width and button.y <= y <= button.y+button.height:
						if not state.default:
							visualizer.create_arr(arr_length)
						state.change_state()
						timer.start()
						if (button.pressed()):
							state.change_state()
							button.change_state()

		draw(screen, buttons, state, visualizer, timer, GAME_WIDTH, GAME_HEIGHT)

	pygame.quit()
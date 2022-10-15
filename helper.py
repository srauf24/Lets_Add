import pygame, os
pygame.font.init()
screen_width = 1400
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

font = pygame.font.SysFont('georgia', 20)
displayStartText = font.render("START SCREEN", False, (0, 0, 0))
displaySettingText = font.render("SETTINGS", False, (0, 0, 0))
displayScoreText = font.render("HIGH SCORE: ", False, (0, 0, 0))

# Animations Class -- Finished logic
# 	Takes care of all animations; characters and backgrounds
class Animations(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y, directory):
		super().__init__()
		self.attack_animation = False
		self.sprites = []
		list = os.listdir(directory)
		list.sort()

		for item in list[1:]:
			if directory == "Animations/Background":
				self.sprites.append(pygame.transform.scale(pygame.image.load(directory + '/' + item).convert(), (1400, 900)))
			else:
				self.sprites.append(pygame.image.load(directory + '/' + item).convert())

		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x, pos_y]

	def idle(self):
		self.attack_animation = True

	def update(self, speed):
		if self.attack_animation == True:
			self.current_sprite += speed
			if int(self.current_sprite) >= len(self.sprites):
				self.current_sprite = 0
				self.attack_animation = False

		self.image = self.sprites[int(self.current_sprite)]

# Text Button Class -- Finished Logic
# 	Placeholder for image based buttons
class Button:
	def __init__(self, color, x, y, width, height, text=''):
		self.color = color
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.text = text
		self.surf = pygame.Surface((width, height))
		self.surf.fill(color)
		self.rect = (x, y)

	def draw(self, win, outline=None):
		# Call this method to draw the button on the screen
		if outline:
			pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)
			pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

		if self.text != '':
			text = font.render(self.text, 1, (0, 0, 0))
			win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

	def isOver(self, pos):
		# Pos is the mouse position or a tuple of (x,y) coordinates
		if pos[0] > self.x and pos[0] < self.x + self.width:
			if pos[1] > self.y and pos[1] < self.y + self.height:
				return True
		return False


# Image Button Class -- WIP
# True button class
class ImgButton():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect


startText = Button((255, 255, 255), screen_width/2, screen_height/2, 100, 25, "Start")
settingText = Button((255, 255, 255), screen_width/2, screen_height/2 + 50, 100, 25, "Settings")
returnText = Button((255, 255, 0), 1200, 100, 100, 25, "Return")
quitText = Button((255, 255, 255), screen_width/2, screen_height/2 + 100, 100, 25, "Quit")
endlessText = Button((255, 255, 255), screen_width/2, screen_height/2, 150, 25, "Endless Mode")
versusText = Button((255, 255, 255), screen_width/2, screen_height/2 + 50, 150, 25, "Versus Mode")

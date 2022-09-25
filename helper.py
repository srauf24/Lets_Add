import pygame
pygame.font.init()
screen_width = 600
screen_height = 600
# Cookie monster Animation
class Player(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.attack_animation = False
		self.sprites = []
		self.sprites.append(pygame.image.load('Animations/17aa-0.jpg'))
		self.sprites.append(pygame.image.load('Animations/17aa-1.jpg'))
		self.sprites.append(pygame.image.load('Animations/17aa-2.jpg'))
		self.sprites.append(pygame.image.load('Animations/17aa-3.jpg'))
		self.sprites.append(pygame.image.load('Animations/17aa-4.jpg')) 
		self.sprites.append(pygame.image.load('Animations/17aa-5.jpg')) 
		self.sprites.append(pygame.image.load('Animations/17aa-6.jpg'))
		self.sprites.append(pygame.image.load('Animations/17aa-7.jpg'))
		self.sprites.append(pygame.image.load('Animations/17aa-8.jpg'))
		self.sprites.append(pygame.image.load('Animations/17aa-9.jpg'))
		self.sprites.append(pygame.image.load('Animations/17aa-10.jpg')) 
		self.sprites.append(pygame.image.load('Animations/17aa-11.jpg')) 
		self.sprites.append(pygame.image.load('Animations/17aa-12.jpg'))
		self.sprites.append(pygame.image.load('Animations/17aa-13.jpg'))
		self.sprites.append(pygame.image.load('Animations/17aa-14.jpg'))
		self.sprites.append(pygame.image.load('Animations/17aa-15.jpg'))
		self.sprites.append(pygame.image.load('Animations/17aa-16.jpg')) 
		self.sprites.append(pygame.image.load('Animations/17aa-17.jpg')) 
		self.sprites.append(pygame.image.load('Animations/17aa-18.jpg'))
		self.sprites.append(pygame.image.load('Animations/17aa-19.jpg'))
		self.sprites.append(pygame.image.load('Animations/17aa-20.jpg'))
		self.sprites.append(pygame.image.load('Animations/17aa-21.jpg'))
		self.sprites.append(pygame.image.load('Animations/17aa-22.jpg')) 
		self.sprites.append(pygame.image.load('Animations/17aa-23.jpg')) 
		self.sprites.append(pygame.image.load('Animations/17aa-24.jpg'))
		self.sprites.append(pygame.image.load('Animations/17aa-25.jpg'))
		self.sprites.append(pygame.image.load('Animations/17aa-26.jpg'))
		self.sprites.append(pygame.image.load('Animations/17aa-27.jpg'))
		self.sprites.append(pygame.image.load('Animations/17aa-28.jpg')) 
		self.sprites.append(pygame.image.load('Animations/17aa-29.jpg')) 
		self.sprites.append(pygame.image.load('Animations/17aa-30.jpg'))
		self.sprites.append(pygame.image.load('Animations/17aa-31.jpg'))
		self.sprites.append(pygame.image.load('Animations/17aa-32.jpg'))
		self.sprites.append(pygame.image.load('Animations/17aa-33.jpg'))
		self.sprites.append(pygame.image.load('Animations/17aa-34.jpg')) 
		self.sprites.append(pygame.image.load('Animations/17aa-35.jpg')) 
		self.sprites.append(pygame.image.load('Animations/17aa-36.jpg'))        




		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x,pos_y]

	def attack(self):
		self.attack_animation = True

	def update(self,speed):
		if self.attack_animation == True:
			self.current_sprite += speed
			if int(self.current_sprite) >= len(self.sprites):
				self.current_sprite = 0
				self.attack_animation = False

		self.image = self.sprites[int(self.current_sprite)]



font = pygame.font.SysFont('georgia', 20)
displayStartText = font.render("START SCREEN", False, (0,0,0))
displaySettingText = font.render("SETTINGS", False, (0,0,0))
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
			win.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))
	def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
		if pos[0] > self.x and pos[0] < self.x + self.width:
			if pos[1] > self.y and pos[1] < self.y + self.height:	
				return True
		return False

startText = Button((255,255,255),screen_height/2, screen_width/2, 100, 25, "Start")
settingText = Button((255,255,255),screen_height/2 + 50, screen_width/2 + 50, 100, 25, "Settings")
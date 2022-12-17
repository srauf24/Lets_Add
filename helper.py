import pygame, os
pygame.font.init()
screen_width = 1400
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

fontBold = pygame.font.Font('Fonts/PixelBold.ttf', 80)
fontMono = pygame.font.Font('Fonts/PixelMono.ttf', 20)
fontSans = pygame.font.Font('Fonts/PixelSans.ttf', 20)
fontSansB = pygame.font.Font('Fonts/PixelSans.ttf', 50)
displayStartText = fontSans.render("START SCREEN", False, (0, 0, 0))
displaySettingText = fontSans.render("SETTINGS", False, (0, 0, 0))
displayScoreText = fontSans.render("HIGH SCORE: ", False, (0, 0, 0))
exp1 = "Each character has its own mystery power in which they can avoid a specific arithemtic operation!\n\nThere are two different modes: Endless and Versus." 
exp2 = """\nIn Endless mode, you need to get as many questions as you can correct. You will be asked math questions using basic operations (+, -, *, //). Press Q to start the sequence of questions, enter your numeric answer, and press space to submit. 
Each question answered correctly will increase your score which will at first look like this! \n\n\nWhenever you answer a question incorrectly, you'll lose a life which will inititially look like this. 
\n\n\nIn Versus mode, you get to go up against your friend! Just like Endless mode, each player will have hearts and a score. The player who has the largest score is the winner! In the case that both players have the same score, a draw will be declared."""
# Animations Class -- Finished logic
# 	Takes care of all animations; characters and backgrounds
class Animations(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y, directory):
		super().__init__()
		self.attack_animation = False
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.sprites = []
		list = os.listdir(directory)
		list.sort()

		for item in list[1:]:
			if directory == "Animations/Background" or directory == "Animations/Background2" or directory == "Animations/Background3" or directory == "Animations/Background4":
				self.sprites.append(pygame.transform.scale(pygame.image.load(directory + '/' + item).convert(), (1400,900)))
			else:
				self.sprites.append(pygame.image.load(directory + '/' + item).convert())

		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]

		self.width = self.image.get_width()
		self.height = self.image.get_height()
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

	def isOver(self, pos):
		if pos[0] > self.pos_x and pos[0] < self.pos_x + self.width:
			if pos[1] > self.pos_y and pos[1] < self.pos_y + self.height:
				return True
		return False

# Text Button Class
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
		if outline:
			pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)
			pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

		if self.text != '':
			text = fontSans.render(self.text, 1, (0, 0, 0))
			win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

	def isOver(self, pos):
		if pos[0] > self.x and pos[0] < self.x + self.width:
			if pos[1] > self.y and pos[1] < self.y + self.height:
				return True
		return False

class Player():
	def __init__(self, player):
		self.lives = 3
		self.character = "placeholder"
		self.player = player
		self.game_sprites = pygame.sprite.Group()
		self.score = 0
	def setCharacter(self, character, player):
		self.character = character
		if player == 1:
			if character == "Animations/SilverSitAnimation":
				self.player1Animation = Animations(100, 300, character)
			else:
				self.player1Animation = Animations(50, 350, character)
			self.game_sprites.add(self.player1Animation)
		if player == 2:
			if character == "Animations/SilverSitAnimation":
				self.player2Animation = Animations(850, -100, character)
			else:
				self.player2Animation = Animations(800, -60, character)
			self.game_sprites.add(self.player2Animation) 

def display_text(surface, text, pos, font, color):
    collection = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    x,y = pos
    for lines in collection:
        for words in lines:
            word_surface = font.render(words, True, color)
            word_width , word_height = word_surface.get_size()
            if x + word_width >= 1100:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x,y))
            x += word_width + space
        x = pos[0]
        y += word_height

def comparison(x, y):
	if x > y:
		return 1
	if y > x:
		return 2
	if x == y:
		return 3

score = pygame.transform.scale(pygame.image.load("Images/score.png").convert(), (93,39))
health = pygame.transform.scale(pygame.image.load("Images/lives.png").convert(), (113,37))
box = pygame.transform.scale(pygame.image.load("Images/textBox.png"), (1300,800))
answerBox = pygame.transform.scale(pygame.image.load("Images/textBox.png"), (800,800))
heart = pygame.transform.scale(pygame.image.load("Images/heart.png"), (100,100))
platform = pygame.transform.scale(pygame.image.load("Images/platform.png"), (800,800))
mute = pygame.transform.scale(pygame.image.load("Images/mute.png"), (100,100))
startText = Button((255, 255, 255), screen_width/2, screen_height/2, 100, 25, "Start")
settingText = Button((255, 255, 255), screen_width/2, screen_height/2 + 50, 100, 25, "Settings")
returnText = Button((255, 255, 255), 1200, 100, 100, 25, "Return")
volumeText = Button((255, 255, 255), screen_width/2, screen_height/2, 100, 25, "Volume")
howToText = Button((255, 255, 255), screen_width/2, screen_height/2 + 50, 130, 25, "How to Play")
quitText = Button((255, 255, 255), screen_width/2, screen_height/2 + 100, 100, 25, "Quit")
endlessText = Button((255, 255, 255), screen_width/2, screen_height/2, 150, 25, "Endless Mode")
versusText = Button((255, 255, 255), screen_width/2, screen_height/2 + 50, 150, 25, "Versus Mode")
playAgain = Button((255, 255, 255), screen_width/2 - 80, screen_height/2 + 25, 150, 25, "Play Again?")
same = Button((255, 255, 255), screen_width/2 - 150, screen_height/2 + 100, 200, 25, "Same Characters")
change = Button((255, 255, 255), screen_width/2 + 150, screen_height/2 + 100, 220, 25, "Change Characters")

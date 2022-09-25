import pygame, sys
from helper import *

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
	K_0
)

# General setup
pygame.init()
clock = pygame.time.Clock()
pygame.font.init()


# Game Screen
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height), pygame.RESIZABLE)

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(100,100)
moving_sprites.add(player)

# Start Screen
start = True

# Setting Screen
setting = False
displaySettingText = font.render("SETTINGS", False, (0,0,0))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()
			if event.key == pygame.K_0:
				player.attack()
			
    
	while (start):
		for event in pygame.event.get():
			pos = pygame.mouse.get_pos()
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()
				if event.key == pygame.K_0:
					start = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if startText.isOver(pos):
					print("Start is pressed")
					start = False
				if settingText.isOver(pos):
					print("Settings is pressed")
					setting = True
					start = False


		screen.fill((255,255,255))
		startText.draw(screen, (255,255,255))
		settingText.draw(screen, (255,255,255))
		pygame.display.flip()

	while (setting):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()
				if event.key == pygame.K_0:
					start = True
					setting = False
			
		screen.fill((255,255,255))
		screen.blit(displaySettingText,(100,100))
		pygame.display.flip()



    # Drawing
	screen.fill((0,0,0)) 
	moving_sprites.draw(screen)
	moving_sprites.update(0.25)
	pygame.display.flip()
	clock.tick(240)

pygame.quit()
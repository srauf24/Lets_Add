from time import sleep
import pygame, sys, os
from helper import *
# samee
# gabe
# william
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
HS_FILE = open('versus_highscore.txt', 'r')
HS_FILE_2 = open('endless_highscore.txt', 'r')

# Game Screen
screen_width = 1400
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
sleepFox = Animations(100, 0, 'Animations/SleepFoxAnimation')
goldieSit = Animations(750, 0, 'Animations/GoldieAnimation')
silverSit = Animations(100, 350, 'Animations/SilverSitAnimation')
catRun = Animations(750, 350, 'Animations/CatRunAnimation')
moving_sprites.add(sleepFox)
moving_sprites.add(goldieSit)
moving_sprites.add(silverSit)
moving_sprites.add(catRun)

startScreen = pygame.sprite.Group()
background = Animations(0, 0, 'Animations/Background')
startScreen.add(background)

choosingCharacterScreen = pygame.sprite.Group()
background2 = Animations(0,0, 'Animations/Background2')
choosingCharacterScreen.add(background2)

# Start Screen
start = True

# Selecting Mode
playerMode = False

# Setting Screen
setting = False
displaySettingText = font.render("SETTINGS", False, (0, 0, 0))

# Choosing Character Screen
choosing = False
displayChoosingText = font.render("CHOOSE YOUR CHARACTER", False, (0, 0, 0))
displayScoreText = font.render("HIGH SCORE: ", False, (0, 0, 0))

# Endless Mode Screen
endlessMode = False

# Versus Mode Screen
versusMode = False

# WIP
displayyWIP = font.render("WORK IN PROGRESS", False, (255, 255, 255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    # Start Screen -- WIP
    # 	Finished logic / Incomplete GUI
    while start:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if startText.isOver(pos):
                    print("Start is pressed")
                    start = False
                    playerMode = True
                if settingText.isOver(pos):
                    print("Settings is pressed")
                    setting = True
                    start = False
                if quitText.isOver(pos):
                    print("Quit is pressed")
                    pygame.quit()
                    sys.exit()

        screen.fill((255, 255, 255))
        startScreen.draw(screen)
        startScreen.update(0.15)
        background.idle()
        startText.draw(screen, (255, 255, 255))
        settingText.draw(screen, (255, 255, 255))
        quitText.draw(screen, (255, 255, 255))

<<<<<<< HEAD
        pygame.display.flip()
=======
		screen.fill((255,255,255))
		startScreen.draw(screen)
		startScreen.update(0.05)
		background.idle()
		startText.draw(screen, (255,255,255))
		settingText.draw(screen, (255,255,255))
		quitText.draw(screen, (255,255,255))
		
		pygame.display.flip()
>>>>>>> 72f6b7e (small changes)

    # Settings Screen -- WIP
    #	Incomplete logic / Incomplete GUI
    while setting:
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
                    start = True
                    setting = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if returnText.isOver(pos):
                    print("Return is pressed")
                    setting = False
                    start = True

        screen.fill((255, 255, 0))
        screen.blit(displaySettingText, (screen_width / 2 - displaySettingText.get_width() / 2, 50))
        returnText.draw(screen, (255, 255, 0))
        pygame.display.flip()

    # Player Mode Screen -- WIP
    # 	Finished logic / Incomplete GUI
    while playerMode:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    playerMode = False
                    choosing = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if endlessText.isOver(pos):
                    print("Endless is pressed")
                    playerMode = False
                    endlessMode = choosing = True

<<<<<<< HEAD
                if versusText.isOver(pos):
                    print("Versus is pressed")
                    playerMode = False
                    versusMode = choosing = True

        pygame.display.flip()
        screen.fill((0, 255, 0))
        endlessText.draw(screen, (255, 255, 255))
        versusText.draw(screen, (255, 255, 255))
        clock.tick(240)

    # Choosing Character Screen -- WIP
    # 	Incomplete logic / Incomplete GUI
    while choosing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    setting = True
                    choosing = False
                if event.key == pygame.K_1:
                    choosing = False
=======
	# Player Mode Screen -- WIP
	# 	Finished logic / Incomplete GUI
	while(playerMode):
		for event in pygame.event.get():
			pos = pygame.mouse.get_pos()
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_0:
					playerMode = False
					choosing = True
			# if event.type == pygame.MOUSEBUTTONDOWN:
			# 	if endlessText.isOver(pos):
			# 		print("Endless is pressed")
			# 		playerMode = False
			# 		endlessMode = choosing = True

			# 	if versusText.isOver(pos):
			# 		print("Versus is pressed")
			# 		playerMode = False
			# 		versusMode = choosing = True

	
		choosingCharacterScreen.draw(screen)
		background2.idle()
		background2.update(0.05)
		endlessText.draw(screen, (255,255,255))
		versusText.draw(screen, (255,255,255))
		pygame.display.flip()
		clock.tick(240)
>>>>>>> 72f6b7e (small changes)

        screen.fill((0, 0, 255))
        screen.blit(displayChoosingText, (screen_width / 2 - displayChoosingText.get_width() / 2, 50))
        screen.blit(displayScoreText, (screen_width / 7 - displayScoreText.get_width() / 2, 50))
        moving_sprites.draw(screen)
        moving_sprites.update(0.1)
        sleepFox.idle()
        goldieSit.idle()
        silverSit.idle()
        catRun.idle()
        pygame.display.flip()
        clock.tick(240)

<<<<<<< HEAD
    # Endless Mode Screen
    # 	Incomplete logic / Incomplete GUI
    while endlessMode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))
        pygame.display.flip()

    # Versus Mode Screen
    # 	Incomplete logic / Incomplete GUI
    while versusMode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
=======
	# Choosing Character Screen -- WIP
	# 	Incomplete logic / Complete GUI
	while(choosing):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_0:
					setting = True
					choosing = False
				if event.key == pygame.K_1:
					choosing = False
		
		choosingCharacterScreen.draw(screen)
		background2.idle()
		background2.update(0.05)
		screen.blit(displayChoosingText, (screen_width/2 - displayChoosingText.get_width()/2,50))
		moving_sprites.draw(screen)
		moving_sprites.update(0.05)
		sleepFox.idle()
		goldieSit.idle()
		silverSit.idle()
		catRun.idle()
		pygame.display.flip()
		clock.tick(240)

	# Endless Mode Screen
	# 	Incomplete logic / Incomplete GUI
	while(endlessMode):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		
		screen.fill((255,255,255))
		screen.blit(displayyWIP, ((screen_width/2) - (displayChoosingText.get_width()/2), (screen_height/2) - (displayChoosingText.get_height()/2)))
		pygame.display.flip()

	
	# Versus Mode Screen
	# 	Incomplete logic / Incomplete GUI
	while(versusMode):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		
		screen.fill((255,255,255))
		screen.blit(displayyWIP, ((screen_width/2) - (displayChoosingText.get_width()/2), (screen_height/2) - (displayChoosingText.get_height()/2)))
		pygame.display.flip()
>>>>>>> 72f6b7e (small changes)

        screen.fill((255, 255, 255))
        pygame.display.flip()

<<<<<<< HEAD
    pygame.display.flip()
    screen.fill((0, 0, 0))
    screen.blit(displayyWIP, ((screen_width / 2) - (displayChoosingText.get_width() / 2),
                              (screen_height / 2) - (displayChoosingText.get_height() / 2)))
    clock.tick(240)
=======

	screen.fill((0,0,0))
	screen.blit(displayyWIP, ((screen_width/2) - (displayChoosingText.get_width()/2), (screen_height/2) - (displayChoosingText.get_height()/2)))
	pygame.display.flip()
	clock.tick(240)
>>>>>>> 72f6b7e (small changes)

pygame.quit()
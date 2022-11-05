from time import sleep
import pygame, sys, os
from helper import *
from pygame import mixer
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
bg_music = mixer.music.load('Sounds/persona5.mp3')
mixer.music.play()
mixer.music.set_volume(0.3)

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

fightingScreen = pygame.sprite.Group()
background3 = Animations(0,0, 'Animations/Background3')
fightingScreen.add(background3)

# Start Screen
start = True

Player1 = Player(1)
Player2 = Player(2)

# Selecting Mode
playerMode = False
amountofPlayers = 0

# Setting Screen
setting = False
displaySettingText = fontBold.render("SETTINGS", False, (0, 0, 0))

# Choosing Character Screen
choosing1 = False
choosing2 = False
displayChoosingText = fontBold.render("CHOOSE YOUR CHARACTER", False, (0, 0, 0))
displayPlayerChoosing1 = fontSans.render("Player 1's Turn!", False, (0, 0, 0))
displayPlayerChoosing2 = fontSans.render("Player 2's Turn!", False, (0, 0, 0))
displayScoreText = fontSans.render("HIGH SCORE: ", False, (0, 0, 0))

# Endless Mode Screen
endlessMode = False

# Versus Mode Screen
versusMode = False

# End Screen
end = False

# WIP
displayyWIP = fontSans.render("WORK IN PROGRESS", False, (255, 255, 255))

while True:

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
                    print("Escape is pressed")
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
        startScreen.update(0.1)
        background.idle()
        startText.draw(screen, (255, 255, 255))
        settingText.draw(screen, (255, 255, 255))
        quitText.draw(screen, (255, 255, 255))
        pygame.display.flip()

        
    # Settings Screen -- WIP
    #	Incomplete logic / Incomplete GUI
    # Only Volume text mutes background music not the image itself -- WIP
    volume_flag = True
    while setting:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("Escape is pressed")
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
                if volumeText.isOver(pos):
                    if volume_flag:
                        print("Volume is muted")
                        mixer.music.set_volume(0.0)
                        setting = True
                        volume_flag = False
                    elif not volume_flag:
                        print("Volume is unmuted")  
                        mixer.music.set_volume(0.3)
                        setting = True
                        volume_flag = True
                

        screen.fill((255, 255, 0))
        screen.blit(sound, (650, 550))
        screen.blit(displaySettingText, (screen_width / 2 - displaySettingText.get_width() / 2, 50))
        returnText.draw(screen, (255, 255, 0))
        volumeText.draw(screen, (255, 255, 0))
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
                    choosing1 = True
                    endlessMode = True
                    amountofPlayers = 1
                    playerMode = False
                if versusText.isOver(pos):
                    print("Versus is pressed")
                    choosing1 = True
                    versusMode = True
                    amountofPlayers = 2
                    playerMode = False

	
        choosingCharacterScreen.draw(screen)
        background2.idle()
        background2.update(0.1)
        endlessText.draw(screen, (255,255,255))
        versusText.draw(screen, (255,255,255))
        pygame.display.flip()
        clock.tick(240)

	# Choosing Character Screen -- WIP
	# 	Incomplete logic / Complete GUI
    mixer.music.load("Sounds/choose.mp3")
    mixer.music.stop()
    mixer.music.play()
    while choosing1:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    setting = True
                    choosing = False
                if event.key == pygame.K_1:
                    choosing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if sleepFox.isOver(pos):
                    Player1.setCharacter('Animations/SleepFoxAnimation', 1)
                    choosing1 = False
                if goldieSit.isOver(pos):
                    Player1.setCharacter('Animations/GoldieAnimation', 1)
                    choosing1 = False
                if silverSit.isOver(pos):
                    Player1.setCharacter("Animations/SilverSitAnimation", 1)
                    choosing1 = False
                if catRun.isOver(pos):
                    Player1.setCharacter("Animations/CatRunAnimation" , 1)
                    choosing1 = False
                
                if (amountofPlayers == 2):
                    choosing2 = True
                if (amountofPlayers == 1 and choosing1 == False):
                    mixer.music.stop()         
		
        choosingCharacterScreen.draw(screen)
        background2.idle()
        background2.update(0.05)
        screen.blit(displayChoosingText, (screen_width/2 - displayChoosingText.get_width()/2,50))
        screen.blit(displayPlayerChoosing1, (screen_width/2 - displayPlayerChoosing1.get_width()/2,150))
        moving_sprites.draw(screen)
        moving_sprites.update(0.05)
        sleepFox.idle()
        goldieSit.idle()
        silverSit.idle()
        catRun.idle()
        pygame.display.flip()
        clock.tick(240)

    while choosing2:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    setting = True
                    choosing = False
                if event.key == pygame.K_1:
                    choosing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if sleepFox.isOver(pos):
                    Player2.setCharacter("Animations/SleepFoxAnimation" , 2)
                    mixer.music.stop()
                    choosing2 = False
                if goldieSit.isOver(pos):
                    Player2.setCharacter("Animations/GoldieAnimation", 2)
                    mixer.music.stop()
                    choosing2 = False
                if silverSit.isOver(pos):
                    Player2.setCharacter("Animations/SilverSitAnimation" , 2)
                    mixer.music.stop()
                    choosing2 = False
                if catRun.isOver(pos):
                    Player2.setCharacter("Animations/CatRunAnimation", 2)
                    mixer.music.stop()   
                    choosing2 = False     
		
        choosingCharacterScreen.draw(screen)
        background2.idle()
        background2.update(0.1)
        screen.blit(displayChoosingText, (screen_width/2 - displayChoosingText.get_width()/2,50))
        screen.blit(displayPlayerChoosing2, (screen_width/2 - displayPlayerChoosing2.get_width()/2,150))
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
    # Added different background music
    mixer.music.load("Sounds/maplestory1.mp3")
    mixer.music.stop()
    mixer.music.play()
    while endlessMode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    endlessMode = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
		
        fightingScreen.draw(screen)
        background3.idle()
        background3.update(0.1)
        screen.blit(platform, (-60, 450))
        Player1.game_sprites.draw(screen)
        Player1.game_sprites.update(0.1)
        Player1.player1Animation.idle()
        for i in range(Player1.lives):
            screen.blit(heart, (100 + (100*i), 770))
        pygame.display.flip()

	
	# Versus Mode Screen
	# 	Incomplete logic / Incomplete GUI
    # Added different background music
    mixer.music.load("Sounds/maplestory2.mp3")
    mixer.music.stop()
    mixer.music.play()
    while versusMode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    versusMode = True
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
		
        fightingScreen.draw(screen)
        background3.idle()
        background3.update(0.1)
        screen.blit(platform, (-60, 450))
        screen.blit(platform, (700, 50))
        Player1.game_sprites.draw(screen)
        Player1.game_sprites.update(0.15)
        Player2.game_sprites.draw(screen)
        Player2.game_sprites.update(0.15)
        Player1.player1Animation.idle()
        Player2.player2Animation.idle()
        for i in range(Player1.lives):
            screen.blit(heart, (150 + (100*i), 800))
        for i in range(Player2.lives):
            screen.blit(heart, (900 + (100*i), 400))
        pygame.display.flip()

    while end:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

        screen.fill((0,0,0))
        screen.blit(displayyWIP, ((screen_width/2) - (displayChoosingText.get_width()/2), (screen_height/2) - (displayChoosingText.get_height()/2)))
        pygame.display.flip()
        clock.tick(240)

pygame.quit()
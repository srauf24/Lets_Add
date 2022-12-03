from time import sleep
import pygame, sys, os
from helper import *
from pygame import mixer
from endless_Mode import *
from versus_mode import *

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
# HS_FILE = open('versus_highscore.txt', 'r')
# HS_FILE_2 = open('endless_highscore.txt', 'r')

# Game Screen
screen_width = 1400
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
mixer.music.load("Sounds/persona5.mp3")
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
background4 = Animations(0,0, 'Animations/Background4')
fightingScreen.add(background4)

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
HowToPlay = False

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
end1 = False
end2 = False
again = False

question = fontBold.render("Press Q", False, (0,0,0))
font_size = pygame.font.Font(None, 75)
score = fontSansB.render("Highscore: ", False, (255,255,255))
user_text = ""
turn = 1
amountQ = 20

with open("endless_highscore.txt") as f:
    highScore = f.read()[:-1]
    print(type(highScore))
    scoreText = fontSansB.render(highScore, False, (0,0,0))


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

        startScreen.draw(screen)
        startScreen.update(0.1)
        background.idle()
        startText.draw(screen, (255, 255, 255))
        settingText.draw(screen, (255, 255, 255))
        quitText.draw(screen, (255, 255, 255))
        pygame.display.flip()

        
    # Settings Screen -- Finished Logic
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
                if event.key == pygame.K_0 and HowToPlay == True:
                    HowToPlay = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if returnText.isOver(pos):
                    print("Return is pressed")
                    HowToPlay = False
                    start = True
                    setting = False
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
                if howToText.isOver(pos):
                    HowToPlay = True
                

        startScreen.draw(screen)
        startScreen.update(0.1)
        screen.blit(displaySettingText, (screen_width / 2 - displaySettingText.get_width() / 2, 50))
        returnText.draw(screen, (255, 255, 255))
        volumeText.draw(screen, (255, 255, 255))
        howToText.draw(screen, (255,255,255))
        if HowToPlay:
            pygame.draw.rect(screen, (255,255,255), (200, 100, 900, 700))
            pygame.draw.rect(screen, (0,0,0), (200, 100, 900, 700), 3)
            display_text(screen, exp1, (220, 120), fontSans, (0,0,0))
            display_text(screen, exp2, (220, 200), fontSans, (0,0,0))
            screen.blit(health, (550, 430))
            screen.blit(score, (550, 310))
        

        pygame.display.flip()

	# Player Mode Screen -- WIP
	# 	Finished logic / Incomplete GUI
    while playerMode:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if endlessText.isOver(pos):
                    print("Endless is pressed")
                    choosing1 = True
                    end1 = True
                    endlessMode = True
                    amountofPlayers = 1
                    playerMode = False
                if versusText.isOver(pos):
                    print("Versus is pressed")
                    choosing1 = True
                    end2 = True
                    versusMode = True
                    amountofPlayers = 2
                    playerMode = False
                if returnText.isOver(pos):
                    print("Return was pressed")
                    start = True
                    playerMode = False

	
        choosingCharacterScreen.draw(screen)
        background2.idle()
        background2.update(0.1)
        endlessText.draw(screen, (255,255,255))
        versusText.draw(screen, (255,255,255))
        returnText.draw(screen, (255,255,255))
        pygame.display.flip()
        clock.tick(240)

	# Choosing Character Screen -- WIP
	# 	Incomplete logic / Complete GUI
    if not start:
        voiceover = mixer.Sound('Sounds/choose.mp3')
        voiceover.play()
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
                elif goldieSit.isOver(pos):
                    Player1.setCharacter('Animations/GoldieAnimation', 1)
                    choosing1 = False
                elif silverSit.isOver(pos):
                    Player1.setCharacter("Animations/SilverSitAnimation", 1)
                    choosing1 = False
                elif catRun.isOver(pos):
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
                elif goldieSit.isOver(pos):
                    Player2.setCharacter("Animations/GoldieAnimation", 2)
                    mixer.music.stop()
                    choosing2 = False
                elif silverSit.isOver(pos):
                    Player2.setCharacter("Animations/SilverSitAnimation" , 2)
                    mixer.music.stop()
                    choosing2 = False
                elif catRun.isOver(pos):
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
    mixer.music.unload()
    mixer.music.load("Sounds/maplestory1.mp3")
    mixer.music.stop()
    mixer.music.play()
    while endlessMode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    myArray = get_question(Player1.character)
                    qText = myArray[0]
                    question = fontBold.render(qText, False, (0,0,0))
                if event.key == pygame.K_SPACE:
                    if user_text != str(myArray[1]):
                        Player1.lives = Player1.lives - 1
                        if Player1.lives == 0:
                            fileE = open('endless_highscore.txt', 'w')
                            if Player1.score > int(highScore):
                                scoreText = fontSansB.render(str(Player1.score), False, (0,0,0))
                                fileE.write(str(Player1.score))
                            fileE.close()
                            end = True
                            endlessMode = False
                    elif user_text == str(myArray[1]):
                            Player1.score += 100
                    user_text = ""
                    myArray = get_question(Player1.character)
                    qText = myArray[0] 
                    question = fontBold.render(qText, False, (0,0,0))
                x = event.unicode
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if (x.isnumeric() or x == "-") and len(user_text) < 2:
                    user_text += x
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                

        fightingScreen.draw(screen)
        background4.idle()
        background4.update(0.1)
        screen.blit(platform, (-60, 450))
        Player1.game_sprites.draw(screen)
        Player1.game_sprites.update(0.1)
        Player1.player1Animation.idle()
        for i in range(Player1.lives):
            screen.blit(heart, (100 + (100*i), 770))
        screen.blit(box, (-100,-200))
        screen.blit(answerBox, (700,380))
        answerText = fontBold.render(user_text, False, (0,0,0))
        screen.blit(answerText, (1025,700))
        screen.blit(question, (300, 130))
        screen.blit(score, (950, 0))
        screen.blit(scoreText, (1235, 0))
        screen.blit(fontBold.render(str(Player1.score), False, (255,255,255)), (550, 800))

        pygame.display.flip()


	# Versus Mode Screen
	# 	Incomplete logic / Incomplete GUI
    # Added different background music
    mixer.music.unload()
    mixer.music.load("Sounds/maplestory2.mp3")
    mixer.music.stop()
    mixer.music.play()
    while versusMode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    myArray = get_question(Player1.character)
                    qText = myArray[0]
                    question = fontBold.render(qText, False, (0,0,0))
                if event.key == pygame.K_SPACE:
                    if(amountQ > 10):
                        print("Player 1 amount left: ", amountQ//2)
                        if user_text != str(myArray[1]):
                            Player1.lives = Player1.lives - 1
                            if Player1.lives == 0:
                                amountQ = 11
                        elif user_text == str(myArray[1]):
                            Player1.score += 100
                        if(amountQ > 10):
                            user_text = ""
                            myArray = get_question(Player1.character)
                            qText = myArray[0] 
                            question = fontBold.render(qText, False, (0,0,0))
                        amountQ -= 1
                    elif(amountQ > 0 and amountQ <= 10):
                        print("Player 2 amount left: ", amountQ)
                        if user_text != str(myArray[1]):
                            Player2.lives = Player2.lives - 1
                            if Player2.lives == 0:
                                amountQ = 0
                        elif user_text == str(myArray[1]):
                            Player2.score += 100
                        if amountQ > 0 and amountQ <= 10:
                            user_text = ""
                            myArray = get_question(Player2.character)
                            qText = myArray[0] 
                            question = fontBold.render(qText, False, (0,0,0))
                            amountQ -= 1
                    elif(amountQ == 0):
                        fileV = open('versus_highscore.txt', 'w')
                        if Player1.score >= Player2.score:
                            fileV.write(str(Player1.score))
                        elif Player2.score >= Player1.score:
                            fileV.write(str(Player2.score))
                        fileV.close()
                        end = True
                        versusMode = False
                x = event.unicode
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if (x.isnumeric() or x == "-") and len(user_text) < 2:
                    user_text += x
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
		
        fightingScreen.draw(screen)
        background4.idle()
        background4.update(0.15)
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

        screen.blit(box, (-200,-200))
        screen.blit(answerBox, (700,380))
        answerText = fontBold.render(user_text, False, (0,0,0))
        screen.blit(answerText, (1025,700))
        screen.blit(question, (225, 130))
        screen.blit(fontBold.render(str(Player1.score), False, (255,255,255)), (550, 800))
        screen.blit(fontBold.render(str(Player2.score), False, (255,255,255)), (1225, 400))
        
        pygame.display.flip()

    while end:
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
                    if playAgain.isOver(pos):
                        mixer.music.unload()
                        print("Again was pressed")
                        Player1.score = 0
                        Player1.lives = 3
                        Player2.score = 0
                        start = True
                        end = False


        startScreen.draw(screen)
        startScreen.update(0.1)
        if end1:
            end1Text = fontSans.render("Your High Score was: " + str(Player1.score), False, (0,0,0))
            screen.blit(end1Text, (screen_width/2 - end1Text.get_width()/2, screen_height/2 - end1Text.get_height()))

        if end2:
            x = comparison(Player1.score, Player2.score)
            if x == 1: 
                end2Text = fontSans.render("The winner is Player 1 with a highscore of: " + str(Player1.score) + "!", False, (0,0,0))
            if x == 2:
                end2Text = fontSans.render("The winner is Player 2 with a highscore of: " + str(Player2.score) + "!", False, (0,0,0))
            if x == 3:
                end2Text = fontSans.render("It's a tie!", False, (0,0,0))
            screen.blit(end2Text, (screen_width/2 - end2Text.get_width()/2, screen_height/2 - end2Text.get_height()))
            
        playAgain.draw(screen, (255,255,255))
        pygame.display.flip()

pygame.quit()
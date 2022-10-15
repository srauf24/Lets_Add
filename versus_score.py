import pygame, sys, os

# Working on implementing score WIP
def update_versus(score):
    # Opens the text file for versus
    file = open('versus_highscore.txt', 'w')
    # Updates the score
    file.write(str(score))
    file.close()


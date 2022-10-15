import pygame, sys, os
from os import path

# Working on implementing score WIP
def update_endless(score):
    # Opens the text file for versus
    file = open('endless_highscore.txt', 'w')
    # Updates the score
    file.write(str(score))
    file.close()

#Crie um programa que abra e execute um arquivo em MP3

import pygame
pygame.init()
pygame.mixer.music.load('rtr.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

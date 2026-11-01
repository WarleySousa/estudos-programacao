import pygame

pygame.init()
pygame.mixer.music.load('ex021a.mp3')
pygame.mixer.music.play()

# O programa vai pausar aqui até você apertar Enter no terminal
input('Pressione Enter para parar a música e encerrar...')


import random
import pygame
import tkinter

def gamba():
    pygame.init()

    screen = pygame.display.set_mode((1920,1080))
    pygame.display.set_caption("Gamba")
    set_image = pygame.image.load("background.png")
    screen.blit(set_image, (-500,-500))
    set_image = pygame.image.load("gamba.png")
    screen.blit(set_image, (200,-50))
    set_image = pygame.image.load("button_exit2.png")
    screen.blit(set_image, (850,650))
    set_button1 = pygame.image.load("button_play.png")
    screen.blit(set_button1, (850,500))
    set_button2 = pygame.image.load("button_exit.png")
    screen.blit(set_button2, (850,650))
    pygame.display.flip()


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > 850 and x < 1050 and y > 650 and y < 750:
                    pygame.quit()
    pygame.quit()

gamba()
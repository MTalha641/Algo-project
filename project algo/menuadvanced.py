import pygame
import sys
import random
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from random import randint
from itertools import combinations
from math import atan2
import brute_final
import jarvis_final
import graham_final
import quickfinal
import chans
import line_final
import ccw
import polygon

# Constants 
SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
navy = (0,0,128)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Game Selector')
clock = pygame.time.Clock()

plt.ion()

current_menu = 'main'

# Button click detection
button_clicked = False

def draw_text(text, size, x, y):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)
    
    
def main_menu():
    running = True
    button_font = pygame.font.SysFont(None, 30)

    while running:
        screen.fill(BLACK)
        draw_text('Algo Project', 40, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        draw_text('Syed Ismail  Ibad Ahmed Muhammad Talha',40,SCREEN_WIDTH // 2 , SCREEN_HEIGHT //3 )
        
        # Draw buttons for each algorithm
        button1 = pygame.Rect(SCREEN_WIDTH // 2.5, SCREEN_HEIGHT // 2, 200, 50)
        button2 = pygame.Rect(SCREEN_WIDTH // 2.5, SCREEN_HEIGHT // 2 + 60, 200, 50)
        button3 = pygame.Rect(SCREEN_WIDTH // 2.5, SCREEN_HEIGHT // 2+120, 325, 50)
        button4= pygame.Rect(SCREEN_WIDTH // 2.5, SCREEN_HEIGHT // 2 + 180 ,200, 50)
        button5 = pygame.Rect(SCREEN_WIDTH // 2.5, SCREEN_HEIGHT // 2 + 240, 200, 50)
        button6 = pygame.Rect(SCREEN_WIDTH // 2.5, SCREEN_HEIGHT // 2 + 300, 200, 50)
        button7 = pygame.Rect(SCREEN_WIDTH // 2.5, SCREEN_HEIGHT // 2 + 360, 250, 50)
        button8 = pygame.Rect(SCREEN_WIDTH // 2.5, SCREEN_HEIGHT // 2 + 420, 275, 50)
        
        

        pygame.draw.rect(screen, navy, button1)
        pygame.draw.rect(screen, navy, button2)
        pygame.draw.rect(screen, navy, button3)
        pygame.draw.rect(screen, navy, button4)
        pygame.draw.rect(screen, navy, button5)
        pygame.draw.rect(screen, navy, button6)
        pygame.draw.rect(screen, navy, button7)
        pygame.draw.rect(screen, navy, button8)

        draw_text('Jarvis March', 30, button1.centerx, button1.centery)
        draw_text('Brute Force', 30, button2.centerx, button2.centery)
        draw_text('Bounded Box Line Intersection', 30, button3.centerx, button3.centery)
        draw_text('Quick elimination', 30, button4.centerx, button4.centery)
        draw_text('Chans Algorithm', 30, button5.centerx, button5.centery)
        draw_text('Graham Scan', 30, button6.centerx, button6.centery)
        draw_text('CCW Line Intersection', 30, button7.centerx, button7.centery)
        draw_text('Sweep Line Algorithm', 30, button8.centerx, button8.centery)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(event.pos):
                    jarvis_final.Jarvis_March()
                elif button2.collidepoint(event.pos):
                    brute_final.brute_algorithm()
                
                elif button3.collidepoint(event.pos):
                    line_final.bounded_box()
                    
                elif button4.collidepoint(event.pos):
                    quickfinal.quick_algo()
                    
                elif button5.collidepoint(event.pos):
                    chans.chans_algo()
                    
                elif button6.collidepoint(event.pos):
                    graham_final.graham()
                    
                elif button7.collidepoint(event.pos):
                    ccw.bounded_box()
          
                elif button8.collidepoint(event.pos):
                    polygon.bounded_box()
                    
            
            if event.type ==  pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.quit()
                sys.exit()     
                
                

        clock.tick(15)

# Helper function to draw text


# Start the program
main_menu()

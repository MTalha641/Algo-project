import pygame
import sys
from math import atan2
import brute_final
import jarvis_final
import graham_final
import chans
import line_final
import ccw
import polygon
import quickfinal  # Import the QuickHull module


# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)
DARK_BLUE = (36, 38, 48)
LIGHT_BLUE = (70, 130, 180)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Algo Project Menu')
clock = pygame.time.Clock()

# Load the Roboto font
pygame.font.init()
font = pygame.font.Font("Roboto-Regular.ttf", 18)

def draw_text(text, size, x, y, color=WHITE):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def draw_rounded_rect(surface, rect, color, radius=10):
    pygame.draw.rect(surface, color, rect, border_radius=radius)

def main_menu():
    running = True
    current_state = 'main'

    while running:
        screen.fill(DARK_BLUE)

        if current_state == 'main':
            draw_text('Algorithm Visualizer Project', 30, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4, WHITE)
            draw_text('Choose your desired algorithm type', 30, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3, WHITE)

            # Draw buttons for main menu
            main_button_width, main_button_height = 200, 40
            main_button_spacing = 10

            convex_hull_button = pygame.Rect((SCREEN_WIDTH - main_button_width) // 2, SCREEN_HEIGHT // 2, main_button_width, main_button_height)
            line_intersection_button = pygame.Rect((SCREEN_WIDTH - main_button_width) // 2, SCREEN_HEIGHT // 2 + main_button_height + main_button_spacing, main_button_width, main_button_height)

            draw_rounded_rect(screen, convex_hull_button, LIGHT_BLUE)
            draw_rounded_rect(screen, line_intersection_button, LIGHT_BLUE)

            draw_text('Convex Hull', 20, convex_hull_button.centerx, convex_hull_button.centery, DARK_BLUE)
            draw_text('Line Intersection', 20, line_intersection_button.centerx, line_intersection_button.centery, DARK_BLUE)

            # Check for button click event in the main menu
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if convex_hull_button.collidepoint(event.pos):
                        current_state = 'convex_hull'
                    elif line_intersection_button.collidepoint(event.pos):
                        current_state = 'line_intersection'

        elif current_state == 'convex_hull':
            # Draw buttons for convex hull algorithms
            convex_button_width, convex_button_height = 200, 40
            convex_button_spacing = 10

            button1 = pygame.Rect((SCREEN_WIDTH - convex_button_width) // 2, SCREEN_HEIGHT // 3 + 2 * (convex_button_height + convex_button_spacing), convex_button_width, convex_button_height)
            button2 = pygame.Rect((SCREEN_WIDTH - convex_button_width) // 2, SCREEN_HEIGHT // 3 + 3 * (convex_button_height + convex_button_spacing), convex_button_width, convex_button_height)
            button3 = pygame.Rect((SCREEN_WIDTH - convex_button_width) // 2, SCREEN_HEIGHT // 3 + 4 * (convex_button_height + convex_button_spacing), convex_button_width, convex_button_height)
            button4 = pygame.Rect((SCREEN_WIDTH - convex_button_width) // 2, SCREEN_HEIGHT // 3 + 5 * (convex_button_height + convex_button_spacing), convex_button_width, convex_button_height)
            quick_elimination_button = pygame.Rect((SCREEN_WIDTH - convex_button_width) // 2, SCREEN_HEIGHT // 3 + 6 * (convex_button_height + convex_button_spacing), convex_button_width, convex_button_height)

            back_button = pygame.Rect(10, 10, 100, 30)

            draw_rounded_rect(screen, button1, LIGHT_BLUE)
            draw_rounded_rect(screen, button2, LIGHT_BLUE)
            draw_rounded_rect(screen, button3, LIGHT_BLUE)
            draw_rounded_rect(screen, button4, LIGHT_BLUE)
            draw_rounded_rect(screen, quick_elimination_button, LIGHT_BLUE)
            draw_rounded_rect(screen, back_button, LIGHT_BLUE)

            draw_text('Jarvis March', 20, button1.centerx, button1.centery, DARK_BLUE)
            draw_text('Brute Force', 20, button2.centerx, button2.centery, DARK_BLUE)
            draw_text('Chan\'s Algorithm', 20, button3.centerx, button3.centery, DARK_BLUE)
            draw_text('Graham Scan', 20, button4.centerx, button4.centery, DARK_BLUE)
            draw_text('Quick Elimination', 20, quick_elimination_button.centerx, quick_elimination_button.centery, DARK_BLUE)
            draw_text('Back', 20, back_button.centerx, back_button.centery, DARK_BLUE)

            # Check for button click event in the convex hull submenu
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
                        chans.chans_algo()
                    elif button4.collidepoint(event.pos):
                        graham_final.graham()
                    elif quick_elimination_button.collidepoint(event.pos):
                        quickfinal.quick_algo()
                    elif back_button.collidepoint(event.pos):
                        current_state = 'main'

        elif current_state == 'line_intersection':
            # Draw buttons for line intersection algorithms
            line_button_width, line_button_height = 200, 40
            line_button_spacing = 10

            button5 = pygame.Rect((SCREEN_WIDTH - line_button_width) // 2, SCREEN_HEIGHT // 3 + 2 * (line_button_height + line_button_spacing), line_button_width, line_button_height)
            button6 = pygame.Rect((SCREEN_WIDTH - line_button_width) // 2, SCREEN_HEIGHT // 3 + 3 * (line_button_height + line_button_spacing), line_button_width, line_button_height)
            button7 = pygame.Rect((SCREEN_WIDTH - line_button_width) // 2, SCREEN_HEIGHT // 3 + 4 * (line_button_height + line_button_spacing), line_button_width, line_button_height)
            button8 = pygame.Rect((SCREEN_WIDTH - line_button_width) // 2, SCREEN_HEIGHT // 3 + 5 * (line_button_height + line_button_spacing), line_button_width, line_button_height)

            back_button = pygame.Rect(10, 10, 100, 30)

            draw_rounded_rect(screen, button5, LIGHT_BLUE)
            draw_rounded_rect(screen, button6, LIGHT_BLUE)
            draw_rounded_rect(screen, button7, LIGHT_BLUE)
            draw_rounded_rect(screen, button8, LIGHT_BLUE)
            draw_rounded_rect(screen, back_button, LIGHT_BLUE)

            draw_text('Bounded Box Line Intersection', 20, button5.centerx, button5.centery, DARK_BLUE)
            draw_text('CCW Line Intersection', 20, button6.centerx, button6.centery, DARK_BLUE)
            draw_text('Sweep Line Algorithm', 20, button7.centerx, button7.centery, DARK_BLUE)
            draw_text('Polygon Line Intersection', 20, button8.centerx, button8.centery, DARK_BLUE)
            draw_text('Back', 20, back_button.centerx, back_button.centery, DARK_BLUE)

            # Check for button click event in the line intersection submenu
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button5.collidepoint(event.pos):
                        line_final.bounded_box()
                    elif button6.collidepoint(event.pos):
                        ccw.bounded_box()
                    elif button7.collidepoint(event.pos):
                        polygon.bounded_box()
                    elif back_button.collidepoint(event.pos):
                        current_state = 'main'

        pygame.display.update()
        clock.tick(15)

# Start the program
main_menu()

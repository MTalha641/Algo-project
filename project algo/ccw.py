import pygame
import sys
import random
pygame.init()

WIDTH, HEIGHT = 600, 400
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
LIGHT_BLUE = (135, 206, 250)
 
def bounded_box():

    def ccw(a, b, c):
        return (c[1] - a[1]) * (b[0] - a[0]) > (b[1] - a[1]) * (c[0] - a[0])

    def do_line_segments_intersect(seg1, seg2):
        a, b = seg1
        c, d = seg2
        return ccw(a, c, d) != ccw(b, c, d) and ccw(a, b, c) != ccw(a, b, d)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Line Intersection using CCW Formula:")
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()

    line_seg1 = []
    line_seg2 = []

    def generate_random_line_segment():
        start_point = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
        end_point = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
        return [start_point, end_point]
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                line_seg1 = generate_random_line_segment()
                line_seg2 = generate_random_line_segment()
                
            elif event.type ==  pygame.KEYDOWN and event.key == pygame.K_q:
                running = False

        intersection = do_line_segments_intersect(line_seg1, line_seg2) if line_seg1 and line_seg2 else False

        screen.fill(BLACK)
        if line_seg1:
            pygame.draw.lines(screen, CYAN, False, line_seg1, 2)
        if line_seg2:
            pygame.draw.lines(screen, CYAN, False, line_seg2, 2)

        if line_seg1 and line_seg2 and intersection:
            pygame.draw.circle(screen, LIGHT_BLUE, line_seg1[0], 5)
            pygame.draw.circle(screen, LIGHT_BLUE, line_seg1[-1], 5)
            pygame.draw.circle(screen, LIGHT_BLUE, line_seg2[0], 5)
            pygame.draw.circle(screen, LIGHT_BLUE, line_seg2[-1], 5)

        intersection_text = font.render("Lines Intersect" if intersection else "Lines Do Not Intersect", True, LIGHT_BLUE)
        screen.blit(intersection_text, (WIDTH // 2 - intersection_text.get_width() // 2, HEIGHT - 50))

        if line_seg1:
            min_text1 = font.render(f"Min: {min(line_seg1[0][1], line_seg1[-1][1])}   Max: {max(line_seg1[0][1], line_seg1[-1][1])}", True, LIGHT_BLUE)
            screen.blit(min_text1, (10, 10))

        if line_seg2:
            min_text2 = font.render(f"Min: {min(line_seg2[0][1], line_seg2[-1][1])}   Max: {max(line_seg2[0][1], line_seg2[-1][1])}", True, LIGHT_BLUE)
            screen.blit(min_text2, (10, 40))

        pygame.display.flip()
        clock.tick(30)

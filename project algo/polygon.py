import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
LIGHT_BLUE = (135, 206, 250)


def do_line_segments_intersect(seg1, seg2):
    def orientation(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0
        return 1 if val > 0 else 2

    def on_segment(p, q, r):
        return (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
                q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]))

    p1, q1 = seg1
    p2, q2 = seg2

    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if (o1 != o2 and o3 != o4) or (o1 == 0 and on_segment(p1, p2, q1)) or (o2 == 0 and on_segment(p1, q2, q1)) or (
            o3 == 0 and on_segment(p2, p1, q2)) or (o4 == 0 and on_segment(p2, q1, q2)):
        return True
    return False


def sweep_line_intersection(segments):
    events = []
    for i, segment in enumerate(segments):
        events.append((segment[0], i, 'start'))
        events.append((segment[1], i, 'end'))

    events.sort()

    active_segments = set()
    for event in events:
        if event[2] == 'start':
            for active_segment in active_segments:
                if do_line_segments_intersect(segments[event[1]], segments[active_segment]):
                    return True
            active_segments.add(event[1])
        else:
            # Check if the segment is in the set before trying to remove it
            if event[1] in active_segments:
                active_segments.remove(event[1])

    return False


def bounded_box():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Line Intersection using Sweep Line Algorithm")
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()

    line_seg1 = []
    line_seg2 = []

    def generate_random_line_segment():
        start_point = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
        end_point = start_point
        while end_point == start_point:
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

        intersection = sweep_line_intersection([line_seg1, line_seg2]) if line_seg1 and line_seg2 else False

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

        intersection_text = font.render("Lines Intersect" if intersection else "Lines Do Not Intersect", True,
                                        LIGHT_BLUE)
        screen.blit(intersection_text,
                    (WIDTH // 2 - intersection_text.get_width() // 2, HEIGHT - 50))

        pygame.display.flip()
        clock.tick(30)


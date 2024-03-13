from matplotlib import pyplot as plt
from random import randint
from itertools import combinations
from math import atan2
import time

def brute_algorithm():
    def close_figure(event):
        if event.key == 'q':
            plt.close()
    def leftmost(points):
        minim = 0
        for i in range(1, len(points)):
            if points[i][0] < points[minim][0]:
                minim = i
            elif points[i][0] == points[minim][0]:
                if points[i][1] > points[minim][1]:
                    minim = i
        return minim

    def det(p1, p2, p3):
        return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

    def create_points(ct, min=0, max=50):
        return [[randint(min, max), randint(min, max)] for _ in range(ct)]

    def scatter_plot(coords, convex_hull=None, current_point=None):
        xs, ys = zip(*coords)
        plt.scatter(xs, ys,color='yellow')

        if convex_hull:
            for i in range(1, len(convex_hull) + 1):
                if i == len(convex_hull):
                    i = 0  # wrap
                c0 = convex_hull[i - 1]
                c1 = convex_hull[i]
                plt.plot((c0[0], c1[0]), (c0[1], c1[1]), 'b')

        if current_point:
            plt.scatter(current_point[0], current_point[1], color='red', marker='x')

        plt.pause(0.5)  # Adjust the pause duration as needed
        plt.clf()  # Clear the plot for the next iteration

    # def brute_force_convex_hull(points):
    #     hull = []
    #     for subset in combinations(points, 3):
    #         det_val = det(subset[0], subset[1], subset[2])
    #         if det_val > 0:
    #             hull.extend(subset)

    # # Remove duplicate points
    #     #hull = list(set(hull))
    #     hull = list(set(tuple(point)for point in hull))

    # # Sort the hull points in counterclockwise order
    #     hull.sort(key=lambda p: (atan2(p[1] - leftMost[1], p[0] - leftMost[0]), p))

    #     return hull

    def brute_force_convex_hull(points):
        hull = []
        N = len(points)
    
    # There must be at least 3 points to form a hull
        if N < 3:
            return points

        for i in range(N):
            for j in range(N):
                if i != j:
                    A, B = points[i], points[j]
                    left_side = True
                    for k in range(N):
                        if k != i and k != j:
                            C = points[k]
                        # Check if C is on the right side of AB
                            if det(A, B, C) < 0:
                                left_side = False
                                break  # C is on the right side, so AB is not an edge of the hull

                    if left_side:  # All points are on the left side of AB
                        hull.append(A)
                        hull.append(B)

    # Remove duplicates
        hull = list(set([tuple(p) for p in hull]))

    # Find the point with the lowest y-coordinate, and if there are ties, the one with the lowest x
        hull.sort(key=lambda point: (point[1], point[0]))

    # Starting from the lowest point, sort the rest of the points
    # by the angle they and the lowest point make with the x-axis
        lowest = hull[0]
        hull = hull[1:]
        hull.sort(key=lambda point: (atan2(point[1] - lowest[1], point[0] - lowest[0]), -point[1]))
        hull.insert(0, lowest)

        return hull

    


    # Generate random points
    points = create_points(10)

    # Calculate the convex hull step by step
    hull = []
    l = leftmost(points)
    leftMost = points[l]
    currentVertex = leftMost
    hull.append(currentVertex)
    nextVertex = points[1]
    index = 2
    nextIndex = -1

    while True:
        c0 = currentVertex
        c1 = nextVertex

        checking = points[index]
        c2 = checking

        crossProduct = det(currentVertex, nextVertex, checking)
        if crossProduct < 0:
            nextVertex = checking
            nextIndex = index

        # Plot the current state
        scatter_plot(points, hull, current_point=checking)

        index += 1
        if index == len(points):
            if nextVertex == leftMost:
                break
            index = 0
            hull.append(nextVertex)
            currentVertex = nextVertex
            nextVertex = leftMost
    
    
    # Plot the final convex hull
    scatter_plot(points, hull)

    # Find the convex hull using brute force
    brute_force_hull = brute_force_convex_hull(points)

    # Plot the brute force convex hull
    scatter_plot(points, convex_hull=brute_force_hull)
    plt.show()
    time.sleep(10)
    plt.close()
    
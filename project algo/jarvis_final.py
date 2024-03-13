from matplotlib import pyplot as plt
from random import randint
import time

def Jarvis_March():
    def leftmost(points):
        minim = 0
        for i in range(1, len   (points)):
            if points[i][0]    < points[minim][0]:
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

    # Generate random points
    points = create_points(10)  # Adjust the number of points as needed

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
    plt.show()
    time.sleep(10)
    plt.close()
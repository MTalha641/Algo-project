from matplotlib import pyplot as plt
from random import randint
import time

def quick_algo():
    def quick_hull(points):
        def find_side(p1, p2, p):
            return (p[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p[0] - p1[0])

        def find_distance(p1, p2, p):
            return abs((p[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p[0] - p1[0]))

        def quick_hull_recursive(left, right, points):
            if not points:
                return []

            hull = []
            farthest_point = None
            max_distance = 0

            for point in points:
                distance = find_distance(left, right, point)
                if distance > max_distance:
                    farthest_point = point
                    max_distance = distance

            if farthest_point is None:
                return []

            hull.extend(quick_hull_recursive(left, farthest_point, [p for p in points if find_side(left, farthest_point, p) > 0]))
            hull.append(farthest_point)
            hull.extend(quick_hull_recursive(farthest_point, right, [p for p in points if find_side(farthest_point, right, p) > 0]))

            return hull

        if len(points) < 3:
            return points

    # Find the leftmost and rightmost points to start the hull construction
        leftmost_index = min(range(len(points)), key=lambda i: points[i][0])
        rightmost_index = max(range(len(points)), key=lambda i: points[i][0])

        leftmost = points[leftmost_index]
        rightmost = points[rightmost_index]

    # Divide the points into two sets based on the side of the line formed by leftmost and rightmost points
        left_set = [p for p in points if find_side(leftmost, rightmost, p) > 0]
        right_set = [p for p in points if find_side(leftmost, rightmost, p) < 0]

    # Start the recursion
        convex_hull = [leftmost] + quick_hull_recursive(leftmost, rightmost, left_set) + [rightmost] + quick_hull_recursive(rightmost, leftmost, right_set)

        return convex_hull

    def create_points(ct, min=0, max=50):
        return [[randint(min, max), randint(min, max)] for _ in range(ct)]

    def scatter_plot(coords, convex_hull=None, current_points=None):
        xs, ys = zip(*coords)
        plt.scatter(xs, ys, color='yellow')

        if convex_hull:
            for i in range(1, len(convex_hull) + 1):
                if i == len(convex_hull):
                    i = 0  # wrap
                c0 = convex_hull[i - 1]
                c1 = convex_hull[i]
                plt.plot((c0[0], c1[0]), (c0[1], c1[1]), 'b')

        if current_points:
            x_curr, y_curr = zip(*current_points)
            plt.scatter(x_curr, y_curr, color='red', marker='x')

        plt.legend()
        plt.pause(1)  # Adjust the pause duration as needed
        plt.clf()  # Clear the plot for the next iteration

# Generate random points
    points = create_points(10)  # Adjust the number of points as needed

# Calculate the convex hull using QuickHull
    convex_hull = quick_hull(points)

# Plot the steps of the convex hull construction
    for i in range(len(convex_hull) - 1):
        current_point = convex_hull[i]
        remaining_points = [p for p in points if p not in convex_hull[:i + 1]]
        scatter_plot(points, convex_hull[:i + 1], [current_point])
        scatter_plot(points, convex_hull[:i + 1], [current_point] + remaining_points)

# Plot the final convex hull
    scatter_plot(points, convex_hull)
    plt.show()
    time.sleep(10)
    plt.close()

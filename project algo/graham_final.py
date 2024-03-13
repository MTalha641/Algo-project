from math import atan2
from random import randint
from matplotlib import pyplot as plt
import time

# declare global variable anchor
global anchor
def graham():
    
    def create_points(ct, min=0, max=50):
        return [[randint(min, max), randint(min, max)] for _ in range(ct)]

    def det(p1, p2, p3):
        return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

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

    def graham_scan(points, show_progress=False):
    # find the anchor point (point with the lowest y, leftmost if ties)
        global anchor  # declare anchor as global
        min_idx = None
        for i, (x, y) in enumerate(points):
            if min_idx is None or y < points[min_idx][1]:
                min_idx = i
            if y == points[min_idx][1] and x < points[min_idx][0]:
                min_idx = i
        anchor = points[min_idx]

        def polar_angle(p0, p1=None):
            global anchor  # declare anchor as global
            if p1 is None:
                p1 = anchor
            y_span = p0[1] - p1[1]
            x_span = p0[0] - p1[0]
            return atan2(y_span, x_span)

        def distance(p0, p1=None):
            global anchor  # declare anchor as global
            if p1 is None:
                p1 = anchor
            y_span = p0[1] - p1[1]
            x_span = p0[0] - p1[0]
            return y_span**2 + x_span**2

        def quicksort(a):
            if len(a) <= 1:
              return a
            smaller, equal, larger = [], [], []
            piv_ang = polar_angle(a[randint(0, len(a) - 1)])
            for pt in a:
                pt_ang = polar_angle(pt)
                if pt_ang < piv_ang:
                    smaller.append(pt)
                elif pt_ang == piv_ang:
                    equal.append(pt)
                else:
                    larger.append(pt)
            return quicksort(smaller) + sorted(equal, key=distance) + quicksort(larger)

    # execute the Graham's scan algorithm
        sorted_pts = quicksort(points)
        del sorted_pts[sorted_pts.index(anchor)]

        hull = [anchor, sorted_pts[0]]
        for s in sorted_pts[1:]:
            while det(hull[-2], hull[-1], s) <= 0:
                del hull[-1]  # backtrack
                if len(hull) < 2:
                    break
            hull.append(s)
            if show_progress:
                scatter_plot(points, hull, current_point=s)
        return hull

    # Example usage:
    # Generate random points
    points = create_points(10)

    # Calculate the convex hull using Graham's scan
    convex_hull = graham_scan(points, show_progress=True)

    # Final plot of the convex hull
    scatter_plot(points, convex_hull)
    plt.show()
    time.sleep(10)
    plt.close()
    

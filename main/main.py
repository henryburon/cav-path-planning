from lib.render_maze import *
from lib.astar import *


def main():
   global map, start, goal, path

   # capture_image()
   prepare_image()

   map = convert_to_binary()
   map = 255 - map # Invert the map so free spaces are white, obstacles are black
   plt.imshow(map, cmap='Greys', interpolation='nearest')

   start = (190, 270)
   goal = (290, 270)

   # Find the path
   path = astar(map, start, goal, heuristic)

   if path is not None:

      # Plot the path
      path_x = [point[1] for point in path]
      path_y = [point[0] for point in path]
      plt.plot(path_x, path_y, marker='x', color='red', markersize=2)

      plt.plot(start[1], start[0], marker='o', color='green', markersize=5)
      plt.plot(goal[1], goal[0], marker='o', color='blue', markersize=5)
      plt.xticks([]), plt.yticks([])

      plt.show()
   else:
      print("No path found.")

if __name__ == "__main__":
    main()
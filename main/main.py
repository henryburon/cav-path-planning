from lib.render_maze import *
from lib.astar import *


def main():
   global map, start, goal, path

   # capture_image()

   prepare_image()

   convert_to_binary()

   # Load the binary image
   map = cv2.imread('../images/binary/binary_maze.png')

   # print(map)

   # print("Image loaded as binary_maze.png")

   start = (50, 60)
   goal = (10, 5)

   # Find the path
   path = astar(map, start, goal, heuristic)

   if path is not None:
      # Print the path
      print(path)

      # Set up the initial plot
      fig, ax = plt.subplots()
      path_lines, = ax.plot([], [], marker='x', color='red', markersize=2)

      # Animation
      ani = FuncAnimation(fig, update(path_lines, path, start, goal, map), fargs=(path_lines,), frames=len(path), interval=100, repeat=False)

      plt.imshow(map, cmap='Greys', interpolation='nearest')
      plt.plot(start[1], start[0], marker='o', color='green', markersize=5)
      plt.plot(goal[1], goal[0], marker='o', color='blue', markersize=5)
      plt.xticks([]), plt.yticks([])

      plt.show()
   else:
      print("No path found.")

if __name__ == "__main__":
    main()
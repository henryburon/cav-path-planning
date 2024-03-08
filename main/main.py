from lib.render_maze import *
from lib.astar import *
from matplotlib.animation import FuncAnimation


def main():

   global map, start, goal, path

   def update(i):
    if i < len(path):
        point = path[i]
        plt.plot(point[1], point[0], marker='x', color='red', markersize=2)

   # capture_image()
   prepare_image()

   map = convert_to_binary()
   map = 255 - map # Invert the map so free spaces are white, obstacles are black
   # plt.imshow(map, cmap='Greys', interpolation='nearest')

   start = (190, 270)
   goal = (290, 270)

   # Find the path
   path = astar(map, start, goal, heuristic)

   if path is not None:
      fig = plt.figure(figsize=(10, 10))
      plt.imshow(map, cmap='Greys', interpolation='nearest')
      plt.plot(start[1], start[0], marker='o', color='green', markersize=5)
      plt.plot(goal[1], goal[0], marker='o', color='blue', markersize=5)
      plt.xticks([]), plt.yticks([])
      # ani = FuncAnimation(fig, update, frames=len(path), repeat=False)
      ani = FuncAnimation(fig, update, frames=len(path), repeat=False, interval=35)
      plt.show()
   else:
      print("No path found.")

if __name__ == "__main__":
    main()
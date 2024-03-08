from lib.render_maze import *
from lib.astar import *
from matplotlib.animation import FuncAnimation
from lib.bfs import *


def main():

   global map, start, goal, path, path2
   xplot = 10
   yplot = 10

   def update(i):
      if i < len(path):
         point = path[i]
         plt.plot(point[1], point[0], marker='x', color='red', markersize=3, linewidth=2)

   def update2(i):
      if i < len(path2):
         point = path2[i]
         plt.plot(point[1], point[0], marker='x', color='green', markersize=3, linewidth=2)

   # capture_image()
   prepare_image()

   map = convert_to_binary()
   map = 255 - map # Invert the map so free spaces are white, obstacles are black

   start, goal = request_start_and_goal(map, xplot, yplot)

   # Find the path
   path = astar(map, start, goal, heuristic)
   path2 = bfs(map, start, goal)

   if path is not None and path2 is not None:

      fig = plt.figure(figsize=(xplot, yplot))
      plt.imshow(map, cmap='Greys', interpolation='nearest')
      plt.title("A* Algorithm", fontsize=15, fontweight='bold', color='red')
      plt.plot(start[1], start[0], marker='o', color='red', markersize=7)
      plt.plot(goal[1], goal[0], marker='o', color='#39FF14', markersize=7)
      ani = FuncAnimation(fig, update, frames=len(path), repeat=False, interval=25)
      ani2 = FuncAnimation(fig, update2, frames=len(path2), repeat=False, interval=25)
      plt.figtext(0.5, 0.15, f"A* Steps: {len(path)} ", ha="center", fontsize=10, bbox={"facecolor":"white", "alpha":0.5, "pad":5})
      plt.show()
   else:
      print("No path found.")



if __name__ == "__main__":
    main()
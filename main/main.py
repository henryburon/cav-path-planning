from lib.render_maze import *
from lib.astar import *
from lib.bfs import *
from matplotlib.animation import FuncAnimation

# Main funtion to run the program
def main():
   """This function is the main function to run the program.
   """

   global map, start, goal, path, path2
   xplot = 10
   yplot = 10
   #plot the path of the astar algorithm
   def update(i):
      """This function updates the visualization of the A* algorithm.

      Args:
          i (): the current frame
      """
      if i < len(path):
        point = path[i]
        plt.plot(point[1], point[0], marker='x', color='red', markersize=3, linewidth=2)
   #plot the path of the bfs algorithm
   def update2(i):
      """_summary_

      Args:
          i (): the current frame
      """
      if i < len(path2):
         point = path2[i]
         plt.plot(point[1], point[0], marker='x', color='purple', markersize=3, linewidth=2, label='BFS' if i == 0 else "")
         
   capture_image()
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
      plt.title("A* vs. BFS Path Planning Algorithm", fontsize=15, fontweight='bold', color='purple')
      plt.plot(start[1], start[0], marker='o', color='red', markersize=7)
      plt.plot(goal[1], goal[0], marker='o', color='#39FF14', markersize=7)
      ani = FuncAnimation(fig, update, frames=len(path), repeat=False, interval=20)
      ani2 = FuncAnimation(fig, update2, frames=(len(path2)), repeat=False, interval=20)
      plt.figtext(0.5, 0.15, f"Start: {start[1], start[0]}\n Goal: {goal[1], goal[0]}", ha="center", fontsize=10, bbox={"facecolor":"white", "alpha":0.5, "pad":5})
      plt.figtext(0.4, 0.16, f"A*", ha="center", fontsize=10, bbox={"facecolor":"red", "alpha":0.5, "pad":5})
      plt.figtext(0.605, 0.16, f"BFS", ha="center", fontsize=10, bbox={"facecolor":"purple", "alpha":0.5, "pad":5})

      plt.show()
   else:
      print("No path found.")


if __name__ == "__main__":
    main()
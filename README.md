# CE 395: Connected and Autonomous Vehicles, Final Project

Authors: Henry Buron, Rahul Roy

In this project, we implemented the A* and BFS path planning algorithms via a real-world maze. 

See YouTube video here: https://youtu.be/TLJ2Jaa2NNs

First, the raw image of the maze is captured with an Intel Realsense camera.  

<img src="https://github.com/henryburon/cav-path-planning/assets/141075086/c01920c7-fbbb-40d7-99ac-8596a8f1801b" width="600">

The image is then cropped around the largest contour, which is assumed to be the maze's bounding box.  

<img src="https://github.com/henryburon/cav-path-planning/assets/141075086/f4462a9f-6b42-4e39-b564-93621df3593a" width="600">


The image is then converted into binary, and the user is asked to select a "Start" and "Goal" for the path.  

<img src="https://github.com/henryburon/cav-path-planning/assets/141075086/2d2459b9-25eb-4416-8ce9-52f6c95604a0" width="650">


Finally, both the A* and BFS path planning algorithms are implemented on the maze.  

<img src="https://github.com/henryburon/cav-path-planning/assets/141075086/2802e3e7-d5c0-4c5c-bfb8-dc3bffdb7c1c" width="650">

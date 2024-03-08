import pyrealsense2 as rs
import numpy as np
import cv2

np.set_printoptions(threshold=np.inf)

# Function to capture image from RealSense camera
def capture_image():
      
      print("Press the space bar to capture the image when ready!")

      # Configure depth and color streams
      pipeline = rs.pipeline()
      config = rs.config()

      # Get device product line for setting a supporting resolution
      pipeline_wrapper = rs.pipeline_wrapper(pipeline)
      pipeline_profile = config.resolve(pipeline_wrapper)
      device = pipeline_profile.get_device()
      device_product_line = str(device.get_info(rs.camera_info.product_line))

      found_rgb = False
      for s in device.sensors:
         if s.get_info(rs.camera_info.name) == 'RGB Camera':
            found_rgb = True
            break
      if not found_rgb:
         print("Requires camera with RGB sensor.")
         exit(0)

      if device_product_line == 'L500':
         config.enable_stream(rs.stream.color, 960, 540, rs.format.bgr8, 30)
      else:
         config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

      # Start streaming
      profile = pipeline.start(config)

      try:
         while True:
            frames = pipeline.wait_for_frames()
            color_frame = frames.get_color_frame()

            if not color_frame:
               print("No color frame received.")
               return
            
            # Convert images to numpy arrays
            color_image = np.asanyarray(color_frame.get_data())

            # Display image stream
            cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
            cv2.imshow('RealSense', color_image)

            if cv2.waitKey(1) & 0xFF == 32:
               cv2.imwrite('../images/raw/maze.png', color_image)
               print("Image saved as maze.png")
               # close the window
               cv2.destroyAllWindows()
               break
      finally:
         # Stop streaming
         pipeline.stop()

def prepare_image():
      
      print("Finding contours and cropping the image...")
      
      # Load the image
      image = cv2.imread('../images/raw/maze.png')

      # Convert to grayscale
      gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

      # Grayscale 
      gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
      
      # Find Canny edges 
      edged = cv2.Canny(gray, 30, 200) 
      cv2.waitKey(0) 
      
      # Find contours
      contours, hierarchy = cv2.findContours(edged,  
         cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 

      # find the biggest contour
      max_area = 0
      biggest_contour = None
      for contour in contours:
         area = cv2.contourArea(contour)
         if area > max_area:
            max_area = area
            biggest_contour = contour

      # crop the image above, below, left and right of the biggest contour
      x, y, w, h = cv2.boundingRect(biggest_contour)
      cropped_image = image[y:y+h, x:x+w]

      # Save the cropped image
      cv2.imwrite('../images/processed/cropped_maze.png', cropped_image)

      # draw the biggest contour
      cv2.drawContours(cropped_image, [biggest_contour], 0, (0, 255, 0), 3)

      # Save the cropped image
      cv2.imwrite('../images/processed/cropped_maze_with_contour.png', cropped_image)

      print("Image saved as cropped_maze.png")

def convert_to_binary():

   print("Converting the image to binary...")

   processed_image = cv2.imread('../images/processed/cropped_maze.png')

   _, binary_image = cv2.threshold(processed_image, 127, 255, cv2.THRESH_BINARY)

   # Convert to 1D so its compatible with the A* algorithm
   binary_image_1d = (np.any(binary_image == 255, axis=2) * 255).astype(np.uint8)

   cv2.imwrite('../images/binary/binary_maze.png', binary_image_1d)

   return binary_image_1d


      


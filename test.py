import cv2
import os
import shutil
from PIL import Image
import numpy as np

# Define a list of colors to use for replacement
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]

# Open the GIF file
with Image.open('./html/static/imgs/step.gif') as im:
    # Iterate over each frame in the GIF
    try:
        while True:
            # Save the current frame as a PNG image
            im.save(f'./stepgif/frame_{im.tell()}.png')
            # Move to the next frame
            im.seek(im.tell() + 1)
    except EOFError:
        # End of sequence
        pass

# Function to replace gray pixels with blue pixels
def replace_color(image_path, output_path, color):
    # Read the image
    img = cv2.imread(image_path)
    
    # Convert the color from RGB to BGR format
    bgr_color = (color[2], color[1], color[0])
    
    # Define lower and upper bounds for gray color
    lower_gray = np.array([40, 40, 40])
    upper_gray = np.array([150, 150, 150])
    
    # Create a mask for gray pixels
    gray_mask = cv2.inRange(img, lower_gray, upper_gray)
    
    # Replace gray pixels with specified color
    img[gray_mask > 0] = bgr_color  # Color in BGR format
    
    # Save the modified image
    cv2.imwrite(output_path, img)

# First, copy the frames from frame_0 to frame_8 to create new frames up to frame_58
for i in range(1, 6):
    for j in range(0, 9):
        src = f'./stepgif/frame_{j}.png'
        dst = f'./stepgif/frame_{i * 10 + j}.png'
        shutil.copy(src, dst)

# Apply the replacement on each set of 9 images
for i in range(0, 6):
    # Select a unique color for this set of 9 images
    selected_color = colors[i % len(colors)]
    for j in range(0, 9):
        src = f'./stepgif/frame_{i * 10 + j}.png'
        temp = f'./stepgif/temp_{i * 10 + j}.png'
        
        # Replace gray pixels with the selected color
        replace_color(src, temp, selected_color)
        
        # Remove the original file
        os.remove(src)
        
        # Rename the temporary file to original name
        os.rename(temp, src)

# Collect all the processed images
images = []
for i in range(0, 59):
    if os.path.exists(f'./stepgif/frame_{i}.png'):
        images.append(Image.open(f'./stepgif/frame_{i}.png'))

# Save the images as a new GIF
images[0].save('processed_step.gif', save_all=True, append_images=images[1:], loop=0, duration=40, disposal=2)

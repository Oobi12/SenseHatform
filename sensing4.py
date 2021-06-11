from sense_hat import SenseHat #imports the SenseHat

import time 
from PIL import Image 
import os #imports the system

#open image file
image_file= os.path.join(
os.sep,"/home","pi","Downloads","art.png") #sets the pathway
img=Image.open(image_file)

#Generate rgb values for image pixels
rgb_img = img.convert('RGB')
image_pixels = list(rgb_img.getdata())

#displays the image
sense= SenseHat() #creates the command
sense.set_rotation(r=180)
sense.set_pixels(image_pixels) 
time.sleep(3)

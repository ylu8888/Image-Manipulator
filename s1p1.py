## Yang Lu

## yang.lu.3@stonybrook.edu

## 114607667

## DUE: Monday, Oct. 30, 11:59pm. 

## IMAGE MANIPULATION - STEP ONE ##

# 1. Import the graphics library. On the line below, write a statement that tells Python
# to import everything from the graphics library.
# For an explaination of this step, you can consult p. 67 of PCS.
# Note: Make sure that graphics.py is in the same folder as this file!

from graphics import *

# 2. Create a window to display your image using the GraphWin function. As Lim notes, "GraphWin
# is a function that takes three inputs: a string and two integers. The string specifies the title
# of the window and the integers specify its dimensions" (PCS, 67). To create the window, you'll
# need to write a statement using the GraphWin function. Write the statement so the title of the
# window is specified as Blue Square - Step One and the dimensions are specified as 1280 x 720.
# Assign this object to a variable named window.
# Save the file and execute it. If you have written the statement correctly, a rectangle-shaped
# window will pop up. 
# Note: For a further explanation of the syntax for the GraphWin function, see p. 67 of PCS.

window = GraphWin('Blue Square - Step One', 1280, 720)

# 3. Create a new image to manipulate and assign it to a variable called new_img.
# In order to create a new image, use the Image function. Image is a function that creates a new
# Image object. We want to display this newly created image in the 'Blue Image - Step One' window.
# The Image function takes two inputs:
# (1) a Point object that tells Python where the image will be displayed; and
# (2) a string that specifies the filename for the image that you want to use.
# We will be creating a new image, so instead of specifying a filename as a string,
# as our second input we will specify two integers representing the width and height of our new image.
# We want to use the entire space of the window we have created. So, set the width and height
# to the same values as the window (i.e., 1280 x 720).
# Lastly, specify the Point object so that the image will fit perfectly in the window.
# Hint: You want to specify the coordinates at the center of the window.
# Save the file and execute the program.
# Note: For tips on the syntax regarding how to specify the Point object, see p. 68 of PCS.

new_img = Image(Point(640,360), 1280, 720)


# 4. Display the image in the window using the draw function. To do this, use the following syntax:

# variable.draw(location)

# In our case, our variable is new_img and the location in which we want to display the image
# is represented by the variable window. Save the file and exectute the program.
# Note: The pixels in your new image will be set to black by default. And so, when you execute the
# draw function in this case, the image in the window will still appear to be blank.

new_img.draw(window)

# 5. Using nested loops, set every pixel in our new 1280 x 720 image to the color blue.
# The blue color can be represented using the following RGB values: (0, 0, 255).
#
# To accomplish this, follow these steps:
#
# 5.1 Write a for loop that iterates through every x-coordinate from 0 to 1279.
# 5.2 Within the loop for x-coordinates, nest another for loop to iterate through every y-coordinate from 0 to 719.
# 5.3 For each combination of (x, y), set the pixel color to blue using the setPixel method of the image object
# and the color_rgb function to define the blue color.
# Execute the program. A blue rectangle should appear in your Blue Image - Step One window. 
# Your computer may take up to a minute to update the image to the blue rectangle! Be patient.
# Note: For an explanation of the setPixel function, see p. 70 of PCS; you can adapt the statement given on p. 70.

for i in range(1280):
    for j in range(720):
        new_img.setPixel(i,j,color_rgb(0,0,255))
        


# 6. Write a statement that creates a Portable Network Graphics image file (.png) with the filename blue_rectangle.
# To do this, you will need to use the save function. See page 71 of PCS for the syntax of the save function.
# Execute the program. If it is working correctly, an image of a solid blue rectangle should
# fill the Blue Image - Step One window. Additionally, a new file called blue_rectangle.png should appear in the
# same file folder that contains this .py file that you are currently editing.

new_img.save('blue_rectangle.png')

# Upload this completed .py file and your newly created .png file to Brightspace.



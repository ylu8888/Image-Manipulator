## Yang Lu

## yang.lu.3@stonybrook.edu

## 114607667

## DUE: Thursday, Nov. 2 by 11:59pm

## IMAGE MANIPULATION - STEP TWO ##

# 2.1 Import the graphics library. On the line below, write a statement that tells Python
# to import everything from the graphics library.

from graphics import *

# 2.2 Create a new 1280 x 720 window called Color Gradient - Step 2 using the GraphWin function.
# Assign this new window to the variable window2.
# Save the file and execute the program. If you have written the statement correctly, a new empty window called
# Color Gradient - Step 2 should pop up.

window2 = GraphWin('Color Gradient', 1280, 720)

# 2.3 Create a new Image object following the same syntax that you used. However, this time
# assign it to the variable blu_img; specify the Point so that the image will perfectly fit in the window;
# and, as your second input, use a string that specifies the name of the new image file that you created in step 7.
# Note: For tips on the syntax regarding how to specify the Point object, see p. 68 of PCS.
# Hint: The name of the image file that you created in step 7 should be: blue_rectangle.png. Make sure the
# blue_rectangle.png file is in the same folder as this current .py file!

blu_img = Image(Point(640,360), 'blue_rectangle.png')

# 2.4. Manipulate our blue rectangle image so that it has a vertical color gradient that transitions from pure red at
# the top to blue at the bottom. Don't forget, our image's dimensions are 1280 pixels wide and 720 pixels tall.
# The block of code below is given on page 73 of PCS. What you need to do is set the range specified in the first
# loop to 720 and set the range specified in the nested loop to 1280.

inc = 256 / 720
for x in range(720):
    R = int(255 - inc * x)
    G = 0
    B = int(inc * x)
    for y in range(1280):
        blu_img.setPixel(y,x,color_rgb(R,G,B))

# 2.5 Display the image in the window using the draw function. To do this, use the following syntax:

# variable.draw(location)

# In our case, our variable is blu_img and the location in which we want to display the image
# is represented by the variable window2. Save the file and exectute the program.
# Note: It may take up to a minute for the gradient image to appear in your Color Gradient - Step 2 window!

blu_img.draw(window2)

# 2.6 Write a statement that creates a Portable Network Graphics image file (.png) with the filename gradient_backdrop.
# To do this, you will need to use the save function. See page 71 of PCS for the syntax of the save function.
# Execute the program. If it is working correctly, a new file called blue_rectangle.png should appear in the
# same file folder that contains this .py file that you are currently editing.
 
blu_img.save('gradient_backdrop.png')


# Upload this .py file and your newly created .png file to Brightspace.

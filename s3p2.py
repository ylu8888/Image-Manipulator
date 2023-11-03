## Yang Lu

## yang.lu.3@stonybrook.edu

## 114607667

## DUE: Thursday, Nov. 2 by 11:59pm

## IMAGE MANIPULATION - STEP THREE ##

# 3.1 Import the graphics library. On the line below, write a statement that tells Python
# to import everything from the graphics library.

from graphics import *

# 3.2 Create a new 1280 x 720 window called Skater Heaven - Step 3 using the GraphWin function.
# Assign this new window to the variable window3.
# Save the file and execute the program. If you have written the statement correctly, a new empty window called
# Skater Heaven - Step 3 should pop up.

window3 = GraphWin('Skater Heaven', 1280, 720)

# 3.3 Create a new Image object. However, this time assign it to the variable background_img.
# Specify the Point so that the image will perfectly fit in the window; and, as your second input,
# use a string that specifies the name of the gradient image file that you created previously.
# Note: For tips on the syntax regarding how to specify the Point object, see p. 68 of PCS.
# Hint: The name of the image file that you created previously should be: gradient_backdrop.png. Make sure the
# gradient_backdrop.png file is in the same folder as this current .py file!

background_img = Image(Point(640,360), 'gradient_backdrop.png')

# 3.4 Create another Image object. However, this time assign it to the variable existing_img.
# We are going to manipulate existing_img so that it pulls only the figure of the skater in the image
# and imposes it on background_img. 
# Specify the Point so that the image will perfectly fit in the window; and, as your second input,
# use a string that specifies the name of the green screen skater image file that you downloaded from
# Brigthspace. The file is called skater.png. Make sure that it is in the same folder as this current
# .py file!

existing_img = Image(Point(640,360), 'skater.png')

# 3.5 Below is a function that will search through all the pixels of existing_img and analyze the R, G, B
# values of each pixel. It will grab only those pixels that are not part of the green screen backdrop. It will
# then export those pixel values onto background_img. Effectively, this should impose the skater figure
# on our gradient backdrop! All you need to do is specify the range for x (i.e., 1280) in the outer loop and
# specify the range for y (i.e., 720) in the inner loop.

threshold = 30

for x in range(1280):
    for y in range(720):
        R, G, B = existing_img.getPixel(x, y)
        
        # This checks if the pixel is not "green enough"
        if not (G > R + threshold and G > B + threshold):
            background_img.setPixel(x, y, color_rgb(R, G, B))

# 3.6 Display the new image in the window using the draw function. To do this, use the following syntax:

# variable.draw(location)

# In our case, our variable is background_img and the location in which we want to display the image
# is represented by the variable window3. Save the file and exectute the program.
# Note: It may take up to a minute for the gradient image to appear in your Skater Heaven - Step 3 window!

background_img.draw(window3)

# 3.7 Write a statement that creates a Portable Network Graphics image file (.png) with the filename skater_gradient.
# To do this, you will need to use the save function. See page 71 of PCS for the syntax of the save function.
# Execute the program. If it is working correctly, a new file called blue_rectangle.png should appear in the
# same file folder that contains this .py file that you are currently editing.

background_img.save('skater_gradient.png')

# Upload this .py file and your newly created .png file to Brightspace.

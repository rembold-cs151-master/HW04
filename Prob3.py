##################################################
# Name:
# Collaborators:
# Estimate of time spent (hr):
##################################################

import arcade

# Define any of your desired functions below








# Your functions go above here! ^^^^

def on_draw(delta_t):
    """
    Function to draw all objects to screen.

    This is where you should place all the drawing commands or functions which
    you would normally have placed between your start_render and finish_render
    commands. Remember that they are still drawn in the order you place them,
    so things written first will appear in the background of the image.

    Args:
        delta_t (float): The time between each time this function will be called for animation

    Returns:
        None
    """
    arcade.start_render()
    # Your drawing commands/functions below!


def main():
    """
    Controlling function to create window and start drawing to it.

    Here you will create your arcade window, set a background color to it if you
    desire, and then schedule the on_draw function to begin drawing.

    Args:
        None

    Returns:
        None
    """
    # Add your lines of code to create the window, set a background, and schedule the on_draw function

    # We will finish with arcade.run() to keep the window open until we close it
    arcade.run()


# Since everything above is a function, this ensures that we call the main function to kick everything off!
main()

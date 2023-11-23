import pygame

from pygame import Color, Rect
from pygame import draw
from pygame import display

SCREEN_SIZE = (500, 500)

# initialize pygame modules
pygame.init()

# get a surface for graphics display
gameDisplay = display.set_mode(SCREEN_SIZE)

# background - color of the sky
gameDisplay.fill(Color('lightblue'))

# draw a house with a roof
draw.rect(gameDisplay, Color('brown'), Rect(100, 200, 300, 200))
draw.polygon(gameDisplay, Color('black'), [(100, 200), (400, 200), (250, 50)])
# draw a cyan window
draw.rect(gameDisplay, Color('cyan'), Rect(150, 250, 50, 100))
draw.line(gameDisplay, Color('black'), (175, 250), (175, 350))
draw.line(gameDisplay, Color('black'), (150, 300), (200, 300))

# draw a red door
draw.rect(gameDisplay, Color('red'), Rect(300, 275, 80, 125))
# draw a gold doorknob
draw.circle(gameDisplay, Color('gold'), (310, 360), 5)
# draw an ellipse window
draw.ellipse(gameDisplay, Color('blue'), Rect(300, 210, 75, 50))

# draw green grass
draw.rect(gameDisplay, Color('green'), Rect(0, 400, 500, 100))

# draw a sun
draw.circle(gameDisplay, Color('orange'), (50, 50), 50)

# show the graphics on the screen
display.flip()

# Wait for user input before closing the window
input("Press enter to exit")
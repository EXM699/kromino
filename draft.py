# importing pyglet module
import pyglet
import pyglet.window.key as key

# width of window
width = 500

# height of window
height = 500

# caption i.e title of the window
title = "Geeksforgeeks"

# creating a window
window = pyglet.window.Window(width, height, title)

# text
text = "Welcome to GeeksforGeeks"

# creating label with following properties
# font = cooper
# position = 250, 150
# anchor position = center
label = pyglet.text.Label(text,
                          font_name='Cooper',
                          font_size=16,
                          x=250,
                          y=150,
                          anchor_x='center',
                          anchor_y='center')

# creating a batch
batch = pyglet.graphics.Batch()

# loading geeksforgeeks image
image = pyglet.image.load('gfg.png')

# creating sprite object
# it is instance of an image displayed on-screen
sprite = pyglet.sprite.Sprite(image, x=200, y=230)


# on draw event
@window.event
def on_draw():
    # clear the window
    window.clear()

    # draw the label
    label.draw()

    # draw the image on screen
    sprite.draw()


# key press event
@window.event
def on_key_press(symbol, modifier):
    # key "C" get press
    if symbol == key.C:
        # printing the message
        print("Key : C is pressed")


# image for icon
img = image = pyglet.resource.image("gfg.png")

# setting image as icon
window.set_icon(img)

# accessing rotation of the sprite
value = sprite.rotation = 60

# creating text from value
text = "Rotation : " + str(value)

# setting text to the label
label.text = text

# start running the application
pyglet.app.run()


#free sprite

 https://opengameart.org/

https://pixabay.com/

https://www.kenney.nl/

https://www.gameart2d.com/
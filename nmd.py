from sense_hat import SenseHat
from random import randint
color = (randint(0,255),randint(0,255),randint(0,255))
sense = SenseHat()
sense.set_rotation(180)
sense.show_message("NMD", text_colour = color)


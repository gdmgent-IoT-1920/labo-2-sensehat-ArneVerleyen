from sense_hat import SenseHat
from random import randint


color = (randint(0,255),randint(0,255),randint(0,255))
sense = SenseHat()
sense.set_rotation(180)

nmd = ["N","M","D"]

sense.show_letter(nmd, text_colour = color, scroll_speed = 1)


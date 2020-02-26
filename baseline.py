import sense_hat from SenseHat
import random from randint

sense = SenseHat()

message = "Hello, we are NMD!"
color = (randint(0,255),randint(0,255),randint(0,255))
no_color = (10,10,10)

sense.show_message(message, text_colour = no_color , back_colour = color)

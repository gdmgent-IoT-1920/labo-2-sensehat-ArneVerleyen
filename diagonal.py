from sense_hat import SenseHat
import sys

sense = SenseHat()
sense.set_imu_config(False, False, False)

def main():
	While True:
		sense.set_pixel(0,0,255,0,0)
		sense.set_pixel(1,1,255,0,0)
		sense.set_pixel(2,2,255,0,0)
		sense.set_pixel(3,3,255,0,0)
		sense.set_pixel(4,4,255,0,0)
		sense.set_pixel(5,5,255,0,0)
		sense.set_pixel(6,6,255,0,0)
		sense.set_pixel(7,7,255,0,0)



try:
	main()
except (KeyboardInterrupt, SystemExit):
	print("Programma sluiten")
finally: 
	print('Opkuisen v/d matrix')
	sense.clear()
	sys.exit(0)


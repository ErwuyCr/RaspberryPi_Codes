import sys 
import time
from picamera import PiCamera

import Adafruit_MPR121.MPR121 as MPR121

cap = MPR121.MPR121()
camera = PiCamera()

if not cap.begin():
    print('Error al iniciar, no se detecta capacitive hat!')
    sys.exit(1)

camera.rotation = 180
camera.start_preview()
frame = 1

last_touched = cap.touched()
while True:
	current_touched = cap.touched()

	for i in range(12):
		pin_bit = 1 << i
	
		if current_touched & pin_bit and not last_touched & pin_bit:
			camera.capture('/home/pi/programas/captura%04d.jpg' % frame)
			frame +=1
	last_touched = current_touched
	time.sleep(0.1)


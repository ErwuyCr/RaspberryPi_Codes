from gpiozero import MotionSensor, LED
from signal import pause
from picamera import PiCamera

pir = MotionSensor(4)
camara = PiCamera()
frame = 1

while True:
        if pir.motion_detected:
          camara.rotation = 180
          camara.start_preview()
          camara.capture('movimiento%04d.jpg' % frame)
          frame +=1
        else:
          camara.stop_preview()

pause()



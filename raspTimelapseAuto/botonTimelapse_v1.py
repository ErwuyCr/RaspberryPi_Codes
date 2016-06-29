#Programa para timelapse Automatico version 2.0
#by Bootcamp Raspberry Pi 2

from gpiozero import Button
from picamera import PiCamera
import subprocess, shlex

button = Button(2)
totalFotos = int(input("Numero de fotos a capturar: "))
foto = 1

with PiCamera() as camera:
        camera.start_preview()
        camera.rotation = 180
        #camera.image_effect = "cartoon" //opcion para poner un efecto a nuestra imagen
        button.wait_for_press()
        while foto <= totalFotos:
                camera.capture('/home/pi/fotos/captura_%03d.jpg' % foto)
                foto += 1

        camera.stop_preview()
        subprocess.call(shlex.split("avconv -r 10 -i /home/pi/fotos/captura_%03d.jpg -r 10 -vcodec libx264 -crf 20 -g 15 /home/pi/fotos/botonTimelapse.mp4"))


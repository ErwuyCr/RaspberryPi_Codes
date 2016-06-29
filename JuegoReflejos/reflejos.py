from gpiozero import Button, LED
from time import sleep
import random

led = LED(4)

jugador_1 = input('Nombre del jugador 1: ')
jugador_2 = input('Nombre del jugador 2: ')
nombres = [jugador_1, jugador_2]

boton_1 = Button(2)
boton_2 = Button(3)

time = random.uniform(5, 10)
sleep(time)
led.on()

while True:
    if boton_1.is_pressed:
        print("Gana " + nombres[0])
        break
    if boton_2.is_pressed:
        print("Gana " + nombres[1])
        break

led.off()

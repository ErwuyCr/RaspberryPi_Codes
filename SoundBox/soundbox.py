import pygame.mixer
from pygame.mixer import Sound
from gpiozero import Button
from signal import pause


pygame.mixer.init()
sonido_pins = {
	2: Sound("samples/the_force.wav"),
	3: Sound("samples/t2_no_problemo.wav"),
	4: Sound("samples/holy_caffeine.wav"),
	9 : Sound("samples/flintstones_yabba_x.wav"),
	25: Sound("samples/droopy_mad.wav")
}
botones = [Button(pin) for pin in sonido_pins]

for boton in botones:
	sound = sonido_pins[boton.pin.number]
	boton.when_pressed = sound.play

pause()


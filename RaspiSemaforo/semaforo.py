from gpiozero import LED
from time     import sleep

rojo = LED(2)
amarillo = LED(3)
verde = LED(4)
repetir = 3
num = 1 

while repetir > 0:
	rojo.on()
	sleep(2)
	rojo.off()
	i = 0	
	
	while i < 2:	
		amarillo.on()
		sleep(1)
		amarillo.off()
		sleep(1)
		i += 1
	
	verde.on()
	sleep(2) 
	verde.off()

	print("Vuelta numero %d" % num)
	repetir -= 1
	num += 1	

print "\n El Programa ha terminado"

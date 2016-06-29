from sense_hat import SenseHat
import random
import time

sensor = SenseHat()

sensor.show_message("Hazme una pregunta", scroll_speed = (0.06))

time.sleep(3)

respuestas = ["En mi opinion, si", "Es cierto", "Es decididamente asi", "Probablemente",
                    "Buen pronostico", "Todo apunta a que si", "Sin duda", " Si", "Si definitivamente",
                    "Debes confiar en ello", "Respuesta vaga, vuelve a intentarlo", "Pregunta en otro momento",
                     "Sera mejor que no te lo diga ahora", "No puedo predecirlo ahora", "Concentrate y vuelve a preguntar",
                     "No cuentes con ello", "Mi respuesta es no", "Mis fuentes me dicen que no",
                     "Las perspectivas no son buenas", "Muy dudoso"
                     ]


while True:
     x, y, z = sensor.get_accelerometer_raw().values()

     x = abs(x)
     y = abs(y)
     z = abs(z)

     if x > 2 or y > 2 or z > 2:
             sensor.show_message(random.choice(respuestas), scroll_speed = (0.06))
     else:
          sensor.clear()

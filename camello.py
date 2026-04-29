#Aquí debes introducir el código Python para recrear el Juego del Camello que encontarás en el Taller 4 de Programarcadegames
# Solo funciona por completo ejecutándolo en la terminal. En colab la pantalla no se borrará, pero sigue siendo jugable.

import time
import os
import random

def clear_output():
    os.system('clear')

#Estadísticas
millas_recorridas = 0
sed = 0
cantidad_cantimplora = 5
usos_cantimplora = 0
cansancio_camello = 0
millas_nativos = -20


# Contexto del juego
print("¡Bienvenido al Camello!")
print("Has robado un camello para atravesar el gran desierto del Mobi.")
print("¡Los nativos quieren que les devuelvas su camello y salen en persecución tuya!")
print("Tendrás que sobrevivir al desierto y correr más que los nativos.")

while True:

  # EL USUARIO ELIGE

  print("\nA. Beber de la cantimplora")
  print("B. Velocidad moderada hacia delante")
  print("C. A toda velocidad hacia delante")
  print("D. Para y descansa")
  print("E. Comprueba tu estado")
  print("Q. Salir\n")

  opcion_usuario = input("Elige una de las opciones: ").upper().strip()

  print("\n")

# CONSECUENCIAS DIRECTAS DE SU ELECCIÓN
  if opcion_usuario in ["A", "B", "C", "D", "E", "Q"]:
    clear_output()
    if opcion_usuario == "Q": # Salir
      break

    elif opcion_usuario == "A": # Beber de la cantimplora
      if cantidad_cantimplora > 0:
        cantidad_cantimplora -= 1
        usos_cantimplora += 1
        sed = 0
        print("Has bebido agua")
      else:
        print("No te queda agua en la cantimplora")

    elif opcion_usuario == "B": # Avanzar a velocidad moderada
       millas_avanzadas = random.randint(5, 12)
       millas_recorridas += millas_avanzadas
       sed += 1
       cansancio_camello += 1
       millas_nativos += random.randint(7, 14)
       print(f"Has avanzado {millas_avanzadas} millas")

    elif opcion_usuario == "C": # Avanzar a toda velocidad
       millas_avanzadas = random.randint(10, 20)
       millas_recorridas += millas_avanzadas
       sed += 1
       cansancio_camello += random.randint(1, 3)
       millas_nativos += random.randint(7, 14)
       print(f"Has avanzado {millas_avanzadas} millas")

    elif opcion_usuario == "D": # Parar y descansar
      cansancio_camello = 0
      millas_nativos += random.randint(7, 14)
      print("El camello ha conseguido descansar")

    elif opcion_usuario == "E": #Mirar estado
      print(f"Millas recorridas: {millas_recorridas}")
      print(f"Veces que has bebido de la cantimplora: {usos_cantimplora}")
  else:
    clear_output()
    print("Elige una opción válida")
    


  # CONSECUENCIAS INDIRECTAS DE SU ELECCIÓN

  if millas_recorridas >= 200:
    clear_output()
    print("¡Has ganado!")
    break

  if sed > 4:
    print("Estás sediendo")
  elif sed > 6:
    print("Has muerto.")
    break

  if cansancio_camello > 5:
    print("Tu camello está cansado")
  elif cansancio_camello > 8:
    print("Tu camello ha muerto")
    break

  if millas_nativos == millas_recorridas:
    print("Los cazadores te han capturado")
    break
  elif millas_recorridas - millas_nativos < 15:
    print("los nativos se están acercando")

  if random.randint(1, 20) == 1 and cantidad_cantimplora < 5:
    print("¡Has encontrado un oasis, tu cantimplora se ha rellenado!")
    cantidad_cantimplora =5


print("Gracias por jugar.")

# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 09:17:15 2026

@author: Adnelly Espinoza 
"""
# Juego: Piedra, Papel o Tijera 

continuar = 1

while continuar == 1:
    
  print ("Juego Piedra,Papel o Tijera")
  print ("Elige una opción")
  print ("1. Piedra")
  print ("2. Papel")
  print ("3. Tijera")

# Datos
  Usuario = int(input("Ingresa tu opción (1,2 o 3): "))

# Validación 
  if Usuario < 1 or Usuario > 3:
    print("Opción inválida. Intenta nuevamente.")
    continue

# Opción fija del Computador 
  Computador = 1
  print ("\nEl Computador eligió: Piedra")

# Comparación de opciones seleccionadas
  if Usuario == Computador: 
    print ("Empate")
  elif Usuario == 3 and Computador == 1:
    print ("Resultado: ¡Perdiste! Piedra gana a Tijera")
    
  elif Usuario == 2 and Computador == 1:
    print("Resultado: ¡Ganaste!  Papel gana a Piedra")     
    
  else:
    print("Opción inválida. Debes elegir 1, 2 o 3")
    
# Preguntar si desea seguir jugando 
  continuar = int(input("\n¿Deseas jugar otra vez? (1= Sí / 0 = No): "))    


print("\nGracias por jugar ")
    

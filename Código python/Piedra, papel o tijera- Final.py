# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 14:03:03 2026

@author: Adnelly Espinoza
"""

# Juego: Piedra, Papel o Tijera
import random

# Lista: almacena las opciones
opciones = ["Piedra", "Papel", "Tijera"]

# Tupla: reglas del juego 
reglas = (
    ("Piedra", "Tijera"),
    ("Papel", "Piedra"),
    ("Tijera", "Papel")
)
# Diccionario: relaciona número con opción
diccionario_opciones = {
    1: "Piedra",
    2: "Papel",
    3: "Tijera"
}

# Función para mostrar menú
def mostrar_menu():
    print("\nJuego Piedra, Papel o Tijera")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")

# Función para obtener opción del usuario
def obtener_opcion_usuario():
    try:
        opcion = int(input("Ingresa tu opción (1, 2 o 3): "))
        if opcion in diccionario_opciones:
            return diccionario_opciones[opcion]
        else:
            print("Opción inválida.")
            return None
    except ValueError:
        print("Debes ingresar un número.")
        return None

# Función para generar opción del computador
def obtener_opcion_computador():
    return random.choice(opciones)

# Función para determinar ganador 
def determinar_ganador(usuario, computador):
    if usuario == computador:
        return "Empate"
    
    for ganador, perdedor in reglas:
        if usuario == ganador and computador == perdedor:
            return "¡Ganaste!"
    
    return "¡Perdiste!"

# Función principal
def jugar():
    continuar = 1
    
    while continuar == 1:
        mostrar_menu()
        
        usuario = obtener_opcion_usuario()
        if usuario is None:
            continue
        
        computador = obtener_opcion_computador()
        
        print(f"\nTú elegiste: {usuario}")
        print(f"El computador eligió: {computador}")
        
        resultado = determinar_ganador(usuario, computador)
        print("Resultado:", resultado)
        
        continuar = int(input("\n¿Deseas jugar otra vez? (1= Sí / 0 = No): "))
    
    print("\nGracias por jugar ")

# Ejecutar juego
jugar()

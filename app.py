#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

import random
from flask import Flask
import cv2
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

def add_user_point():
    puntuaciones["user"] += 1

def add_maquina_point():
    puntuaciones["maquina"] += 1

def juego(choice):
    machine_choice = random.choice(choices)
    print("Machine chose", machine_choice)
    if choice == machine_choice:
        print("\n\nIt's a tie!\n\n")

    elif choice == "rock" and machine_choice == "paper":
        print("\n\nMachine wins!\n\n")
        add_maquina_point()

    elif choice == "rock" and machine_choice == "scissors":
        print("\n\nYou win!\n\n")
        add_user_point()

    elif choice == "paper" and machine_choice == "rock":
        print("\n\nYou win!\n\n")
        add_user_point()

    elif choice == "paper" and machine_choice == "scissors":
        print("\n\nMachine wins!\n\n")
        add_maquina_point()

    elif choice == "scissors" and machine_choice == "rock":
        print("\n\nMachine wins!\n\n")
        add_maquina_point()

    elif choice == "scissors" and machine_choice == "paper":
        print("\n\nYou win!\n\n")
        add_user_point()

# una funcion llamada ver_puntuaciones que muestre el resultado de las puntuaciones y que vuelva cuando cualqueira tecla se pulse
def ver_puntuaciones():
    print("\n\n\n")
    print("Puntuaciones")
    print("User:", puntuaciones["user"])
    print("Maquina:", puntuaciones["maquina"])
    input("Pulsa una tecla para continuar")
    print("\n\n\n")

puntuaciones = {"user": 0, "maquina": 0}
choices = ["rock", "paper", "scissors"]
while True:
    print("1. Jugar")
    print("2. Ver puntuaciones")
    print("3. Salir")
    option = input("Elige una opción: ")
    if option == "1":
        print("\n\n\n")
        print("\n".join(choices))
        choice = input("Enter your choice: ")
        if choice in choices:
            juego(choice)
    elif option == "2":
        ver_puntuaciones()
    elif option == "3":
        break
    else:
        print("Opción incorrecta")
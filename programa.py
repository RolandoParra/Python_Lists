import time

bienvenido = r"""
▗▄▄▖ ▗▄▄▄▖▗▄▄▄▖▗▖  ▗▖▗▖  ▗▖▗▄▄▄▖▗▖  ▗▖▗▄▄▄▖▗▄▄▄   ▗▄▖ 
▐▌ ▐▌  █  ▐▌   ▐▛▚▖▐▌▐▌  ▐▌▐▌   ▐▛▚▖▐▌  █  ▐▌  █ ▐▌ ▐▌
▐▛▀▚▖  █  ▐▛▀▀▘▐▌ ▝▜▌▐▌  ▐▌▐▛▀▀▘▐▌ ▝▜▌  █  ▐▌  █ ▐▌ ▐▌
▐▙▄▞▘▗▄█▄▖▐▙▄▄▖▐▌  ▐▌ ▝▚▞▘ ▐▙▄▄▖▐▌  ▐▌▗▄█▄▖▐▙▄▄▀ ▝▚▄▞▘
"""
pero = r"""
$$$$$$$\  $$$$$$$$\ $$$$$$$\   $$$$$$\              
$$  __$$\ $$  _____|$$  __$$\ $$  __$$\             
$$ |  $$ |$$ |      $$ |  $$ |$$ /  $$ |            
$$$$$$$  |$$$$$\    $$$$$$$  |$$ |  $$ |            
$$  ____/ $$  __|   $$  __$$< $$ |  $$ |            
$$ |      $$ |      $$ |  $$ |$$ |  $$ |            
$$ |      $$$$$$$$\ $$ |  $$ | $$$$$$  |$$\ $$\ $$\ 
\__|      \________|\__|  \__| \______/ \__|\__|\__|
"""
aunque = r"""
  _               _                                 
 | |             | |                                
 | |__   __ _ ___| |_ __ _    __ _ _   _  ___       
 | '_ \ / _` / __| __/ _` |  / _` | | | |/ _ \      
 | | | | (_| \__ \ || (_| | | (_| | |_| |  __/_ _ _ 
 |_| |_|\__,_|___/\__\__,_|  \__, |\__,_|\___(_|_|_)
                                | |                 
                                |_|                 
"""
felicidades = r"""
 ________  ________  __        ______   ______   ______  _______    ______   _______   ________   ______   __ 
|        \|        \|  \      |      \ /      \ |      \|       \  /      \ |       \ |        \ /      \ |  \
| $$$$$$$$| $$$$$$$$| $$       \$$$$$$|  $$$$$$\ \$$$$$$| $$$$$$$\|  $$$$$$\| $$$$$$$\| $$$$$$$$|  $$$$$$\| $$
| $$__    | $$__    | $$        | $$  | $$   \$$  | $$  | $$  | $$| $$__| $$| $$  | $$| $$__    | $$___\$$| $$
| $$  \   | $$  \   | $$        | $$  | $$        | $$  | $$  | $$| $$    $$| $$  | $$| $$  \    \$$    \ | $$
| $$$$$   | $$$$$   | $$        | $$  | $$   __   | $$  | $$  | $$| $$$$$$$$| $$  | $$| $$$$$    _\$$$$$$\ \$$
| $$      | $$_____ | $$_____  _| $$_ | $$__/  \ _| $$_ | $$__/ $$| $$  | $$| $$__/ $$| $$_____ |  \__| $$ __ 
| $$      | $$     \| $$     \|   $$ \ \$$    $$|   $$ \| $$    $$| $$  | $$| $$    $$| $$     \ \$$    $$|  \
 \$$       \$$$$$$$$ \$$$$$$$$ \$$$$$$  \$$$$$$  \$$$$$$ \$$$$$$$  \$$   \$$ \$$$$$$$  \$$$$$$$$  \$$$$$$  \$$
"""

print(bienvenido)
print()
prnt()


def menu():
  print("Que quieres hacer?")
  print()
  print("1. Crear una lista de amigos")
  print("2. lista de edades y gustos musicales")
  print("3. Salir")
  elección = input("Elección: ")
  if elección == "1":
    lista_de_amigos()
  elif elección == "2":
    lista_de_edades_y_gustos_musicales()
  elif elección == "3":
    print("Adios!")
    time.sleep(1)
    exit()
  else:
    print("Opción no válida, intenta de nuevo")
    time.sleep(1)
    menu()

def lista_de_amigos():
  print()
  print()
  print("Ingresa el nombre de tus 3 mejores amigos")
  time.sleep(0.3)
  n1 = input("Amigo 1: ")
  time.sleep(0.3)
  n2 = input("Amigo 2: ")
  time.sleep(0.3)
  n3 = input("Amigo 3: ")
  lista_amigos = [n1, n2, n3]

  print()
  time.sleep(2)
  print(pero)
  print()
  time.sleep(1)
  print("Un nuevo amigo se a unido al grupo, ingresa su nombre")
  time.sleep(0.3)
  nuevo_amigo = input("Nuevo amigo: ")
  lista_amigos.append(nuevo_amigo)

  print()
  time.sleep(2)
  print(aunque)
  print()

  print("Te peleaste con tu segundo amigo y salió de el grupo")
  time.sleep(0.3) 
  lista_amigos.remove(n2)

  time.sleep(2)
  print(felicidades)
  time.sleep(0.3)
  print()
  print("tu lista de amigos ahora es...")
  time.sleep(0.5)
  print(lista_amigos)
  input()


def lista_de_edades_y_gustos_musicales():
  print()
  print()
  print("Ingresa las edades de 5 compañeros de clase")
  time.sleep(0.3)
  e1 = input("Compañero 1: ")
  time.sleep(0.3)
  e2 = input("Compañero 2: ")
  time.sleep(0.3)
  e3 = input("Compañero 3: ")
  time.sleep(0.3)
  e4 = input("Compañero 4: ")
  time.sleep(0.3)
  e5 = input("Compañero 5: ")
  lista_edades = [e1, e2, e3, e4, e5]

  print()
  print()
  print("Ahora ingresa los gustos musicales de esos mismos compañeros")
  time.sleep(0.3)
  g1 = input("Compañero 1: ")
  time.sleep(0.3)
  g2 = input("Compañero 2: ")
  time.sleep(0.3)
  g3 = input("Compañero 3: ")
  time.sleep(0.3)
  g4 = input("Compañero 4: ")
  time.sleep(0.3)
  g5 = input("Compañero 5: ")
  lista_gustos = [g1, g2, g3, g4, g5]

  print()
  print()
  print("Veamos quien es mayor de 15 años...")
  time.sleep(3)
  for i in range(len(lista_edades)):
    if int(lista_edades[i]) > 15:
      print(f"El compañero {i+1} es mayor de 15 años")
  
  print()
  print("Veamos quien le gusta el rock...")
  time.sleep(3)
  for i in range(len(lista_gustos)):
    if lista_gustos[i].lower() == "rock":
      print(f"Al compañero {i+1} le gusta el rock")
lista_equipos = []
puntos = []
goles_favor = []
numequipos = 0


def fixture_partidos(lista_equipos, numequipos):
    posicion = 0
    posicion1 = 1
    numP = 1
    print("El fixture es")
    while True:
        print()
        print("partido", numP)
        print(lista_equipos[posicion], "vs", lista_equipos[posicion1])
        print()
        goles_local = int(input(f"Goles de {lista_equipos[posicion]}: "))
        goles_visitante = int(input(f"Goles de {lista_equipos[posicion1]}: "))
        if goles_local > goles_visitante:
            puntos[posicion] += 3
        elif goles_local < goles_visitante:
            puntos[posicion1] += 3
        else:
            puntos[posicion] += 1
            puntos[posicion1] += 1
        goles_favor[posicion] += goles_local
        goles_favor[posicion1] += goles_visitante
        posicion = posicion + 2
        posicion1 = posicion1 + 2
        numP = numP + 1
        if numP == numequipos/2 + 1:
            break

def mostrar_tabla(lista_equipos, puntos, goles_favor):
    print("\n-------------------------------------------")
    print("EQUIPO\t\t\tPUNTOS\t\tGOLES")
    print("-------------------------------------------")
    for i in range(len(lista_equipos)):
        print(f"{lista_equipos[i]}\t\t{puntos[i]}\t\t{goles_favor[i]}")
    print("-------------------------------------------\n")

ejecutando_menu = True
while ejecutando_menu:
    print("--- MENU PRINCIPAL - LIGA DE FÚTBOL ---")
    print("1. Registrar Equipos")
    print("2. Mostrar Fixture de Partidos")
    print("3. Mostrar Tabla de Posiciones")
    print("4. Salir")
    opcion = input("Seleccione una opción (1-4): ")
    if opcion == "1":
        entrada_valida = False
        while not entrada_valida:
            print("Ingrese un numero par de equipos (entre 2 y 20):")
            entrada_usuario = input()
            if entrada_usuario.isdigit():
                numequipos = int(entrada_usuario)
                if numequipos >= 2 and numequipos <= 20 and numequipos % 2 == 0:
                    entrada_valida = True
                else:
                    print("Error: La cantidad de equipos debe ser un número PAR entre 2 y 20.\n")
            else:
                print("Error: Por favor, ingrese un número entero válido (no letras ni símbolos).\n")
        lista_equipos.clear()
        puntos = [0] * numequipos
        goles_favor = [0] * numequipos
        for i in range(numequipos):
            print("equipo", i + 1)
            lista_equipos.append(input("Escriba el nombre: "))
        print("Equipos registrados:", lista_equipos)
    elif opcion == "2":
        if len(lista_equipos) == 0:
            print("Error: No hay equipos registrados todavía. Por favor, use la Opción 1 primero.")
        else:
            print("--- Fixture de La Liga ---")
            fixture_partidos(lista_equipos, numequipos)
    elif opcion == "3":
        if len(lista_equipos) == 0:
            print("Error: No hay equipos registrados todavía. No se puede mostrar la tabla")
        else:
            print("--- Tabla de Posiciones ---")
            mostrar_tabla(lista_equipos, puntos, goles_favor)
    elif opcion == "4":
        print("Saliendo del programa...")
        ejecutando_menu = False

lista_equipos = []
numequipos = 0
tablaequipos = lista_equipos


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
        posicion = posicion + 2
        posicion1 = posicion1 + 2
        numP = numP + 1
        if numP == numequipos/2 + 1:
            break


ejecutando_menu = True
while ejecutando_menu:
    print("--- MENU PRINCIPAL - LIGA DE FÚTBOL ---")
    print("1. Registrar Equipos")
    print("2. Mostrar Fixture de Partidos")
    print("3. Salir")
    opcion = input("Seleccione una opción (1-3): ")
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
        print("Saliendo del programa...")
        ejecutando_menu = False

lista_equipos = []
puntos = []
goles_favor = []
numequipos = 0

print("Este es el archivo nuevo")


def fixture_partidos(lista_equipos, numequipos):
    equipos_rotacion = list(lista_equipos)
    num_fechas = numequipos - 1
    part_por_fecha = numequipos // 2
    numP = 1
    for fecha in range(num_fechas):
        print(f"\n--- Fecha {fecha + 1} ---")
        for i in range(part_por_fecha):
            local = equipos_rotacion[i]
            visitante = equipos_rotacion[numequipos - 1 - i]
            idx_local = lista_equipos.index(local)
            idx_visitante = lista_equipos.index(visitante)
            print(f"Partido {numP}: {local} vs {visitante}")
            goles_local = int(input(f"Goles de {local}: "))
            goles_visitante = int(input(f"Goles de {visitante}: "))
            if goles_local > goles_visitante:
                puntos[idx_local] += 3
            elif goles_local < goles_visitante:
                puntos[idx_visitante] += 3
            else:
                puntos[idx_local] += 1
                puntos[idx_visitante] += 1
            goles_favor[idx_local] += goles_local
            goles_favor[idx_visitante] += goles_visitante
            numP += 1
            print()
        ultimo = equipos_rotacion.pop()
        equipos_rotacion.insert(1, ultimo)

def mostrar_tabla(lista_equipos, puntos, goles_favor):
    print("\n-------------------------------------------")
    print(f"| {'EQUIPO':<15} | {'PUNTOS':>6} | {'GOLES':>6} |")
    print("-------------------------------------------")
    for i in range(len(lista_equipos)):
        print(f"| {lista_equipos[i]:<15} | {puntos[i]:>6} | {goles_favor[i]:>6} |")
    print("-------------------------------------------\n")


def mostrar_campeon(lista_equipos, puntos, goles_favor):
    idx_camp = 0
    max_puntos = puntos[0]
    max_goles = goles_favor[0]
    for i in range(1, len(lista_equipos)):
        if puntos[i] > max_puntos:
            max_puntos = puntos[i]
            max_goles = goles_favor[i]
            idx_camp = i
        elif puntos[i] == max_puntos and goles_favor[i] > max_goles:
            max_goles = goles_favor[i]
            idx_camp = i
    campeon = lista_equipos[idx_camp]
    print("\n=========================================================")
    print(f" ¡EL CAMPEÓN DEL TORNEO ES: {campeon.upper()}! ")
    print(f" Estadísticas finales: {max_puntos} Puntos | {max_goles} Goles a Favor")
    print("=========================================================\n")


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
            print("--- Campeón del Torneo ---")
            mostrar_campeon(lista_equipos, puntos, goles_favor)   
    elif opcion == "4":
        print("Saliendo del programa...")
        ejecutando_menu = False
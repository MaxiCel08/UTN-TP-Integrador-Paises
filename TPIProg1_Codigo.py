import csv

archivo = "TPIntegradorProg1_Paises.csv"

def validar_int(string = "Input: "): #validar entero con un bucle
    while True:
        variable = input(f"{string}")
        if variable.isdigit():
            variable = int(variable)
            return variable
        else:
            print("\nNúmero entero invalido.\n")
            continue

def validar_alpha(string = "Input: "): #validar string con un bucle
    while True:
        variable = input(f"{string}")
        if variable.isalpha():
            variable = str(variable)
            return variable
        else:
            print("\nValor string invalido.\n")
            continue

def bucle_seleccion_continentes(): #validar seleccion de continentes con un bucle
    while True:
        seleccion2 = validar_int("1. Africa"
        "\n2. America"
        "\n3. Asia"
        "\n4. Europa"
        "\n5. Australia"
        "\n6. Antartica"
        "\n\nSeleccione un continente: ")

        if seleccion2 < 1 or seleccion2 > 6:
            print("\nSelección fuera del rango.\n")
            continue

        if seleccion2 == 1:
            continente = "Africa"
            return continente
        if seleccion2 == 2:
            continente = "America"
            return continente
        if seleccion2 == 3:
            continente = "Asia"
            return continente
        if seleccion2 == 4:
            continente = "Europa"
            return continente
        if seleccion2 == 5:
            continente = "Australia"
            return continente
        if seleccion2 == 6:
            continente = "Antartica"
            return continente

def bucle_seleccion_opcion1():
    while True:
        seleccion = validar_int("\n1. Filtrar por continente"
                                "\n2. Filtrar por rango de población"
                                "\n3. Filtrar por rango de superficie"
                                "\n\nSeleccione una opción: ")

        if seleccion < 1 or seleccion > 3:
            print("\nSelección fuera del rango.\n")
            continue
        else:
            return seleccion

def bucle_seleccion_opcion6():
    while True:
        seleccion = validar_int("\n1. Ver mayor y menor indice de población"
                                "\n2. Ver promedio de superficie"
                                "\n3. Ver cantidad de paises por continente"
                                "\n\nSeleccione una opción: ")

        if seleccion < 1 or seleccion > 3:
            print("\nSelección fuera del rango.\n")
            continue
        else:
            return seleccion

def bucle_seleccion_orden():
    while True:
        seleccion = validar_int("\n1. Mostrar nombres ordenados alfabeticamente"
                                "\n2. Mostrar poblacion ordenada de menor a mayor"
                                "\n3. Mostrar superficie de menor a mayor o viceversa"
                                "\n\nSeleccione una opción: ")
        
        if seleccion < 1 or seleccion > 3:
            print("\nSelección fuera del rango.\n")
            continue
        else:
            return seleccion
            
def bucle_seleccion_superficie_ascendiente_o_descendiente():
    while True:
        seleccion = validar_int("\n1. Menor a mayor"
                                "\n2. Mayor a menor"
                                "\n\nSeleccione una opción: ")
        
        if seleccion < 1 or seleccion > 2:
            print("\nSelección fuera del rango.\n")
            continue
        else:
            return seleccion


#Africa, America, Asia, Europa, Australia, Antartica

while True: #mostrar menu de opciones
    seleccion_menu = validar_int( "1. Añadir un nuevo país"
                                "\n2. Actualizar un país"
                                "\n3. Buscar país por nombre"
                                "\n4. Filtrar información"
                                "\n5. Ordenar información"
                                "\n6. Mostrar estadisticas"
                                "\n7. Salir"
                                "\n\nSeleccione una opción: ")

    if seleccion_menu == 1:
        pais_repetido = False
        with open(archivo, "r", newline="", encoding="utf-8") as paises_csv:
            lector = list(csv.reader(paises_csv))

            nuevo_pais_nombre = validar_alpha("\nIngrese el nombre de un nuevo país: ").capitalize()

            for linea in lector:
                if linea[0] == nuevo_pais_nombre:
                    pais_repetido = True
                    break

            if pais_repetido == True:
                print("\nEse país ya existe!\n")
            else:
                    nuevo_pais_poblacion = validar_int("\nIngrese la población: ")
                    nuevo_pais_superficie = validar_int("\nIngrese la superficie del país (en metros cuadrados): ")
                    nuevo_pais_continente = bucle_seleccion_continentes()

                    with open(archivo, "a", newline="", encoding="utf-8") as paises_escritura_csv:
                        escritor = csv.writer(paises_escritura_csv)
                        
                        escritor.writerow([
                            nuevo_pais_nombre,
                            nuevo_pais_poblacion,
                            nuevo_pais_superficie,
                            nuevo_pais_continente
                        ])

    if seleccion_menu == 2:
        with open(archivo, "r", newline="", encoding="utf-8") as paises_csv:

            filas_lista = list(csv.reader(paises_csv))

            nombre_a_buscar = validar_alpha("Ingrese el nombre de un país: ")

            encontrado = False

            for indice, fila in enumerate(filas_lista):
                if fila[0] == nombre_a_buscar:

                    nuevo_pais_nombre = validar_alpha("Ingrese el nombre de un nuevo país: ").capitalize()
                    nuevo_pais_poblacion = validar_int("Ingrese la población: ")
                    nuevo_pais_superficie = validar_int("Ingrese la superficie del país (en metros cuadrados): ")
                    nuevo_pais_continente = bucle_seleccion_continentes()

                    filas_lista[indice] = [
                        nuevo_pais_nombre,
                        nuevo_pais_poblacion,
                        nuevo_pais_superficie,
                        nuevo_pais_continente
                    ]

                    with open(archivo, "w", newline="", encoding="utf-8") as paises_csv:
                        escritor = csv.writer(paises_csv)
                        escritor.writerows(filas_lista)

                    encontrado = True
                    break

            if encontrado == False:
                print("No se encontró ese país.")
    
    if seleccion_menu == 3:
        with open(archivo, "r", encoding="utf-8") as paises_csv:
        
            nombre_a_buscar = validar_alpha("Ingrese el nombre de un país: ").capitalize()

            lector = csv.DictReader(paises_csv)

            encontrado = False

            for fila in lector:
                if fila["nombre"] == nombre_a_buscar:
                    print(f"\nNombre: {fila["nombre"]}"
                        f"\nPoblación: {fila["poblacion"]}"
                        f"\nSuperficie: {fila["superficie"]}"
                        f"\nContinente: {fila["continente"]}\n")
                    encontrado = True
                    break
            
            if encontrado == False:
                print("\nNo se encontró ese país.\n")

    if seleccion_menu == 4: #filtrar información
        seleccion = bucle_seleccion_opcion1()

        if seleccion == 1: #mostrar pais y continente
            with open(archivo, "r", newline="", encoding="utf-8") as paises_csv:

                lector = csv.reader(paises_csv)

                next(lector)
                print("\nPAIS - CONTINENTE\n")

                for linea in lector:
                    print(linea[0], "-", linea[3])
                print()
        
        if seleccion == 2: #filtrar población por rango
            
            poblacion_cantidad_minima = validar_int("Ingrese una cantidad minima de población: ")
            poblacion_cantidad_maxima = validar_int("Ingrese una cantidad maxima de población: ")

            with open(archivo, "r", newline="", encoding="utf-8") as paises_csv:
                lector = csv.reader(paises_csv)
                next(lector)

                print()
                print("PAIS - POBLACIÓN")
                print()
                for linea in lector:
                    if int(linea[1]) > poblacion_cantidad_minima and int(linea[1]) < poblacion_cantidad_maxima:
                        print(linea[0], "-", linea[1])
                print()

        if seleccion == 3: #filtrar superficie por rango
                    
            superficie_cantidad_minima = validar_int("Ingrese una cantidad minima de superficie: ")
            superficie_cantidad_maxima = validar_int("Ingrese una cantidad maxima de superficie: ")

            with open(archivo, "r", newline="", encoding="utf-8") as paises_csv:
                lector = csv.reader(paises_csv)
                next(lector)

                print()
                print("PAIS - SUPERFICIE")
                print()
                for linea in lector:
                    if int(linea[2]) > superficie_cantidad_minima and int(linea[2]) < superficie_cantidad_maxima:
                        print(linea[0], "-", linea[2])
                print()
        
    if seleccion_menu == 5: #ordenar información
        with open(archivo, "r", newline="", encoding="utf-8") as paises_csv:

            paises = csv.reader(paises_csv)

            next(paises)

            seleccion = bucle_seleccion_orden()

            if seleccion == 1:
                paises_nombres_ordenados = []

                for linea in paises:
                    paises_nombres_ordenados.append(linea[0])
                print()
                
                paises_nombres_ordenados = sorted(paises_nombres_ordenados)

                for linea in paises_nombres_ordenados:
                    print(linea)
                print()
            
            if seleccion == 2:
                poblacion_ordenada = []

                for linea in paises:
                    poblacion_ordenada.append(int(linea[1]))
                print()

                poblacion_ordenada = sorted(poblacion_ordenada)

                for dato in poblacion_ordenada:
                    print(dato)
                print()
            
            if seleccion == 3:
                seleccion2 = bucle_seleccion_superficie_ascendiente_o_descendiente()

                if seleccion2 == 1:
                    superficie_lista_ascendiente = []

                    for linea in paises:
                        superficie_lista_ascendiente.append(int(linea[2]))
                    print()

                    superficie_lista_ascendiente = sorted(superficie_lista_ascendiente)

                    for dato in superficie_lista_ascendiente:
                        print(dato)
                    print()
                
                if seleccion2 == 2:
                    superficie_lista_descendiente = []

                    for linea in paises:
                        superficie_lista_descendiente.append(int(linea[2]))
                    print()

                    superficie_lista_descendiente = sorted(superficie_lista_descendiente)

                    for i in range(len(superficie_lista_descendiente) - 1, -1, -1):
                        print(superficie_lista_descendiente[i])
                    print()

    if seleccion_menu == 6:
        with open(archivo, "r", newline="", encoding="utf-8") as paises_csv:

            paises_lector = csv.reader(paises_csv)

            next(paises_lector)

            seleccion = bucle_seleccion_opcion6()

            if seleccion == 1:

                poblacion_datos = {}

                for linea in paises_lector:
                    poblacion_datos[linea[0]] = int(linea[1])

                print()
                print(f"El país con más población tiene un indice de {max(poblacion_datos.values())} habitantes.")
                print()
                print(f"El país con menos población tiene un indice de {min(poblacion_datos.values())} habitantes.")
                print()

            if seleccion == 2:
                lista_superficies = []

                for linea in paises_lector:
                    lista_superficies.append(int(linea[2]))

                promedio = sum(lista_superficies) // len(lista_superficies)

                print()
                print(f"El promedio de superficie es {promedio}.")
                print()
            
            if seleccion == 3:
                continentes = {"America":0, "Antartica":0, "Asia":0, "Europa":0, "Africa":0, "Australia":0}

                for linea in paises_lector:
                    continente = linea[3]

                    if continente in continentes:
                        continentes[continente] += 1
                    else:
                        continentes[continente] = 1

                print(continentes)

                print()
                print(f"Hay {continentes["America"]} paises que residen en America.")
                print(f"Hay {continentes["Antartica"]} paises que residen en Antartica.")
                print(f"Hay {continentes["Asia"]} paises que residen en Asia.")
                print(f"Hay {continentes["Europa"]} paises que residen en Europa.")
                print(f"Hay {continentes["Africa"]} paises que residen en Africa.")
                print(f"Hay {continentes["Australia"]} paises que residen en Australia.")
                print()

    if seleccion_menu == 7: #terminar programa
        break
    
    if seleccion_menu == 8: #mostrar el archivo completo
        with open(archivo, "r", encoding="utf-8") as paises_csv:
        
            lector = csv.DictReader(paises_csv)

            print()
            for linea in lector:
                print(f"{linea["nombre"]}", linea["poblacion"], linea["superficie"], linea["continente"])
            print()
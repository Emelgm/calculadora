# Proyecto de funciones de circuitos y onda

opcion = ''

# ciclo general
while opcion != 'x':
    print('*'*45)
    print("""
                MENU

        [A] - Cálculo de circuitos
        [B] - Cálculo de una onda

        [X] - FINALIZAR
    """)
    print('*'*45)

    opcion = input("Seleccione la opción a calcular: ")

    # bloque de circuitos
    if opcion == 'a':
        opcion_2 = input("\nCalcular circuitos\n[A] - En serie\n[B] - En paralelo\n: ")

        # circuito en serie
        if opcion_2 == 'a':
            print("\nCircuitos en serie")
            result = 0
            cantidad = int(input("\nCantidad de R a calcular: "))
            for i in range(1, cantidad + 1):
                r = float(input(f"Valor de R{i} en kΩ: "))
                result += r
            print(f"\nLa R resultante es: {round(result,2)} kΩ")
        # cricuito en paralelo
        elif opcion_2 == 'b':
            print("\nCircuitos en paralelo")
            result = 0
            cantidad = int(input("\nCantidad de R a calcular: "))
            for i in range(1, cantidad + 1):
                r = float(input(f"Valor de R{i} en kΩ: "))
                result = result+(1/r)
            rtotal = 1/result
            print(f"\nLa R resultante es: {round(rtotal,2)} kΩ")
        else:
            print("\n¡¡ OPCIÓN EQUIVOCADA !!")
            opcion = 'a'
        # continuar con otra opción o salir del programa
        restart = input("\n¿Desea continuar?\n[S] SÍ - [N] NO\n: ")
        if restart == 's':
            continue
        elif restart == 'n':
            print("\n")
            print('*'*18)
            print(" FIN DEL PROGRAMA")
            print('*'*18)
            opcion = 'x'
        else:
            print("\n¡¡ OPCIÓN EQUIVOCADA !!")
    # bloque de onda
    elif opcion == 'b':
        print("\nCalcular parámetros de una onda")
        param = input("[A] - Longitud\n[B] - Frecuencia\n[C] - Velocidad\n:")
        if param == 'a':
            print("\nFórmula ----> λ = v / f\n")
            velocidad = float(input("Valor de V m/s: "))
            frecuencia = float(input("Valor de F en kHz: "))
            longitud = velocidad/frecuencia
            print(f"\nLa longitud de onda es λ = {round(longitud,2)}")
        elif param == 'b':
            print("\nFórmula ----> f = v / λ\n")
            velocidad = float(input("Valor de V m/s: "))
            longitud = float(input("Valor de λ en m: "))
            frecuencia = velocidad/longitud
            print(f"\nLa frecuencia de la onda es f = {round(frecuencia,2)}")
        elif param == 'c':
            print("\nFórmula ----> v = λ * f\n")
            frecuencia = float(input("Valor de F en kHz: "))
            longitud = float(input("Valor de λ en m: "))
            velocidad = frecuencia*longitud
            print(f"\nLa frecuencia de la onda es f = {round(velocidad,2)}")
        # continuar con otra opción o salir del programa
        restart = input("\n¿Desea continuar?\n[S] SÍ - [N] NO\n: ")
        if restart == 's':
            continue
        elif restart == 'n':
            print("\n")
            print('*'*18)
            print(" FIN DEL PROGRAMA")
            print('*'*18)
            opcion = 'x'
        else:
            print("\n¡¡ OPCIÓN EQUIVOCADA !!")
    # salir del programa
    elif opcion == 'x':
        print("\n")
        print('*'*18)
        print(" FIN DEL PROGRAMA")
        print('*'*18)
        opcion = 'x'
    else:
        print("\n¡¡ OPCIÓN EQUIVOCADA !!")


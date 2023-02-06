# Proyecto de funciones de circuitos y onda

opcion = ''

# ciclo general
while opcion != 'x' or opcion != 'X':
    print('*'*45)
    print("""
                MENU

        [A] - Cálculo de resistencia de circuitos
        [B] - Ley de Ohm
        [C] - Cálculo de una onda

        [X] - FINALIZAR
    """)
    print('*'*45)

    opcion = input("Seleccione la opción a calcular: ")

    # bloque de circuitos
    if opcion == 'a' or opcion == 'A':
        opcion_2 = input("\nCalcular circuitos\n[A] - En serie\n[B] - En paralelo\n: ")

        # circuito en serie
        if opcion_2 == 'a' or opcion_2 == 'A':
            print("\nCircuitos en serie")
            result = 0
            cantidad = int(input("\nCantidad de Resistencias a calcular: "))
            for i in range(1, cantidad + 1):
                r = float(input(f"Valor de Resistencia {i} en kΩ: "))
                result += r
            print(f"\nLa Resistencia resultante es: {round(result,2)} kΩ")
        # cricuito en paralelo
        elif opcion_2 == 'b' or opcion_2 == 'B':
            print("\nCircuitos en paralelo")
            result = 0
            cantidad = int(input("\nCantidad de Resistencias a calcular: "))
            for i in range(1, cantidad + 1):
                r = float(input(f"Valor de Resistencia {i} en kΩ: "))
                result = result+(1/r)
            rtotal = 1/result
            print(f"\nLa Resistencia resultante es: {round(rtotal,2)} kΩ")
        else:
            print("\n¡¡ OPCIÓN EQUIVOCADA !!")
            opcion = 'a'
        # continuar con otra opción o salir del programa
        restart = input("\n¿Desea continuar?\n[S] SÍ - [N] NO\n: ")
        if restart == 's' or restart == 'S':
            continue
        elif restart == 'n' or restart == 'N':
            print("\n")
            print('*'*18)
            print(" FIN DEL PROGRAMA")
            print('*'*18)
            #opcion = 'x'
            break
        else:
            print("\n¡¡ OPCIÓN EQUIVOCADA !!")
    # bloque ley de ohm
    elif opcion == 'b' or opcion == 'B':
        print("\nLey de Ohm")
        omh = input("[A] - Voltaje\n[B] - Corriente\n[C] - Resistencia\n: ")
        if omh == 'a' or omh == 'A':
            print("\nVoltaje ----> V = I * R")
            corriente = float(input("Valor de Corriente en mA: "))
            resistencia = float(input("Valor de Resistencia en kΩ: "))
            voltaje = corriente * resistencia
            print(f"Voltaje = {round(voltaje,3)}")
        elif omh == 'b' or omh == 'B':
            print("\nCorriente ---> I = V / R")
            voltaje = float(input("Valor de Voltaje: "))
            resistencia = float(input("Valor de Resistencia en kΩ: "))
            corriente = voltaje / resistencia
            print(f"Corriente = {round(corriente, 3)} mA")
        elif omh == 'c' or omh == 'C':
            print("\nResistencia ----> R = V / I")
            voltaje = float(input("Valor de Voltaje: "))
            corriente = float(input("Valor de Corriente en mA: "))
            resistencia = voltaje / corriente
            print(f"Resistencia = {round(resistencia, 2)} kΩ")
        else:
            print("\n¡¡ OPCIÓN EQUIVOCADA !!")
        # continuar con otra opción o salir del programa
        restart = input("\n¿Desea continuar?\n[S] SÍ - [N] NO\n: ")
        if restart == 's' or restart == 'S':
            continue
        elif restart == 'n' or restart == 'N':
            print("\n")
            print('*'*18)
            print(" FIN DEL PROGRAMA")
            print('*'*18)
            break
        else:
            print("\n¡¡ OPCIÓN EQUIVOCADA !!")
    # bloque de onda
    elif opcion == 'c' or opcion == 'C':
        print("\nCalcular parámetros de una onda")
        param = input("[A] - Longitud\n[B] - Frecuencia\n[C] - Velocidad\n:")
        if param == 'a' or param == 'A':
            print("\nFórmula ----> λ = v / f\n")
            velocidad = float(input("Valor de Velocidad m/s: "))
            frecuencia = float(input("Valor de Frecuencia en Hz: "))
            longitud = velocidad/frecuencia
            print(f"\nLa longitud de onda es λ = {round(longitud,2)} m")
        elif param == 'b' or param == 'B':
            print("\nFórmula ----> f = v / λ\n")
            velocidad = float(input("Valor de Velocidad m/s: "))
            longitud = float(input("Valor de Longitud (λ) en m: "))
            frecuencia = velocidad/longitud
            print(f"\nLa frecuencia de la onda es f = {round(frecuencia,2)} Hz")
        elif param == 'c' or param == 'C':
            print("\nFórmula ----> v = λ * f\n")
            frecuencia = float(input("Valor de FrecuenciaF en Hz: "))
            longitud = float(input("Valor de Longitud (λ) en m: "))
            velocidad = frecuencia*longitud
            print(f"\nLa velocidad de la onda es v = {round(velocidad,2)} m/s")
        else:
            print("\n¡¡ OPCIÓN EQUIVOCADA !!")
        # continuar con otra opción o salir del programa
        restart = input("\n¿Desea continuar?\n[S] SÍ - [N] NO\n: ")
        if restart == 's' or restart == 'S':
            continue
        elif restart == 'n' or restart == 'N':
            print("\n")
            print('*'*18)
            print(" FIN DEL PROGRAMA")
            print('*'*18)
            break
        else:
            print("\n¡¡ OPCIÓN EQUIVOCADA !!")

    # salir del programa
    elif opcion == 'x' or opcion == 'X':
        print("\n")
        print('*'*18)
        print(" FIN DEL PROGRAMA")
        print('*'*18)
        #opcion = 'x'
        break
    else:
        print("\n¡¡ OPCIÓN EQUIVOCADA !!")
        print("\n¡¡ REGRESANDO AL MENU PRINCIPAL !!")
        print("\n")
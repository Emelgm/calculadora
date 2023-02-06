import math as ma

def calculo_circuitos ():
    opcion_2 = input("\nCalcular circuitos\n[A] - En serie\n[B] - En paralelo\n[X] - Menú Principal\n\nOpción: ")
    
    # circuito en serie
    if opcion_2 == 'a' or opcion_2 == 'A':
        print("\nCircuitos en serie")
        result = 0
        cantidad = int(input("\nCantidad de Resistencias a calcular: "))
        for i in range(1, cantidad + 1):
            r = float(input(f"Valor de R{i} en kΩ: "))
            result += r
        print(f"\nLa Resistencia resultante es: {round(result,2)} kΩ")
        calculo_circuitos ()
    # cricuito en paralelo
    elif opcion_2 == 'b' or opcion_2 == 'B':
        print("\nCircuitos en paralelo")
        result = 0
        cantidad = int(input("\nCantidad de Resistencias a calcular: "))
        for i in range(1, cantidad + 1):
            r = float(input(f"Valor de R{i} en kΩ: "))
            result = result+(1/r)
            rtotal = 1/result
        print(f"\nLa Resistencia resultante es: {round(rtotal,2)} kΩ")
        calculo_circuitos ()
    elif opcion_2 == 'x' or opcion_2 == 'X':
        pass
    else:
        print("\n¡¡ OPCIÓN EQUIVOCADA !!")
        calculo_circuitos ()

def calculo_ley_ohm ():
    print("\nLey de Ohm")
    omh = input("[A] - Voltaje\n[B] - Corriente\n[C] - Resistencia\n[X] - Menú Principal\n\nOpción: ")
    #Calculo Voltaje
    if omh == 'a' or omh == 'A':
        print("\nVoltaje ----> V = I * R")
        corriente = float(input("Valor de I en mA: "))
        resistencia = float(input("Valor de R en kΩ: "))
        voltaje = corriente * resistencia
        print(f"Voltaje = {round(voltaje,3)}")
        calculo_ley_ohm ()
    #Calculo Corriente
    elif omh == 'b' or omh == 'B':
        print("\nCorriente ---> I = V / R")
        voltaje = float(input("Valor de V: "))
        resistencia = float(input("Valor de R en kΩ: "))
        corriente = voltaje / resistencia
        print(f"Corriente = {round(corriente, 3)} mA")
        calculo_ley_ohm ()
    #Calculo Resistencia
    elif omh == 'c' or omh == 'C':
        print("\nResistencia ----> R = V / I")
        voltaje = float(input("Valor de V: "))
        corriente = float(input("Valor de I en mA: "))
        resistencia = voltaje / corriente
        print(f"Resistencia = {round(resistencia, 2)} kΩ")
        calculo_ley_ohm ()
    elif omh == 'x' or omh == 'X':
        pass
    else:
        print("\n¡¡ OPCIÓN EQUIVOCADA !!")
        calculo_ley_ohm ()

def calculo_onda ():
    print("\nCalcular parámetros de una onda")
    param = input("[A] - Longitud\n[B] - Frecuencia\n[C] - Velocidad\n[X] - Menú Principal\n\nOpción: ")
    if param == 'a' or param == 'A':
        print("\nFórmula ----> λ = v / f\n")
        velocidad = float(input("Valor de V m/s: "))
        frecuencia = float(input("Valor de F en Hz: "))
        longitud = velocidad/frecuencia
        print(f"\nLa longitud de onda es λ = {round(longitud,2)} m")
        calculo_onda ()
    elif param == 'b' or param == 'B':
        print("\nFórmula ----> f = v / λ\n")
        velocidad = float(input("Valor de V m/s: "))
        longitud = float(input("Valor de λ en m: "))
        frecuencia = velocidad/longitud
        print(f"\nLa frecuencia de la onda es f = {round(frecuencia,2)} Hz")
        calculo_onda ()
    elif param == 'c' or param == 'C':
        print("\nFórmula ----> v = λ * f\n")
        frecuencia = float(input("Valor de F en Hz: "))
        longitud = float(input("Valor de λ en m: "))
        velocidad = frecuencia*longitud
        print(f"\nLa velocidad de la onda es v = {round(velocidad,2)} m/s")
        calculo_onda ()
    elif param == 'x' or param == 'X':
        pass
    else:
        print("\n¡¡ OPCIÓN EQUIVOCADA !!")
        calculo_onda ()

def calculo_potencia ():
    print("\nCalcular la Potencia")
    dato = input("[A] - dBm a Watts\n[B] - Watts a dBm\n[C] - mW a dBm\n[D] - dBm a mW\n[X] - Menú Principal\n\nOpción: ")
    if dato == 'a' or dato == 'A':
        print("\nFórmula ----> P(W) = 10**((P(dBm)- 30) / 10)\n")
        potenw= float(input("Ingrese el valor a convertir en dBm: "))
        resultw = 10**((potenw-30)/10)
        print (f"La potencia en Watts es = {resultw} Watts")
        calculo_potencia ()
    elif dato == 'b' or dato == 'B':
        print("\nFórmula ----> P(dBm) = 10 * log10( P(W) / 1W) + 30")
        potendb = float(input("Ingrese el valor a convertir en Watts: "))
        resultdb = 10*(ma.log10(potendb))+30
        print (f"La potencia en dBm es = {round(resultdb,2)} dBm")
        calculo_potencia ()
    elif dato == 'c' or dato == 'C':
        print("\nFórmula ----> P(dBm) = 10 * log10( P(mW) / 1mW)")
        potendb = float(input("Ingrese el valor a convertir en mW: "))
        resultdb = 10*(ma.log10(potendb/1))
        print (f"La potencia en dBm es = {round(resultdb,2)} dBm")
        calculo_potencia ()
    elif dato == 'd' or dato == 'D':
        print("\nFórmula ----> P(mW) = 1mW * 10(P(dBm) / 10)")
        potendb = float(input("Ingrese el valor a convertir en dBm: "))
        resultdb = (10**(potendb/10))
        print (f"La potencia en dBm es = {round(resultdb,2)} mW")
        calculo_potencia ()
    elif dato == 'x' or dato == 'X':
        pass
    else:
        print("\n¡¡ OPCIÓN EQUIVOCADA !!")
        calculo_potencia ()

def  finalizar ():
    print("\n")
    print('*'*18)
    print("FIN DEL PROGRAMA")
    print('*'*18)
    print("\n")

if __name__ == "__main__":

    opcion = ''
    #Ciclo general
    while opcion != 'x' or opcion != 'X':
        print("\n \n")
        print('*'*45)
        print("""    
                           MENU

             [A] - Cálculo de resistencia de circuitos
             [B] - Ley de Ohm
             [C] - Cálculo de una onda
             [D] - Calculo de Potencia

             [X] - FINALIZAR
                 """)
        print('*'*45)
        print("\n")
        opcion = input("Seleccione la opción a calcular: ")

        if opcion == 'a' or opcion == 'A':
            calculo_circuitos ()  
        elif opcion == 'b' or opcion == 'B':
            calculo_ley_ohm ()
        elif opcion == 'c' or opcion == 'C':
            calculo_onda ()   
        elif opcion == 'd' or opcion == 'D':
            calculo_potencia () 
        elif opcion == 'x' or opcion == 'X':
            finalizar ()   
            break
#
#
#

def leer_numero():
    numero = False
    while numero == False:
        try:
            numero = int(input("Introduce un número entero (0 para terminar): "))
            return numero
        except ValueError:
            print("*ERROR* Por favor, introduce un número entero.")

def calcular_suma_positivos():
    suma = 0
    flag = False
    while flag == False:
        numero = leer_numero()
        if numero == 0:
            break
        if numero > 0:
            suma += numero
    return suma

def main():
    total = calcular_suma_positivos()
    print(f"La suma de todos los números introducidos es: {total}")

if __name__ == "__main__":
    main()
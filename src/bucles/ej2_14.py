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

def calcular_suma():
    suma = 0
    flag = False
    while flag == False:
        numero = leer_numero()
        if numero == 0:
            break
        suma += numero
    return suma

def main():
    total = calcular_suma()
    print(f"La suma de todos los números introducidos es: {total}")

if __name__ == "__main__":
    main()
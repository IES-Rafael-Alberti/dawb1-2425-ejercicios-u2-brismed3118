#
#   Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.
# 

def introducir_num():

    num = None

    while num == None:

        try:
            num = int(input("Introduce un número mayor que 1 (Introduce 0 para terminar): "))

            if num <= 1 and num != 0:

                num = None
                e = IndexError("El número debe ser mayor que 1.")
                raise e
            
        except ValueError:
            print("*ERROR* El formato no es válido.")

        except IndexError as e:
            print(f"*ERROR* {e}")

    return num

def comprobar_primo(numeros: int):

    total = 1

    for i in range (1, numeros):
        total *= i 

    total += 1

    if total % numeros == 0:

        return True
    
    else:

        return False

def main():

    numeros = None
    primos = 0
    
    while numeros != 0:

        numeros = introducir_num()

        if numeros != 0:

            if comprobar_primo(numeros) == True:
                primos += 1

    print(f"La cantidad de números primos introducidos es {primos}")

if __name__ == "__main__":
    main()
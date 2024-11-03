#
# Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene. Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.
#

def contar_pares(numero):

    pares = 0

    for i in str(numero):
        if int(i) % 2 == 0:
            pares += 1
    
    print(f"El número {numero} contiene {pares} números pares.")
    

    return pares

def contar_impares(numero):
    impares = 0

    for i in str(numero):
        if int(i) % 2 != 0:
            impares += 1
    
    print(f"El número {numero} contiene {impares} números impares.")

    return impares

def introducir_numero():

    numero = None
    
    while numero == None:
        try:
            numero = int(input("Introduce un número entero positivo (0 para terminar): "))
            
            if numero < 0:
                numero = None
                e = IndexError(("Número inválido."))
                raise e
                
        except ValueError:
            print("*ERROR* Formato no válido.")
        
        except IndexError as e:
            print(f"*ERROR* {e}")
    
    return numero


def main():

    numero = None
    total_pares = 0
    total_impares = 0
    while numero != 0:

        numero = introducir_numero()

        if numero != 0:

            total_pares += contar_pares(numero)
            total_impares += contar_impares(numero)

        else:
            print(f"El total de números pares ha sido {total_pares} y de números impares {total_impares}")
            break

if __name__ == "__main__":
    main()
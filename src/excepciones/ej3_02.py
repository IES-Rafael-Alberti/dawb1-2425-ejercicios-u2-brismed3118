#
#
#

def introducir_numero():

    num = None

    while num == None:

        try:
            num = int(input("Introduce un número: "))

            if num < 0:

                num = None
                e = IndexError("El número no puede ser negativo.")
                raise e
        
        except ValueError:
            print("*ERROR* El formato no es válido.")

        except IndexError as e:
            print(f"*ERROR* {e}")

    return num

def encontrar_impares(num: int):

    impares = ""

    for i in range (1, num + 1):

        if i % 2 == 1:
            impares += str(i) + ", "

    impares = impares[:-2]
    
    return impares      

def main():
    num = introducir_numero()
    print(encontrar_impares(num))

if __name__ == "__main__":
    main()
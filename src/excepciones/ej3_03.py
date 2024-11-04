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

def cuenta_atras(num: int):

    cuenta = ""

    for i in range (0, num + 1):

        if i == 0:
            cuenta = str(i)

        else:
            cuenta = str(i) + ", " + cuenta

    return cuenta      

def main():
    
    num = introducir_numero()
    print(cuenta_atras(num))

if __name__ == "__main__":
    main()
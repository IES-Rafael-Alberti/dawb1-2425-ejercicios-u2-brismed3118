#
#
#

def introducir_numero():

    num = None

    while num == None:

        try:
            num = int(input("Introduce un número: "))

        except ValueError as e:
            print("La entrada no es correcta.")
            raise e

    return num     

def main():
    
    introducir_numero()

if __name__ == "__main__":
    main()
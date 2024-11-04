#
#   PLANTILLA PARA MAIN
#

def mostrar_edad(edad:int):
    i = 0
    for i in range (1, edad + 1):
        print (i)

def main():
    try:
        edad = int(input("Introduce tu edad: "))
        mostrar_edad(edad)

    except ValueError:
        print("**ERROR**")

if __name__ == "__main__":
    main()
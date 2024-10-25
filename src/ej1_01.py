#
#
#

def comprobar_edad(edad:int) -> bool:
    if edad >= 18:
        return True
    else:
        return False


def main():
    edad = int(input("Introduce tu edad: "))
    if comprobar_edad(edad) == True:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")
        

if __name__ == "__main__":
    main()
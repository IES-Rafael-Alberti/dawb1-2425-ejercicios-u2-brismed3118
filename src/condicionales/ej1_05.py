#
# 
#

def tributa(edad: int, salario: int) -> bool:
    if edad > 16 and salario >= 1000:
        return True
    else:
        return False


def main():
    edad = None
    salario = None

    while edad == None or salario == None:
        try:
            edad =  int(input("Introduzca su edad: "))
            salario = int(input("Introduzca su salario mensual: "))
        except ValueError:
            print("**ERROR** Edad o salario no válidos")

    if tributa(edad, salario) == True:
        print("Tributa")
    else:
        print("No tributa")

    pass

if __name__ == "__main__":
    main()
#
#
#

def comprobar_par(num: int) -> bool:
    resto = num % 2

    if resto == 0:
        return True
    else:
        return False
        
def main():
    num = int(input("Introduce un número entero: "))

    if num == 0:
        num = int(input("Mmm... No me sirve, prueba con otro: "))


    if comprobar_par(num) == True:
        print("El número es par")

    else:
        print("El número es impar")

if __name__ == "__main__":
    main()
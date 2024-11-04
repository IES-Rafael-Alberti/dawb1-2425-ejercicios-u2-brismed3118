#
#
#

def comprobar_tramo(renta: float):

    if renta < 10000:
        print("El tio de impositivo es 5%")
    if renta >= 10000 and renta < 20000:
        print("El tio de impositivo es 15%")
    if renta >= 20000 and renta < 35000:
        print("El tio de impositivo es 20%")
    if renta >= 35000 and renta < 60000:
        print("El tio de impositivo es 30%")
    if renta >= 60000:
        print("El tio de impositivo es 45%")   

def main():
    renta = None

    while renta == None:
        try:
            renta = float(input("Introduzca su renta anual: "))
            if renta < 0:
                renta = None
                raise ValueError
        except ValueError:
            print("**ERROR** Esa no es una renta válida...")
            renta == None

    
    comprobar_tramo(renta)
if __name__ == "__main__":
    main()
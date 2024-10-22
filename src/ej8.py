#
#
#

def tipo_rendimiento(rend:float) -> str:

    if rend == 0:
        rend = "Inaceptable"
        return rend
    if rend == 0.4:
        rend = "Aceptable"
        return rend
    if rend == 0.6:
        rend = "Meritorio"
        return rend

def calcular_dinero(rend:float) -> float:

    if rend == 0:
        return 0
    if rend == 0.4:
        dinero = 2400 * 0.4
        return dinero
    if rend == 0.6:
        dinero = 2400 * 0.6
        return dinero


def aproximar(rend: float) -> float:

    if rend < 0.4:
        rend = 0
    elif rend >= 0.4 and rend < 0.6:
        rend = 0.4
    elif rend >= 0.6:
        rend = 0.6
    
    return rend


def comprobar_rent() -> float:

    rend = None
    while rend == None:
        try:
            rend = float(input("Introduce el rendimiento con valores entre 0.0 y 1: "))
            if rend < 0 or rend > 1:
                raise ValueError("Ese valor no se encuentra en el rango o no es correcto...")
        except ValueError as e:
            if rend is None:
                print()
            else:
                rend = None
                print(f"**ERROR** {e}")
    return rend


def main():
    
    rend = comprobar_rent()
    rend = aproximar(rend)
    dinero = calcular_dinero(rend)
    rend = tipo_rendimiento(rend)
    print(f"El usuario ha tenido un rendimiento {rend} y recibirá {dinero}€")
    

if __name__ == "__main__":
    main()
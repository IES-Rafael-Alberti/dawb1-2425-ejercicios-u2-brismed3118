#
#
#

def introducir_montos():
    monto = None
    
    while monto == None:
        try:
            monto = float(input("Introduce el monto de la compra (0 para terminar): "))

            if monto < 0:
                monto = None
                e = IndexError("No puede ser negativo.")
                raise e
                
        except ValueError:
            print(f"*ERROR* Formato no válido...")

        except IndexError as e:
            print(f"*ERROR* {e}")
    
    return monto

def calcular_total(total, monto):
    total += monto
    return total

def aplicar_descuento(total):

    if total > 1000:
        descuento = total * 0.10
        total -= descuento
        print(f"Se ha aplicado un descuento del 10%. El total es: {total:.2f}€.")

    else:
        print(f"Total a pagar: {total:.2f}€.")
    
    return total

def main():

    monto = None
    total = 0

    while monto != 0:
        monto = introducir_montos()
        total = calcular_total(total, monto)

    aplicar_descuento(total)

if __name__ == "__main__":
    main()
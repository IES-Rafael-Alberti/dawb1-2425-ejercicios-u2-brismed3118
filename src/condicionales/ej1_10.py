#
#
#

def ingrediente_pizza(tipo: str) -> str:

    if tipo == "vegetariana":
        ingrediente = None
        while ingrediente == None:
            try:
                ingrediente = input("Elige el ingrediente que quieres: Pimiento o tofu: ")
                ingrediente = ingrediente.lower()
                if ingrediente != "pimiento" and ingrediente != "tofu":
                    ingrediente = None
                    raise ValueError
            except ValueError:
                print("**ERROR** Tipo de dato inválido")
    elif tipo == "no vegetariana":
        ingrediente = None
        while ingrediente == None:
            try:
                ingrediente = input("Elige el ingrediente que quieres: Peperoni, jamon y salmon: ")
                ingrediente = ingrediente.lower()
                if ingrediente != "peperoni" and ingrediente != "jamon" and ingrediente != "salmon":
                    ingrediente = None
                    raise ValueError
            except ValueError:
                print("**ERROR** Tipo de dato inválido")
    
    return ingrediente

def tipo_pizza() -> str:
    tipo = None

    while tipo == None:
        try:
            tipo = input("Qué tipo de pizza quieres, vegetariana o no vegetariana? ").lower()
            if tipo !=  "vegetariana" and tipo != "no vegetariana":
                tipo = None
                raise ValueError("Esa pizza no es válida, inténtalo de nuevo...")
        except ValueError:
            print("**ERROR**Tipo de dato inválido")
    
    return tipo

def main():
    tipo = tipo_pizza()
    ingrediente = ingrediente_pizza(tipo)
    print(f"La pizza que has elegido es una {tipo} con {ingrediente}, mozzarella y tomate.")

if __name__ == "__main__":
    main()
import os

def borrar_e_imprimir(numero):
    """Borra la terminal e imprime el número proporcionado."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(numero)

def main():
    numero = 0
    while numero <= 50:
        entrada = input("Presiona 'n' y Enter para incrementar el número o cualquier otra tecla y Enter para salir: ")
        if entrada == 'n':
            numero += 1
            borrar_e_imprimir(numero)
        else:
            break

if __name__ == "__main__":
    main()
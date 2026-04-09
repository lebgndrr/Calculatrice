print("""
╔══════════════════════╗
║    CALCULATRICE     ║
╚══════════════════════╝
""")

def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

while True:
    print("\n1) Addition")
    print("2) Soustraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Quitter")

    try:
        choix = int(input("Choisissez une opération: "))

        if choix == 5:
            print("Au revoir")
            break

        if choix not in [1, 2, 3, 4]:
            print("Choix invalide")
            continue

        nombre1 = float(input("Entrez le premier nombre: "))
        nombre2 = float(input("Entrez le deuxième nombre: "))

        if choix == 1:
            print("Résultat:", addition(nombre1, nombre2))
        elif choix == 2:
            print("Résultat:", soustraction(nombre1, nombre2))
        elif choix == 3:
            print("Résultat:", multiplication(nombre1, nombre2))
        elif choix == 4:
            if nombre2 == 0:
                print("Impossible de diviser par 0")
            else:
                print("Résultat:", division(nombre1, nombre2))

    except ValueError:
        print("Entrée invalide (nombre attendu)")
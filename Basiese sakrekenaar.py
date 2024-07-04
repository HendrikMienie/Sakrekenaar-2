# Sakrekenaar funksie vir optelling
def add(x, y):
    return x + y

# Sakrekenaar funksie vir aftrekking
def subtract(x, y):
    return x - y

# Sakrekenaar funksie vir vermenigvuldiging
def multiply(x, y):
    return x * y

# Sakrekenaar funksie vir deling
def divide(x, y):
    if y == 0:
        return "Fout: kan nie deur nul deel nie"
    return x / y

# Hoofprogram van die sakrekenaar
def main():
    while True:
        # Druk die menu uit
        print("\nKies 'n rekenkundige bewerking:")
        print("1. Plus (+)")
        print("2. Minus (-)")
        print("3. Maal (*)")
        print("4. Deel (/)")
        print("5. Afsluit")

        # Vra die gebruiker om 'n keuse te maak
        choice = input("Gee jou keuse (1/2/3/4/5): ")

        # Verwerk die keuse
        if choice == '5':
            print("Uitvoer die sakrekenaar.")
            break  # Verlaat die lus as die keuse 5 is

        # Vra die gebruiker om twee getalle in te voer
        num1 = float(input("Gee die eerste getal: "))
        num2 = float(input("Gee die tweede getal: "))

        # Voer die rekenkundige bewerking uit gebaseer op die keuse
        if choice == '1':
            result = add(num1, num2)
            print(f"\nUitkoms: {num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"\nUitkoms: {num1} - {num2} = {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"\nUitkoms: {num1} * {num2} = {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"\nUitkoms: {num1} / {num2} = {result}")
        else:
            print("Ongeldige keuse. Probeer weer.")

if __name__ == "__main__":
    main()

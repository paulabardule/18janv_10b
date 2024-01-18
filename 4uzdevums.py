# Faila nosaukums ir vards un paplašinājums ir txt
def lasit_failu(fails):
    try:
        with open(fails, 'r', encoding='utf-8') as faila_objekts:
            saturs=faila_objekts.read()
            print(f"Faila saturs:\n{saturs}")
    except FileNotFoundError:
        print("Norādītais fails nav atrasts.")
    except Exception as e:
        print(f"Kļūda: {e}")

def main():
    try:
        faila_nosaukums = input("Ievadiet faila nosaukumu: ")

        faila_formats = input("Ievadiet faila formātu (paplašinājumu): ")

        fails=f"{faila_nosaukums}.{faila_formats}"

        lasit_failu(fails)

    except Exception as e:
        print(f"Kļūda: {e}")

if __name__ == "__main__":
    main()